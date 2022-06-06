# hom3c0ming_badge

This is a DEFCON Indie badge created for D3FC0N HOM3C0MING a.k.a. DC30.

This is where all the files for the hom3c0ming_badge project will be stored.

This includes code and art and cad and fab and 3D files.  All the things.

## File Structure

This is the file structure of this repository

* [/](/README.md) - YOU ARE HERE
* [/3D/](./3D/) - 3D print artifacts related to this project
* [/art/](./art/) - Artwork and other graphics created by this project
* [/code/](./code/) - All project related Code / Firmware
* [/docs/](./docs/) - Documentation created by this project including web pages
* [/eda/](./eda/) - Electronic Design Automation files (i.e. KiCad)
* [/reference_parts/](./reference_parts/) - Documentation pulled from other sources related to components
* [./README.md](/README.md) - This File
* [./LICENSE](/LICENSE) - Currently set to MIT

Note: the reference_parts directory is a link to a submodule repository.
To add it use the following cmd after cloning this:
```
git submodule add https://github.com/gowenrw/reference_parts reference_parts
```
This will make a link to the current commit of that repo.
To update it to a newer commit after its been added use this cmd:
```
git submodule update --recursive
```
