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
neopixelsgp18 = neopixel.NeoPixel(board.GP18, NUMPIXELSGP18, brightness=1, auto_write=False)

# NeoPixel strip connected on GP20
NUMPIXELSGP20 = 2
neopixelsgp20 = neopixel.NeoPixel(board.GP20, NUMPIXELSGP20, brightness=1, auto_write=False)

# Blue/Green Common Cathode LED
d1blu = digitalio.DigitalInOut(board.GP2)
d1blu.direction = digitalio.Direction.OUTPUT
d1grn = digitalio.DigitalInOut(board.GP4)
d1grn.direction = digitalio.Direction.OUTPUT
d2blu = digitalio.DigitalInOut(board.GP6)
d2blu.direction = digitalio.Direction.OUTPUT
d2grn = digitalio.DigitalInOut(board.GP8)
d2grn.direction = digitalio.Direction.OUTPUT
d3blu = digitalio.DigitalInOut(board.GP10)
d3blu.direction = digitalio.Direction.OUTPUT
d3grn = digitalio.DigitalInOut(board.GP12)
d3grn.direction = digitalio.Direction.OUTPUT
d4blu = digitalio.DigitalInOut(board.GP14)
d4blu.direction = digitalio.Direction.OUTPUT
d4grn = digitalio.DigitalInOut(board.GP16)
d4grn.direction = digitalio.Direction.OUTPUT

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
    # ########## RED ##########
    # GRB
    neopixelsgp18[0] = (0, 255, 0)
    neopixelsgp18[1] = (0, 255, 0)
    neopixelsgp20[0] = (0, 255, 0)
    neopixelsgp20[1] = (0, 255, 0)
    #
    neopixelsgp18.show()
    neopixelsgp20.show()
    #
    d1grn.value = 0
    d1blu.value = 0
    d2grn.value = 0
    d2blu.value = 0
    d3grn.value = 0
    d3blu.value = 0
    d4grn.value = 0
    d4blu.value = 0
    #
    time.sleep(0.5)
    #
    # ########## GRN ##########
    # GRB
    neopixelsgp18[0] = (255, 0, 0)
    neopixelsgp18[1] = (255, 0, 0)
    neopixelsgp20[0] = (255, 0, 0)
    neopixelsgp20[1] = (255, 0, 0)
    #
    neopixelsgp18.show()
    neopixelsgp20.show()
    #
    d1grn.value = 1
    d1blu.value = 0
    d2grn.value = 1
    d2blu.value = 0
    d3grn.value = 1
    d3blu.value = 0
    d4grn.value = 1
    d4blu.value = 0
    #
    time.sleep(0.5)
    #
    # ########## BLU ##########
    # GRB
    neopixelsgp18[0] = (0, 0, 255)
    neopixelsgp18[1] = (0, 0, 255)
    neopixelsgp20[0] = (0, 0, 255)
    neopixelsgp20[1] = (0, 0, 255)
    #
    neopixelsgp18.show()
    neopixelsgp20.show()
    #
    d1grn.value = 0
    d1blu.value = 1
    d2grn.value = 0
    d2blu.value = 1
    d3grn.value = 0
    d3blu.value = 1
    d4grn.value = 0
    d4blu.value = 1
    #
    time.sleep(0.5)
    #
