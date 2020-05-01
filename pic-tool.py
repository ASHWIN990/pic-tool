#!/usr/bin/env python3

## Toolname : pic-tool
## Git-Repo URL : https://github.com/ASHWIN990/pic-tool.git
## Name : Ashwini Sahu 
## Date : 01/May/2020

import os
import sys
import platform
from time import sleep
from PIL import Image
from PIL.ExifTags import TAGS

## TRYING SOME COLORS ##

black_col="\u001b[30;1m"
red_col="\u001b[31;1m"
green_col="\u001b[32;1m"
yellow_col="\u001b[33;1m"
blue_col="\u001b[34;1m"
magenta_col="\u001b[35;1m"
cyan_col="\u001b[36;1m"
white_col="\u001b[37;1m"
reset_col="\u001b[0m"

## HELP SECTION ##

def pic_tool_help_other():
    print(f"""\
    {green_col}
         _         __            __
   ___  (_)_______/ /____  ___  / /
  / _ \/ / __/___/ __/ _ \/ _ \/ / 
 / .__/_/\__/    \__/\___/\___/_/  
/_/                                
{reset_col}
pic-tool is a image manipulation tool writeen in python by ASHWINI SAHU.

Usage: python3 pic-tool.py [OPTIONS...]

-dm, -d, --dir-mode         Define Directory mode.
-sm, -s, --sin-mode         Define Single image mode.      By Default
-nc,     --no-clear         Use this flag to stop the script from clearing the screen.
-na,     --no-art           Use this flag to not print the ASCII art.
-h,      --help             Use this flag to see the help section.

You can pass multiple flags at same time like :- python3 pic-tool.py -na -nc

----------------------------------------------------------------------------------------

This tool can do many things like :-
                                        * Resize the image
                                        * Compress the image
                                        * Convert image to thubmnail
                                        * Change the image format
                                        * Rotate the image
                                        * Greyscale the image 
                                        * Remove the image Metadata
                                        * MORE TO BE ADDED
        """)

def pic_tool_help_win():
    print(f"""\
         _         __            __
   ___  (_)_______/ /____  ___  / /
  / _ \/ / __/___/ __/ _ \/ _ \/ / 
 / .__/_/\__/    \__/\___/\___/_/  
/_/                                

pic-tool is a image manipulation tool writeen in python by ASHWINI SAHU.

Usage: python3 pic-tool.py [OPTIONS...]

-dm, -d, --dir-mode         Define Directory mode.
-sm, -s, --sin-mode         Define Single image mode.      By Default
-nc,     --no-clear         Use this flag to stop the script from clearing the screen.
-na,     --no-art           Use this flag to not print the ASCII art.
-h,      --help             Use this flag to see the help section.

You can pass multiple flags at same time like :- python3 pic-tool.py -na -nc

Note: While giving the path to the image or folder give paths as :-

    Example : F:\\\\Wallpaper\\\\Nature\\\\Forest.jpg      With double \\\\

----------------------------------------------------------------------------------------

This tool can do many things like :-
                                        * Resize the image
                                        * Compress the image
                                        * Convert image to thubmnail
                                        * Change the image format
                                        * Rotate the image
                                        * Greyscale the image 
                                        * Remove the image Metadata
                                        * MORE TO BE ADDED
        """)

## HELP DOCUMENTATION FUNCTION ##

def pic_tool_help():
    if os.name == 'nt':
        pic_tool_help_win()
    else:
        pic_tool_help_other()

for args in sys.argv:
    if args == "-h" or args == "--h" or args == "-help" or args =="--help": ## CHECKING IF YOU WANT TO HELP OR NOT ##
        pic_tool_help()
        exit()

## CHECKING THE COMMAND LINE ARGVS ##

do_clear=True
want_art=True
dir_mode=False
sin_mode=False
sin_mode_argv=False
dir_mode_argv=False

for args in sys.argv:
    if args == "--dir-mode" or args == "-dm" or args == "-d": ## CHECKING IF YOU WANT THE DIRECTORY MODE BY DEFAULT ##
        dir_mode=True
        dir_mode_argv=True

