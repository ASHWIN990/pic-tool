#!/usr/bin/env python3

import os
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

def single_img_resize():

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
    resized_image = image.resize((image_width_take(), image_height_take())) ## Width, Height
    resized_image.save(f'resized_{img_basename}')
    print(f"\nWidth : {resized_image.size[0]}      Height : {resized_image.size[1]}") ## Size of original image
    print("\nDone ✓")


def dir_image_resize():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    for files in list_of_files:
        if os.path.isfile(img_dir_path+files):
            try:
                image = Image.open(img_dir_path+files)
            except:
                pass
            else:
                pass


single_img_resize()

