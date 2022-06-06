# Firmware

Firmware used by the badges

## Adafruit CircuitPython

I decided to use the Adafruit CircuitPython firmware on the Raspberry Pi Pico for the corsage badge.

Nothing against Raspberry MicroPython, I just like CircuitPython more.

The Raspberry Pi Pico boards that will be provided with the badges will be preloaded with a specific Adafruit CircuitPython version

Currently using version 7.2.5 but might change as we get closer to badge release date.

In case you need to reload your board or are using a different Pico than provided I have included the uf2 firmware file I used here so you can use the same version I did.

To load the new firmware follow these simple steps:

*  Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer.
*  Release the BOOTSEL button after your Pico is connected.
*  It will mount as a Mass Storage Device called RPI-RP2
*  Drag and drop the CircuitPython UF2 file onto the RPI-RP2 volume.
*  Your Pico will reboot. You are now running CircuitPython.

If you wish to try a different version than I used then you can find all the CircuitPython for Pico downloads here:

[CircuitPython for Pico Downloads](https://circuitpython.org/board/raspberry_pi_pico/)

Note: If you upgrade the CircuitPython version you will need to download the version specific version of the library files to match the version you are running for any external libraries you are calling in your code (like neopixel.mpy).

You can download CircuitPython library files here:

[CircuitPython Library File Downloads](https://circuitpython.org/libraries)

For more information about the Raspberry Pi Pico including data sheets and downloads like their MicroPython firmware go to this page:

[Raspberry Pi Microcontrollers Documentation](https://www.raspberrypi.com/documentation/microcontrollers/)