for args in sys.argv:
    if args == "--sin-mode" or args == "-sm" or args == "-s": ## CHECKING IF YOU WANT THE SINGLE MODE BY DEFAULT ##
        sin_mode=True
        sin_mode_argv=True

if sin_mode == True and dir_mode == True:
    dir_mode = True
    sin_mode = False

if sin_mode == False and dir_mode == False:
    sin_mode = True

## NOTE : IF YOU PROVIDE BOTH SINLE AND DIRECTORY MODE FLAG IT WILL TAKE DIRECTORY MODE AS PRIORITY ##

for args in sys.argv:
    if args == "--no-clear" or args == "-nc": ## CHECKING IF YOU WANT TO CLEAR THE SCREEN OR NOT ##
        do_clear=False

for args in sys.argv:
    if args == "--no-art" or args == "-na": ## CHECKING IF YOU WANT THE ASCII ART OR NOT ##
        want_art=False

## FUNCTION TO CLEAR THE SCREEN ##

def clear_scr():
    if do_clear == True:
        do_clear_scr()
    elif do_clear == False:
        pass

def do_clear_scr():
    if do_clear != False:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

## BANNER FUNCTION ##

def banner():
    if want_art == True:
        if os.name == 'nt':
            if do_clear == False:
                banner_print_no_color()
            else:
                banner_print_color()
        else:
            banner_print_color()
    elif want_art == False:
        pass

def banner_print_color():

        print(f"""\

        {green_col} ________________________
        {green_col}|.----------------------.|
        {green_col}||                      ||
        {green_col}||       ______         ||
        {green_col}||     .;;;;;;;;.       ||
        {green_col}||    /;;;;;;;;;;;\     ||
        {green_col}||   /;/`    `-;;;;; . .||{yellow_col}                 __                     __                          __ 
        {green_col}||   |;|__  __  \;;;|   ||{yellow_col}                /  |                   /  |                        /  |
        {green_col}||.-.|;| e`/e`  |;;;|   ||{yellow_col}        ______  $$/   _______         _$$ |_     ______    ______  $$ |
        {green_col}||   |;|  |     |;;;|'--||{yellow_col}       /      \ /  | /       |______ / $$   |   /      \  /      \ $$ |
        {green_col}||   |;|  '-    |;;;|   ||{yellow_col}      /$$$$$$  |$$ |/$$$$$$$//      |$$$$$$/   /$$$$$$  |/$$$$$$  |$$ |
        {green_col}||   |;;\ --'  /|;;;|   ||{yellow_col}      $$ |  $$ |$$ |$$ |     $$$$$$/   $$ | __ $$ |  $$ |$$ |  $$ |$$ |
        {green_col}||   |;;;;;---'\|;;;|   ||{yellow_col}      $$ |__$$ |$$ |$$ \_____          $$ |/  |$$ \__$$ |$$ \__$$ |$$ |
        {green_col}||   |;;;;|     |;;;|   ||{yellow_col}      $$    $$/ $$ |$$       |         $$  $$/ $$    $$/ $$    $$/ $$ |
        {green_col}||   |;;.-'     |;;;|   ||{yellow_col}      $$$$$$$/  $$/  $$$$$$$/           $$$$/   $$$$$$/   $$$$$$/  $$/ 
        {green_col}||'--|/`        |;;;|--.||{yellow_col}      $$ |                                                             
        {green_col}||;;;;    .     ;;;;.\;;||{yellow_col}      $$ |                                                             
        {green_col}||;;;;;-.;_    /.-;;;;;;||{yellow_col}      $$/                                            {red_col}GitHub {blue_col}: {yellow_col}ASHWIN990
        {green_col}||;;;;;;;;;;;;;;;;;;;;;;||
        {green_col}||{red_col}A{yellow_col}S{blue_col}H{green_col};;;;;;;;;;;;;;;;;;;||
        {green_col}'------------------------'{reset_col}

                        """)

