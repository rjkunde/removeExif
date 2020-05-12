# removeExif
Python command line program to remove EXIF meta data from jpg images

This is a useful program to remove unnessary data from jpg image files. Modern day cameras of all shapes and sizes collect increasingly intrusive data about the image being taken. This includes camera attributes, color information, and even GPS coordinates. This data is stored inside the .jpg image file itself. Most of us upload these files to the internet and unknowingly divuldge private information. 

## Why use this?
Two reasons:
1) If you wish to wipe EXIF data from your images (GPS location, detailed camera specifications, etc).
2) Space savings. Running in "Overwrite Mode" allows images to require 40-70% less space on your computer on average.

## Prerequsites
* Python 3
* Python Image Library "Pillow"
* A directory with .jpg images in it

## Installation
1) Obtain Python 3 for your operating system: https://www.python.org/downloads/
2) Install Python 3, with pip, and make sure you instlal python to PATH so it can be called from the command line
3) Once installed, run this from command prompt/bash shell/terminal: `pip install pillow`
4) That's it!

## Running removeExif
1) Download / clone this program from Github
2) Copy removeExif.py into any directory that you wish you process images inside
3) Run the program from your OS'es command line: `python removeExif.py`
4) Follow prompts
