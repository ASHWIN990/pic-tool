#!/usr/bin/env python3

import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS

def single_img_meta_ext():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("\nEnter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("\nImage not found")
        exit()
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    exifdata = image.getexif()
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            try:
                data = data.decode()
            except:
                pass
        if os.path.exists(f"Exif_{img_basename}.txt"):
            tmp_file=open(f"Exif_{img_basename}.txt", "a")
            tmp_file.write(f"{tag:25}: {data}\n")
            tmp_file.close()        
            print("\nDone ✓")
        else:
            tmp_file=open(f"Exif_{img_basename}.txt", "a")
            tmp_file.write(f"{tag:25}: {data}\n")
            tmp_file.close()
            print("\nDone ✓")

def dir_image_meta_ext_window():


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
            except:
                pass
            else:
                print(f'\nExtracting Exif data : {files}                                     ', end='')
                sys.stdout.flush()
                exifdata = image.getexif()
                for tag_id in exifdata:
                    # get the tag name, instead of human unreadable tag id
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    # decode bytes 
                    if isinstance(data, bytes):
                        try:
                            data = data.decode()
                        except:
                            pass
                    if os.path.exists(f"Exif_{files}.txt"):
                        tmp_file=open(f"Exif_{files}.txt", "a")
                        tmp_file.write(f"{tag:25}: {data}\n")
                        tmp_file.close()
                    else:
                        tmp_file=open(f"Exif_{files}.txt", "a")
                        tmp_file.write(f"{tag:25}: {data}\n")
                        tmp_file.close()

    print("\n\nDone ✓")
    exit(0)


def dir_image_meta_ext_other():

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
            except:
                pass
            else:
                print(f'\nExtracting Exif data : {files}                                     ', end='')
                sys.stdout.flush()
                exifdata = image.getexif()
                for tag_id in exifdata:
                    # get the tag name, instead of human unreadable tag id
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    # decode bytes 
                    if isinstance(data, bytes):
                        try:
                            data = data.decode()
                        except:
                            pass
                    if os.path.exists(f"Exif_{files}.txt"):
                        tmp_file=open(f"Exif_{files}.txt", "a")
                        tmp_file.write(f"{tag:25}: {data}\n")
                        tmp_file.close()
                    else:
                        tmp_file=open(f"Exif_{files}.txt", "a")
                        tmp_file.write(f"{tag:25}: {data}\n")
                        tmp_file.close()

    print("\n\nDone ✓")
    exit(0)
single_img_meta_ext()