def banner_print_no_color():

        print(f"""\

         ________________________
        |.----------------------.|
        ||                      ||
        ||       ______         ||
        ||     .;;;;;;;;.       ||
        ||    /;;;;;;;;;;;\     ||
        ||   /;/`    `-;;;;; . .||                 __                     __                          __ 
        ||   |;|__  __  \;;;|   ||                /  |                   /  |                        /  |
        ||.-.|;| e`/e`  |;;;|   ||        ______  $$/   _______         _$$ |_     ______    ______  $$ |
        ||   |;|  |     |;;;|'--||       /      \ /  | /       |______ / $$   |   /      \  /      \ $$ |
        ||   |;|  '-    |;;;|   ||      /$$$$$$  |$$ |/$$$$$$$//      |$$$$$$/   /$$$$$$  |/$$$$$$  |$$ |
        ||   |;;\ --'  /|;;;|   ||      $$ |  $$ |$$ |$$ |     $$$$$$/   $$ | __ $$ |  $$ |$$ |  $$ |$$ |
        ||   |;;;;;---'\|;;;|   ||      $$ |__$$ |$$ |$$ \_____          $$ |/  |$$ \__$$ |$$ \__$$ |$$ |
        ||   |;;;;|     |;;;|   ||      $$    $$/ $$ |$$       |         $$  $$/ $$    $$/ $$    $$/ $$ |
        ||   |;;.-'     |;;;|   ||      $$$$$$$/  $$/  $$$$$$$/           $$$$/   $$$$$$/   $$$$$$/  $$/ 
        ||'--|/`        |;;;|--.||      $$ |                                                             
        ||;;;;    .     ;;;;.\;;||      $$ |                                                             
        ||;;;;;-.;_    /.-;;;;;;||      $$/                                            GitHub : ASHWIN990
        ||;;;;;;;;;;;;;;;;;;;;;;||
        ||ASH;;;;;;;;;;;;;;;;;;;||
        '------------------------'

                        """)

clear_scr() ## CLEARING THE SCREEN
banner() ## PRINTING THE BANNER

## CHECKING FOR THE MODE ##

if sin_mode == True:
    if sin_mode_argv == True:
        print("\n    Single Mode is active by user.\n")
    elif sin_mode_argv == False:
        print("\n    Single Mode is active by default.\n")

if dir_mode == True:
    print("\n    Directory Mode is active by user\n")


### MAIN MENU STARTS HERE ###

def menu_list():
    if os.name == 'nt':
        if do_clear == False:
            menu_list_no_color()
        else:
            menu_list_color()
    else:
        menu_list_color()

def menu_list_color():

    print(f"\n{yellow_col}    A Image manipulation tool written in {red_col}Python, {yellow_col}Enjoy{reset_col}")
    print (f'''
    {yellow_col}  [ {blue_col}1 {yellow_col}] {green_col}Resize Image.             {yellow_col}  [ {blue_col}5 {yellow_col}] {green_col}Rotate The Image.
    {yellow_col}  [ {blue_col}2 {yellow_col}] {green_col}Image Compressor.         {yellow_col}  [ {blue_col}6 {yellow_col}] {green_col}Grayscale The Image.
    {yellow_col}  [ {blue_col}3 {yellow_col}] {green_col}Image Thumbnail Maker.    {yellow_col}  [ {blue_col}7 {yellow_col}] {green_col}Image Metadata Remover.
    {yellow_col}  [ {blue_col}4 {yellow_col}] {green_col}Image Format Changer.

    {yellow_col}  [ {blue_col}x {yellow_col}] {green_col}Exit. {reset_col}''')


def menu_list_no_color():

    print(f"\n    A Image manipulation tool written in Python, Enjoy")
    print (f'''
      [ 1 ] Resize Image.               [ 5 ] Rotate The Image.
      [ 2 ] Image Compressor.           [ 6 ] Grayscale The Image.
      [ 3 ] Image Thumbnail Maker.      [ 7 ] Image Metadata Remover.
      [ 4 ] Image Format Changer.

      [ x ] Exit. ''')


