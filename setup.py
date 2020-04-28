#!/bin/usr/python3


# to add this to the /bin/usr for linux 
# and for windows to the path

import os
import platform
try:
    from time import sleep
    is_time_module_avb=True
except ImportError as e:
    is_time_module_avb=False

## TRYING SOME COLORS ##

black_col="\u001b[30m"
red_col="\u001b[31m"
green_col="\u001b[32m"
yellow_col="\u001b[33m"
blue_col="\u001b[34m"
magenta_col="\u001b[35m"
cyan_col="\u001b[36m"
white_col="\u001b[37m"

## FUNTION FOR CHECKING THE OS ##

if platform.system() == 'Linux':
    print("Platform is Linux")
    platform_current="Linux"
elif platform.system() == 'Windows':
    print("Platform is Windows")
    platform_current="Windows"
elif platform.system() == 'Darwin':
    print("Platform is Mac")
    platform_current="macOS"
else:
    print("Taking Platorm as Linux Cause Cant Determine the Platform")
    if is_time_module_avb == True:
        sleep(2)
    platform_current="Linux"

## FUNCTION TO CLEAR THE SCREEN ##

def clear_scr():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


## BANNER FUNCTION ##

def banner():
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
        {green_col}||;;;;;-.;_    /.-;;;;;;||{yellow_col}      $$/
        {green_col}||;;;;;;;;;;;;;;;;;;;;;;||
        {green_col}||{red_col}A{yellow_col}S{blue_col}H{green_col};;;;;;;;;;;;;;;;;;;||
        {green_col}'------------------------'{white_col}

                        """)

clear_scr() ## CLEARING THE SCREEN
banner() ## PRINTING THE BANNER

print("Thanks for installing the pic-tool ❤\n")

print(f"The current platform is {platform_current} and release is {platform.release()}")

print("\nChecking if the required packages are installed or not if not installing them !!")

