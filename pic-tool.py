#!/usr/bin/env python3

import os
import sys
import platform
from time import sleep

## TRYING SOME COLORS ##

black_col="\u001b[30m"
red_col="\u001b[31m"
green_col="\u001b[32m"
yellow_col="\u001b[33m"
blue_col="\u001b[34m"
magenta_col="\u001b[35m"
cyan_col="\u001b[36m"
white_col="\u001b[37m"
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

-nc, --no-clear         Use this flag to stop the script from clearing the screen.
-na, --no-art           Use this flag to not print the ASCII art.
-h,  --help             Use this flag to see the help section.

You can pass multiple flags at same time like :- python3 pic-tool.py -na -nc

----------------------------------------------------------------------------------------

This tool can do many things like :-
                                        * Resize the image
                                        * Compress the image
                                        * Convert image to thubmnail
                                        * Change the image format
                                        * Rotate the image
                                        * Greyscale the image 
                                        * Extract the image Metadata
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

-nc, --no-clear         Use this flag to stop the script from clearing the screen.
-na, --no-art           Use this flag to not print the ASCII art.
-h,  --help             Use this flag to see the help section.

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
                                        * Extract the image Metadata
                                        * Remove the image Metadata
                                        * MORE TO BE ADDED
        """)

def pic_tool_help():
    if os.name == 'nt':
        pic_tool_help_win()
    else:
        pic_tool_help_other()

## CHECKING THE COMMAND LINE ARGVS ##

do_clear=True
want_art=True

for args in sys.argv:
    if args == "-h" or args == "--h" or args == "-help" or args =="--help":
        pic_tool_help()
        exit()

## Bug in color in windows ##
for args in sys.argv:
    if args == "--no-clear" or args == "-nc":
        do_clear=False

for args in sys.argv:
    if args == "--no-art" or args == "-na":
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
    {yellow_col}  [ {blue_col}3 {yellow_col}] {green_col}Image Thumbnail Maker.    {yellow_col}  [ {blue_col}7 {yellow_col}] {green_col}Image Metadata Extractor.
    {yellow_col}  [ {blue_col}4 {yellow_col}] {green_col}Image Format Changer.     {yellow_col}  [ {blue_col}8 {yellow_col}] {green_col}Image Metadata Remover.

    {yellow_col}  [ {blue_col}x {yellow_col}] {green_col}Exit. {reset_col}''')


def menu_list_no_color():

    print(f"\n    A Image manipulation tool written in Python, Enjoy")
    print (f'''
      [ 1 ] Resize Image.               [ 5 ] Rotate The Image.
      [ 2 ] Image Compressor.           [ 6 ] Grayscale The Image.
      [ 3 ] Image Thumbnail Maker.      [ 7 ] Image Metadata Extractor.
      [ 4 ] Image Format Changer.       [ 8 ] Image Metadata Remover.

      [ x ] Exit. ''')


total_option=["1", "2", "3", "4", "5", "6", "x", "X"] ## Creating the list of all options

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




###



def option_launcher(opt):

    if opt == "1":
        print("1")
    elif opt == "2":
        pass
    elif opt == "3":
        pass
    elif opt == "4":
        pass
    elif opt == "5":
        pass
    elif opt == "6":
        pass
    elif opt == "x" or opt == "X":
        print(f"\n   Exiting the tool Bye !!")
        exit()

menu_list()
option_taker()