total_option=["1", "2", "3", "4", "5", "6", "7", "x", "X"] ## Creating the list of all options

def option_taker():
    user_opt = input(f"\n   Enter the option here $ ")
    if user_opt == "":
        clear_scr()
        banner()
        menu_list()
        print(f"\n   Enter the right option")
        option_taker()
    else:
        if user_opt in total_option:
            option_launcher(user_opt)
        else:
            clear_scr()
            banner()
            menu_list()
            print(f"\n   Enter the right option")
            option_taker()


###

            #######################    MAIN CODE IS HERE     #######################


###

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




################################################ 1. IMAGE RESIZE ####################################################################################


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
    exit(0)


def dir_image_resize_window():


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
                print(f'\rResizing image : {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                resized_image = image.resize((image_width, image_height))
                resized_image.save(f'resized_{files}')
    print("\n\nDone ✓")
    exit(0)

def dir_image_resize_other():

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
                print(f'\rResizing image : {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                pass
                resized_image = image.resize((image_width, image_height))
                resized_image.save(f'resized_{files}')
    print("\n\nDone ✓")
    exit(0)

def image_resize():
    if sin_mode == True:
        single_img_resize()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_resize_window()
        else:
            dir_image_resize_other()




################################################ 2. IMAGE COMPRESS ####################################################################################


def single_img_compress():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("\nEnter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("\nImage not found")
        exit()
    compr_rat=input("\nEnter the Compress Ratio (ex: 50) : ")
    compr_rat_tmp = compr_rat.isnumeric()
    if compr_rat_tmp == True:
        compr_rat=int(compr_rat)
    else:
        print("\nCompress Ratio must be number.\n")
        exit(0)
    img_basename=os.path.basename(img_path)
    image = Image.open(img_path)
    print(f"\nFormat of image is : {image.format}")
    print(f"\nCompression Ration of image is : {compr_rat}")
    image.save(f'compressed_{img_basename}', quality=compr_rat)
    print("\nDone ✓")

def dir_image_compress_window():


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
    compr_rat=input("\nEnter the Compress Ratio (ex: 50) : ")
    compr_rat_tmp = compr_rat.isnumeric()
    if compr_rat_tmp == True:
        compr_rat=int(compr_rat)
    else:
        print("\nCompress Ratio must be number.\n")
        exit(0)
    print("\n")
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
    print("\n\nDone ✓")
    exit(0)


def dir_image_compress_other():

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("\nDirectory is empty")        
        exit(0)
    compr_rat=input("\nEnter the Compress Ratio (ex: 50) : ")
    compr_rat_tmp = compr_rat.isnumeric()
    if compr_rat_tmp == True:
        compr_rat=int(compr_rat)
    else:
        print("\nCompress Ratio must be number.\n")
        exit(0)
    print("\n")
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
    print("\n\nDone ✓")
    exit(0)

def image_compress():
    if sin_mode == True:
        single_img_compress()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_compress_window()
        else:
            dir_image_compress_other()




################################################ 3. IMAGE THUMBNAIL MAKER ####################################################################################


def single_img_thumbnailer():

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

def image_thumbnailer():
    if sin_mode == True:
        single_img_thumbnailer()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_thumbnailer_window()
        else:
            dir_image_thumbnailer_other()




################################################ 4. IMAGE FORMAT CHANGER ####################################################################################


def single_img_ext_changer():

    # Note: For Windows while giving the path to the image or folder give paths as :-
    # Example : F:\\Wallpaper\\Nature\\Forest.jpg      With double \\

    img_path=input("\nEnter the path of the image : ")
    if os.path.isfile(img_path) != True:
        print("\nImage not found")
        exit()
    new_ext=input("\nEnter the new Extension (ex: png) : ")
    img_basename=os.path.basename(img_path)
    img_name=os.path.splitext(img_basename)[0]
    image = Image.open(img_path)
    print(f"\nFormat of image is : {image.format}")
    print(f"\nWidth : {image.size[0]}      Height : {image.size[1]}") ## Size of original image
    try:
        image.save(f'{img_name}.{new_ext}')
        img_name=os.path.splitext(files)[0]
        image.save(f'{img_name}.{new_ext}')
    except:
        pass
    else:
        pass
    print("\nDone ✓")

def dir_image_ext_changer_window():


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
    new_ext=input("\nEnter the new Extension (ex: png) : ")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}\\\\{files}"):
            try:
                image = Image.open(f"{img_dir_path}\\\\{files}")
                print(f'\rChanging Extension : {files}                                     ', end='')
                sys.stdout.flush()
                img_name=os.path.splitext(files)[0]
                image.save(f'{img_name}.{new_ext}')
            except:
                pass
            else:
                pass

    print("\n\nDone ✓")
    exit(0)


def dir_image_ext_changer_other():

    img_dir_path=input("\nEnter the path of the image directory : ")
    if os.path.isdir(img_dir_path) != True:
        print("\nDirectory not found")
        exit()
    list_of_files = os.listdir(img_dir_path)
    if len(list_of_files) == 0:
        print("\nDirectory is empty")        
        exit(0)
    print("\n")
    new_ext=input("Enter the new Extension (ex: png) : ")
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}/{files}"):
            try:
                image = Image.open(f"{img_dir_path}/{files}")
                print(f'\rChanging Extension : {files}                                     ', end='')
                sys.stdout.flush()
                img_name=os.path.splitext(files)[0]
                image.save(f'{img_name}.{new_ext}')
            except:
                pass
            else:
                pass

    print("\n\nDone ✓")
    exit(0)

def image_ext_changer():
    if sin_mode == True:
        single_img_ext_changer()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_ext_changer_window()
        else:
            dir_image_ext_changer_other()




################################################ 5. ROTATE THE IMAGE ####################################################################################


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

def image_rotator():
    if sin_mode == True:
        single_img_rotate()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_rotate_window()
        else:
            dir_image_rotate_other()




################################################ 6. ROTATE THE IMAGE ####################################################################################


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

def image_greyscale():
    if sin_mode == True:
        single_img_greyscale()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_greyscale_window()
        else:
            dir_image_greyscale_other()




################################################ 7. Image Metadata Remover ####################################################################################




def single_img_meta_rem():

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
    try:
        image.save(f'No_Exif_{img_basename}')
    except:
        pass
    else:
        pass
    print("\nDone ✓")

def dir_image_meta_rem_window():


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
                print(f'\rRemoving Metadata : {files}                                     ', end='')
                sys.stdout.flush()
                image.save(f'No_Exif_{files}')
            except:
                pass
            else:
                pass

    print("\n\nDone ✓")
    exit(0)


def dir_image_meta_rem_other():

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
                print(f'\rRemoving Metadata : {files}                                     ', end='')
                sys.stdout.flush()
                image.save(f'No_Exif_{files}')
            except:
                pass
            else:
                pass

    print("\n\nDone ✓")
    exit(0)

def image_meta_rem():
    if sin_mode == True:
        single_img_meta_rem()
    elif dir_mode == True:
        if os.name == 'nt':
            dir_image_meta_rem_window()
        else:
            dir_image_meta_rem_other()




################################################################## END OF THE SCRIPT ####################################################################################

## Function For Checking The Given Option

def option_launcher(opt):

    if opt == "1":
        image_resize()
    elif opt == "2":
        image_compress()
    elif opt == "3":
        image_thumbnailer()
    elif opt == "4":
        image_ext_changer()
    elif opt == "5":
        image_rotator()
    elif opt == "6":
        image_greyscale()
    elif opt == "7":
        image_meta_rem()
    elif opt == "8":
        pass
    elif opt == "x" or opt == "X":
        print(f"\n   Exiting the tool Bye !!")
        exit()

menu_list() ## CALLING THE MENU LIST ##
option_taker() ## CALLING THE OPTION TAKER FUNCTION ##
 
                                                          ########### END HERE ###########