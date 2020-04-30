#!/usr/bin/env python3

import os
import sys
from PIL import Image

## FUNCTION TO TAKE HEIGHT OF IMAGE ##

def image_height_take():
    img_hei=input("\nEnter the new Height for the image : ")
    temp_hei = img_hei.isnumeric()
    if temp_hei == True:
        img_hei=int(img_hei)
        return img_hei
    else:
        print("\nHeight must be number !!\n")
        exit()

## FUNCTION TO TAKE WIDTH OF IMAGE ##

def image_width_take():
    img_wid=input("\nEnter the new Width for the image : ")
    temp_wid = img_wid.isnumeric()
    if temp_wid == True:
        img_wid=int(img_wid)
        return img_wid
    else:
        print("\n\nWidth must be number !!\n")
        exit()

def single_img_thumbnailer():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("\nEnter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("\nImage not found")
        exit()
    
    img_basename=os.path.basename(img_path)
    print(f"image basename {img_basename}")
    image = Image.open(img_path)
    print(f"\nFormat of image is : {image.format}")
    print(f"\nWidth : {image.size[0]}      Height : {image.size[1]}") ## Size of original image
    image.thumbnail((image_width_take(), image_height_take())) ## Width, Height
    image.save(f'thumbnail_{img_basename}')
    print("\nDone ✓")

def dir_image_thumbnailer_window():


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
    image_width=image_width_take()
    image_height=image_height_take()
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}\\\\{files}"):
            try:
                image = Image.open(f"{img_dir_path}\\\\{files}")
                print(f'\rThumbnailing image : {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                image.thumbnail((image_width, image_height))
                image.save(f'thumbnail_{files}')
    print("\n\nDone ✓")
    exit(0)


def dir_image_thumbnailer_other():

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("\nDirectory is empty")        
        exit(0)
    image_width=image_width_take()
    image_height=image_height_take()
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}/{files}"):
            try:
                image = Image.open(f"{img_dir_path}/{files}")
                print(f'\rThumbnailing image : {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                pass
                image.thumbnail((image_width, image_height))
                image.save(f'thumbnail_{files}')
    print("\n\nDone ✓")
    exit(0)


