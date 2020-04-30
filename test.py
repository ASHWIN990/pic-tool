import os
import sys
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
    image_width=image_width_take()
    image_height=image_height_take()
    for files in list_of_files:
        if os.path.isfile(f"{img_dir_path}\\\\{files}"):
            try:
                image = Image.open(f"{img_dir_path}\\\\{files}")
                print(f'\rResizing image  {files}                                     ', end='')
                sys.stdout.flush()
            except:
                pass
            else:
                resized_image = image.resize((image_width, image_height))
                resized_image.save(f'resized_{files}')

dir_image_resize_window()
