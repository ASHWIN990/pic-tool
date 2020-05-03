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

def banner_other():
    print(f"""{red_col}
        __                   __                 __   
______ |__| ____           _/  |_  ____   ____ |  |  
\____ \|  |/ ___\   ______ \   __\/  _ \ /  _ \|  |  
|  |_> >  \  \___  /_____/  |  | (  <_> |  <_> )  |__
|   __/|__|\___  >          |__|  \____/ \____/|____/  BY : {blue_col}ASHWINI SAHU{red_col}
|__|           \/                                    
    {reset_col}""")

def banner_win():
    print(f"""
        __                   __                 __   
______ |__| ____           _/  |_  ____   ____ |  |  
\____ \|  |/ ___\   ______ \   __\/  _ \ /  _ \|  |  
|  |_> >  \  \___  /_____/  |  | (  <_> |  <_> )  |__
|   __/|__|\___  >          |__|  \____/ \____/|____/  BY : ASHWINI SAHU
|__|           \/                                    
""")

def banner():
    if os.name == 'nt':
        banner_win()
    else:
        banner_other()

## MAIN FUNCTION ##

def main():

    if os.name == 'nt':
        parser = argparse.ArgumentParser(description=f"Image Greyscaler, Writeen by : ASHWINI SAHU, GITHUB : https:github.com/ASHWIN990/pic-tool.git")
    else:
        parser = argparse.ArgumentParser(description=f"Image Greyscaler, Writeen by : {blue_col}ASHWINI SAHU{reset_col}, GITHUB : https:github.com/ASHWIN990/pic-tool.git")

    parser.add_argument("-s", "--single", action='store_true', default=False, help="Enables Single image mode.",)
    parser.add_argument("-d", "--dir", action='store_true', default=False, help="Enables Directory image mode.",)
    parser.add_argument("--img", metavar="PATH", required=True, type=str, help="Provide the path of Image for Single mode or path of Dir for Dir mode")

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
            single_img_greyscale(args)
        else:
            print(f"Path {args.img} : is invalid")

    if args.dir == True and args.single == False:
        dir_mode=True
        if os.path.isdir(args.img):
            if os.name == 'nt':
                dir_image_greyscale_window(args)
            else:
                dir_image_greyscale_other(args)
        else:
            print(f"Path {args.img} : is invalid")

def single_img_greyscale(args):

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=str(args.img)
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    print(f"Format of image is : {image.format}")
    print(f"Width : {image.size[0]}      Height : {image.size[1]}") ## Size of original image
    greyscale_image = image.convert('L')
    greyscale_image.save(f'greyscaled_{img_basename}')
    print("Done ✓")
    exit(0)

def dir_image_greyscale_window(args):

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_dir_path=str(args.img)
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("Directory is empty")
        exit(0)
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
    print("\nDone ✓")
    exit(0)

def dir_image_greyscale_other(args):

    img_dir_path=str(args.img)
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("Directory is empty")        
        exit(0)
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
    print("\nDone ✓")
    exit(0)

if __name__ == "__main__":
    banner()
    main()