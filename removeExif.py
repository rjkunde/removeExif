#!/usr/bin/env python

# removeExif Python Program
# Removes EXIF meta data from jpg images
# RJ Kunde
# 5/11/2020
# https://github.com/rjkunde/removeExif

from PIL import Image
import time
import os
import sys

directory = os.getcwd()
  
def loadProgram():
    print()
    print("Python jpg exif data remover by RJ Kunde - 2020")
    time.sleep(1.0)
    main()
    
# Main Menu Function 
# Provides choices, captures user input              
def main():
    
    # Main Menu
    choice = input("""
                      Main Menu
                      1: Copy Mode - Leave orignal images intact, de-exif the copies only
                      2: Overwrite Mode - de-exif existing files, do not make copies
                      3: Exit Program

                      Please enter your choice: """)
    
    if choice == "1":
        copyMenu()
    elif choice == "2":
        overwriteMenu()
    elif choice == "3":
        print("Adios!")
        sys.exit        
    else:
        print("Invalid Selection")
        print("Please try again")
        main()

# Copy Mode Menu
# Allows user to kick-off image clone and de-exif function copyMode()        
def copyMenu():
    print()
    print()
    print("Copy Mode Selected - You like to play it safe!")
    print("Warning: this mode uses approximately 50% additional disk space than your current images.")
    print("A de-exif'ed copy of each image will be created in the directory where this program was executed.")
    print()
    time.sleep(1.0)
    copyChoice =  input("Shall we begin? y/n: ")
    if copyChoice == "y" or copyChoice == "Y":
        copyMode()
    elif copyChoice == "n" or copyChoice == "N":
        main()        
    else:
        print("Invalid Selection")
        print("Please try again")
        copyMenu()

# Copy Mode Main Function
# Iterates over all files in a directory
# Checks for jpg or jpeg, ignores already processed files (noexif_), ignores removeExif.py or any other filetypes
# Opens image, creates a new saved copy which doesn't contain EXIF data 
def copyMode():
    print("Starting Python exif data remover in Copy Mode!")
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            if filename.startswith("noexif_"):
                print("Skipped: " + directory + filename + " it has already had exif data removed")
            else:
                try:
                    print("Processed:  " + (os.path.join(directory, filename)))
                    image = Image.open(filename)
                    image.save("noexif_" + filename)
                except:
                    print("Error processing: " + directory + filename)
        else:
            if filename.startswith("removeExif"):
                pass
            else:
                print("Skipped: " + directory + filename + " it is not a .jpg or .jpeg")
    print()               
    print("Your images have been processed! See output log above for any issues.")

# Overwrite Mode Menu
# Allows user to kick-off image de-exif function overwriteMode() 
def overwriteMenu():
    print()
    print()
    print("Overwrite Mode Selected - You like to live dangerously!")
    print("Warning: this mode removes exif meta data from existing images. There is inherent risk of data loss!")
    print("Each image in the same directory as this program will be opened, de-exif'ed, saved and closed.")
    print()
    time.sleep(1.0)
    overwriteChoice =  input("Shall we begin? y/n: ")
    if overwriteChoice == "y" or overwriteChoice == "Y":
        overwriteMode()
    elif overwriteChoice == "n" or overwriteChoice == "N":
        main()        
    else:
        print("Invalid Selection")
        print("Please try again")
        overwriteMenu()

# Overwrite Mode Main Function
# Iterates over all files in a directory
# Checks for jpg or jpeg, ignores already processed files (noexif_), ignores removeExif.py or any other filetypes
# Opens image, removes EXIF data via PIL Open(), saves file - thus removing EXIF data
def overwriteMode():
    print("Starting Python exif data remover in Overwrite Mode!")
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            if filename.startswith("noexif_"):
                print("Skipped " + directory + filename + " it has already had its exif data removed")
            else:
                try:
                    print("Processed:  " + (os.path.join(directory, filename)))
                    image = Image.open(filename)
                    image.save(filename)
                except:
                    print("Error processing: " + directory + filename)
        else:
            if filename.startswith("removeExif"):
                pass
            else:
                print("Skipped: " + directory + filename + " it is not a .jpg or .jpeg")
    print()               
    print("Your images have been processed! See output above for any issues.")

# Start Program
loadProgram()

