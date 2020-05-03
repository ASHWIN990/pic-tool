#!/usr/bin/env python3

import os
import sys
from PIL import Image

def single_img_compress():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("Enter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("Image not found")
        exit()
    compr_rat=input("Enter the Compress Ratio (ex: 50) : ")
    compr_rat_tmp = compr_rat.isnumeric()
    if compr_rat_tmp == True:
        compr_rat=int(compr_rat)
    else:
        print("Compress Ratio must be number.")
        exit(0)
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    print(f"Format of image is : {image.format}")
    print(f"Compression Ration of image is : {compr_rat}")
    image.save(f'compressed_{img_basename}', quality=compr_rat)
    print("Done ✓")

def dir_image_compress_window():


    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("Directory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("Directory is empty")
        exit(0)
    compr_rat=input("\nEnter the Compress Ratio (ex: 50) : ")
    compr_rat_tmp = compr_rat.isnumeric()
    if compr_rat_tmp == True:
        compr_rat=int(compr_rat)
    else:
        print("Compress Ratio must be number.")
        exit(0)
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}\\\\{files}"):
            try:
                image = Image.open(f"{img_dir_path}\\\\{files}")
            except:
                pass
            else:
                print(f'\rCompressing image : {files}                                     ', end='')
                sys.stdout.flush()
                image.save(f'compressed_{files}', quality=compr_rat)
    print("Done ✓")
    exit(0)


def dir_image_compress_other():

    img_dir_path=input("Enter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("Directory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("Directory is empty")        
        exit(0)
    compr_rat=input("Enter the Compress Ratio (ex: 50) : ")
    compr_rat_tmp = compr_rat.isnumeric()
    if compr_rat_tmp == True:
        compr_rat=int(compr_rat)
    else:
        print("Compress Ratio must be number.\n")
        exit(0)
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}/{files}"):
            try:
                image = Image.open(f"{img_dir_path}/{files}")
            except:
                pass
            else:
                print(f'\rCompressing image : {files}                                     ', end='')
                sys.stdout.flush()
                image.save(f'compressed_{files}', quality=compr_rat)
    print("Done ✓")
    exit(0)

