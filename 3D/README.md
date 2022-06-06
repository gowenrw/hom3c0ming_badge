# 3D

This is where all the 3D print artifacts for this project are located.

This project uses translucent 3D printed LED covers.

The LED covers are designed to be screwed to the PCB using M2 self threading screws (i.e.,  wood/machine screws, not bolts) via designated drill holes in the PCB.

## 3D STL Files

There is a 3D Model I created for the Rose shaped LED cover.
This has been provided in several STL files for printing (quantity differences supporting different print bed sizes or time constraints).

Here are the STL files:

*  [Rose_LED_Cover_w_Leaves.stl](Rose_LED_Cover_w_Leaves.stl)
*  [Rose_LED_Cover_w_Leaves_x15.stl](Rose_LED_Cover_w_Leaves_x15.stl)
*  [Rose_LED_Cover_w_Leaves_x20.stl](Rose_LED_Cover_w_Leaves_x20.stl)
*  [Rose_LED_Cover_w_Leaves_x40.stl](Rose_LED_Cover_w_Leaves_x40.stl)

## My Setup

I own a FlashForge Adventurer 3 printer which I slice prints for using FlashPrint, and a Creality Ender 3V2 which I slice prints for using Cura.

The directory FlashForgeAdv3 contains my FlashPrint project files, printer configuration profiles, and gcode for various STL files above.

The directory Ender3V2_Cura contains my Cura project files, printer configuration profiles, and gcode for various STL files above.

## Custom profile settings and material for this project

The material I am using for this project is the [Amazon Basics PLA 3D Printer Filament, 1.75mm, Translucent, 1 kg Spool](https://www.amazon.com/dp/B07SZLZG3L).

As you are setting up your machine to print these parts here are some notes about what I changed from my default print setting and why:

*  Layer height 0.16mm - Setting just a bit better than standard 0.2mm layers makes a big difference in the quality without that much added time.
*  Raft with 9mm-15mm margin - Given how small the surface area of the bottom layer is compared to the height, a wide solid raft was needed to prevent tip overs during printing
