#!/usr/bin/env python3

import os
import sys
from PIL import Image

def single_img_rotate():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("\nEnter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("\nImage not found")
        exit()
    rot_deg=input("\nEnter the Degree of Rotation : ")
    temp_rot_deg=rot_deg.isnumeric()
    if temp_rot_deg == True:
        rot_deg=int(rot_deg)
    else:
        print("\nDegree of Rotation must be number.")
        exit(0)
    tem_rot_deg = 0 <= rot_deg <= 360
    if tem_rot_deg == False:
            print("\nDegree of Rotation must be between 0 to 360.")
            exit(0)
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    print(f"\nFormat of image is : {image.format}")
    print(f"\nDegree of  Rotation of new image is : {rot_deg}")
    image_rot=image.rotate(rot_deg, expand=True)
    image_rot.save(f'rotated_{rot_deg}_{img_basename}')
    print("\nDone ✓")

def dir_image_rotate_window():


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
    rot_deg=input("\nEnter the Degree of Rotation : ")
    temp_rot_deg=rot_deg.isnumeric()
    if temp_rot_deg == True:
        rot_deg=int(rot_deg)
    else:
        print("\nDegree of Rotation must be number.")
        exit(0)
    tem_rot_deg = 0 <= rot_deg <= 360
    if tem_rot_deg == False:
            print("\nDegree of Rotation must be between 0 to 360.")
            exit(0)
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}\\\\{files}"):
            try:
                image = Image.open(f"{img_dir_path}\\\\{files}")
            except:
                pass
            else:
                print(f'\rRotating image : {files}                                     ', end='')
                sys.stdout.flush()
                image_rot=image.rotate(rot_deg, expand=True)
                image_rot.save(f'rotated_{rot_deg}_{files}') 
    print("\n\nDone ✓")
    exit(0)


def dir_image_rotate_other():

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("\nDirectory is empty")        
        exit(0)
    rot_deg=input("\nEnter the Degree of Rotation : ")
    temp_rot_deg=rot_deg.isnumeric()
    if temp_rot_deg == True:
        rot_deg=int(rot_deg)
    else:
        print("\nDegree of Rotation must be number.")
        exit(0)
    tem_rot_deg = 0 <= rot_deg <= 360
    if tem_rot_deg == False:
            print("\nDegree of Rotation must be between 0 to 360.")
            exit(0)
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}/{files}"):
            try:
                image = Image.open(f"{img_dir_path}/{files}")
            except:
                pass
            else:
                print(f'\rRotating image : {files}                                     ', end='')
                sys.stdout.flush()
                image_rot=image.rotate(rot_deg, expand=True)
                image_rot.save(f'rotated_{rot_deg}_{files}')
    print("\n\nDone ✓")
    exit(0)
