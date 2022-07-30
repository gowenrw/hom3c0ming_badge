import board
import digitalio
import time
import neopixel
import pwmio

# On board LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# WS2812D Reversed Pin 'NeoPixel' LEDs
# Note: NeoPixel Values specified as (G, R, B)

# NeoPixel strip connected on GP18
NUMPIXELSGP18 = 2
neopixelsgp18 = neopixel.NeoPixel(board.GP18, NUMPIXELSGP18, brightness=0.5, auto_write=False)

# NeoPixel strip connected on GP20
NUMPIXELSGP20 = 2
neopixelsgp20 = neopixel.NeoPixel(board.GP20, NUMPIXELSGP20, brightness=0.5, auto_write=False)

# Blue/Green Common Cathode LED
d1blu = pwmio.PWMOut(board.GP2, frequency=5000, duty_cycle=0)
d1grn = pwmio.PWMOut(board.GP4, frequency=5000, duty_cycle=0)
d2blu = pwmio.PWMOut(board.GP6, frequency=5000, duty_cycle=0)
d2grn = pwmio.PWMOut(board.GP8, frequency=5000, duty_cycle=0)
d3blu = pwmio.PWMOut(board.GP10, frequency=5000, duty_cycle=0)
d3grn = pwmio.PWMOut(board.GP12, frequency=5000, duty_cycle=0)
d4blu = pwmio.PWMOut(board.GP14, frequency=5000, duty_cycle=0)
d4grn = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)

# Function to give us a nice color swirl on NeoPixel (G,R,B)
def wheeln(pos, sft):
    # pos = position, sft = shift-position
    #
    # Want a minimum of red since these are flowers
    redmin = 30
    if (pos + sft) > 255:
        pos = (pos + sft) - 256
    else:
        pos = (pos + sft)
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(pos*3), int(max(redmin, (255 - pos*3))), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos*3)), redmin, int(pos*3))
    else:
        pos -= 170
        return (0, int(max(redmin, (pos*3))), int(255 - pos*3))

# Function to turn on/off led
def leaf(pos, sft, brt, min):
    # pos = position, sft = shift-position, brt = brightness (0.1-1.0), min = minimum
    #
    # Set maximum leaf brightness
    # Full=65535 Half=32768 Quarter=16384
    # Setting to Full-value * brightness-value
    leafhigh = 65535 * brt
    if (pos + sft) > 255:
        pos = (pos + sft) - 256
    else:
        pos = (pos + sft)
    if (pos) < 128:
        leafstate = int(max(min, (pos * 2 * leafhigh / 255)))
    else:
        leafstate = int(max(min, (leafhigh - int((pos - 128) * 2 * leafhigh / 255))))
    return leafstate

# Function to turn all LEDs off in a neopixel string
def alloff(pixel):
    for j in range(len(pixel)):
        pixel[j] = (0, 0, 0)

######################### MAIN LOOP ##############################
i = 0
alloff(neopixelsgp18)
alloff(neopixelsgp20)
while True:
    led.value = 1
    #
    # D501
    neopixelsgp18[0] = wheeln(i, 0)
    # D502
    neopixelsgp18[1] = wheeln(i, 32)
    # D601
    neopixelsgp20[0] = wheeln(i, 64)
    # D602
    neopixelsgp20[1] = wheeln(i, 96)
    #
    neopixelsgp18.show()
    neopixelsgp20.show()
    #
    d1grn.duty_cycle = leaf(i, 0, 0.6, 6554)
    d1blu.duty_cycle = leaf(i, 32, 0.4, 0)
    d2grn.duty_cycle = leaf(i, 32, 0.6, 6554)
    d2blu.duty_cycle = leaf(i, 64, 0.4, 0)
    d3grn.duty_cycle = leaf(i, 64, 0.6, 6554)
    d3blu.duty_cycle = leaf(i, 96, 0.4, 0)
    d4grn.duty_cycle = leaf(i, 96, 0.6, 6554)
    d4blu.duty_cycle = leaf(i, 128, 0.4, 0)
    #
    print("i: ", i, " d1grn: ", d1grn.duty_cycle, " d1blu: ", d1blu.duty_cycle, " d501(G,R,B): ", neopixelsgp18[0])
    #
    i = (i+1) % 256
    #
    time.sleep(0.02) # make bigger to slow down
