#!/usr/bin/env python3

## Toolname : pic-tool
## Git-Repo URL : https://github.com/ASHWIN990/pic-tool.git
## Name : Ashwini Sahu
## Date : 03/May/2020

import argparse
import os
import sys
from PIL import Image

## COLOR ##

black_col="\u001b[30;1m"
red_col="\u001b[31;1m"
green_col="\u001b[32;1m"
yellow_col="\u001b[33;1m"
blue_col="\u001b[34;1m"
magenta_col="\u001b[35;1m"
cyan_col="\u001b[36;1m"
white_col="\u001b[37;1m"
reset_col="\u001b[0m"

## BANNER ##

def banner():
    print(f"""{red_col}
        __                   __                 __   
______ |__| ____           _/  |_  ____   ____ |  |  
\____ \|  |/ ___\   ______ \   __\/  _ \ /  _ \|  |  
|  |_> >  \  \___  /_____/  |  | (  <_> |  <_> )  |__
|   __/|__|\___  >          |__|  \____/ \____/|____/  BY : {blue_col}ASHWINI SAHU{red_col}
|__|           \/                                    
    {reset_col}""")

## MAIN FUNCTION ##

def main():
    parser = argparse.ArgumentParser(description=f"Image Metadata Remover, Writeen by : {blue_col}ASHWINI SAHU{reset_col}, GITHUB : https:github.com/ASHWIN990/pic-tool.git")
    parser.add_argument("-s", "--single", action='store_true', default=False, help="Enables Single image mode.",)
    parser.add_argument("-d", "--dir", action='store_true', default=False, help="Enables Directory image mode.",)
    parser.add_argument("--img", metavar="PATH", required=True, type=str, help="Provide the path of Image for Single mode or path of Dir for Dir mode.")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        exit(0)

    if args.single == True and args.dir == True:
        print("Both the single and dir mode flag is passed, give any one")
        exit(0)

    if args.single == False and args.dir == False:
        print("No flag for single or dir mode is passed, give any one")
        exit(0)

    if len(args.img) == 0:
        print("Provide the path of Image for Single mode or path of Dir for Dir mode")
        exit(0)

    if args.single == True and args.dir == False:
        sin_mode=True
        if os.path.isfile(args.img):
            single_img_meta_rem(args)
        else:
            print(f"Path {args.img} : is invalid")

    if args.dir == True and args.single == False:
        dir_mode=True
        if os.path.isdir(args.img):
            dir_image_meta_rem_changer(args)
        else:
            print(f"Path {args.img} : is invalid")

def single_img_meta_rem(args):

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=int(args.img)
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    print(f"Format of image is : {image.format}")
    print(f"Width : {image.size[0]}      Height : {image.size[1]}") ## Size of original image
    try:
        image.save(f'No_Exif_{img_basename}')
    except:
        pass
    else:
        pass
    print("Done ✓")

def dir_image_meta_rem_changer(args):
    
    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\
    
    img_dir_path=str(args.img)
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("Directory is empty")        
        exit(0)
    print("\n")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}/{files}"):
            try:
                image = Image.open(f"{img_dir_path}/{files}")
                print(f'\rRemoving Metadata : {files}                                     ', end='')
                sys.stdout.flush()
                image.save(f'No_Exif_{files}')
            except:
                pass
            else:
                pass

    print("\nDone ✓")
    exit(0)

if __name__ == "__main__":
    banner()
    main()