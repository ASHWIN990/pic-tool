#!/usr/bin/env python3

import os
import sys
from PIL import Image


def single_img_greyscale():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("\nEnter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("\nImage not found")
        exit()
    
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    print(f"\nFormat of image is : {image.format}")
    print(f"\nWidth : {image.size[0]}      Height : {image.size[1]}") ## Size of original image
    greyscale_image = image.convert('L')
    greyscale_image.save(f'greyscaled_{img_basename}')
    print("\nDone ✓")

def dir_image_greyscale_window():


    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("\nDirectory is empty")
        exit(0)
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}\\\\{files}"):
            try:
                image = Image.open(f"{img_dir_path}\\\\{files}")
                print(f'\rGreyscaling image : {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                greyscale_image = image.convert('L')
                greyscale_image.save(f'greyscaled_{files}')
    print("\n\nDone ✓")
    exit(0)


def dir_image_greyscale_other():

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("\nDirectory is empty")        
        exit(0)
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}/{files}"):
            try:
                image = Image.open(f"{img_dir_path}/{files}")
                print(f'\rGreyscaling image : {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                pass
                greyscale_image = image.convert('L')
                greyscale_image.save(f'greyscaled_{files}')
    print("\n\nDone ✓")
    exit(0)
