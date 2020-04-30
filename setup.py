#!/usr/bin/env python3

import os
import platform
from pip._internal.utils.misc import get_installed_distributions
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

## FUNTION FOR CHECKING THE OS ##

if platform.system() == 'Linux':
    print("Platform is Linux")
    platform_current="Linux"
elif platform.system() == 'Windows':
    print("Platform is Windows")
    platform_current="Windows"
elif platform.system() == 'Darwin':
    print("Platform is macOS")
    platform_current="macOS"
else:
    print("Taking Platorm as Linux Cause Cant Determine the Platform")
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
        {green_col}'------------------------'{reset_col}

                        """)

def req_pak():
    required_pkg=["Pillow", "progress"]
    return required_pkg

def chk_installed_pkg():
    installed_packages = [package.project_name for package in get_installed_distributions()]
    return installed_packages

def install_pkg_windows():
    for pkg in required_pkg:
        if pkg in installed_packages:
            print(f"{pkg} requirement satisfied\n")
        else:
            print(f"installing the package {pkg}\n")
            os.system(f"pip install {pkg}")

def install_pkg_linux():
    for pkg in required_pkg:
        if pkg in installed_packages:
            print(f"{pkg} requirement satisfied\n")
        else:
            print(f"installing the package {pkg}\n")
            os.system(f"pip install {pkg}")

def install_pkg_macOS():
    print(f"{yellow_col}The platform is {red_col}{platform_current} {yellow_col}and i suggest to install the packages by yourself and then run the script.\n")
    print(f"\nRequired packages are :- {green_col}")
    for pkg in required_pkg:
        print(f"\t\t{pkg}")
    print(f"{reset_col}")
    os._exit(0)

def install_pkg_other():
    print(f"{yellow_col}The platform is {red_col}{platform_current} {yellow_col}and i suggest to install the packages by yourself and then run the script.\n")
    print(f"\nRequired packages are :- {green_col}")
    for pkg in required_pkg:
        print(f"\t\t{pkg}")
    print(f"{reset_col}")
    os._exit(0)

clear_scr() ## CLEARING THE SCREEN
banner() ## PRINTING THE BANNER
required_pkg=req_pak() ## MAKKING A LIST OF INSTALLED PACKAGES
installed_packages=chk_installed_pkg() ## MAKING A LIST OF INSTALLED PACKAGES

print(f"{yellow_col}Thanks for installing the pic-tool {red_col}❤{reset_col}\n")
print(f"The current platform is {green_col}{platform_current} {reset_col}and release is {green_col}{platform.release()}{reset_col}")
print(f"\n{green_col}Checking if the required packages are installed or not if not installing them !!{reset_col}\n")

## INSTALLING THE REQUIRED PAKAGES ##

if platform_current == "Windows":
    install_pkg_windows() ## Using the Windows installer
elif platform_current == "Linux":
    install_pkg_linux() ## Using the Linux installer
elif platform_current == "macOS":
    install_pkg_macOS() ## Using the macOS installer 
else:
    install_pkg_other() ## Using the other installer

print(f"\n{yellow_col}Thanks for installation of pic-tool is succesfull{reset_col}\n")

## DONE INSTALLING 