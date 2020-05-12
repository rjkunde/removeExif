# removeExif
Python command line program to remove EXIF meta data from jpg images

This is a useful program to remove unnecessary  data from jpg image files. Modern day cameras of all shapes and sizes collect increasingly intrusive data about the images being taken. This includes camera attributes, color information, and even GPS coordinates. This data is stored inside the .jpg image file itself. Most of us upload these files to the internet and unknowingly divulge private information.

This program leverages the Python Image Library and your input to operate in one of two modes: Copy Mode - which creates an EXIF sanitized clone of your files, or Overwrite Mode - which removes EXIF data directly from your images .

## Why use this?
Two reasons:
1) If you wish to wipe EXIF data from your images (GPS location, detailed camera specifications, etc).
3) If you're an avid user of social media, you'll likely wish to post EXIF sanitized photos so people can't track you.
2) Space savings. Running in "Overwrite Mode" allows images to require 40-70% less space on your computer on average.

## Prerequisites
* Python 3
* Python Image Library "Pillow"
* A directory with .jpg images in it

## Installation
1) Obtain Python 3 for your operating system: https://www.python.org/downloads/
2) Install Python 3, include pip, and make sure python is present into PATH so it can be called from the command line
3) Once installed, run this from command prompt/bash shell/terminal: `pip install pillow`
4) That's it!

## Running removeExif.py
1) Download / clone this program from Github
2) Copy removeExif.py into any directory that you wish you process images inside
3) Open of a command prompt, terminal, or shell and change directory to your image folder 
3) Run `python removeExif.py`
4) Follow prompts
