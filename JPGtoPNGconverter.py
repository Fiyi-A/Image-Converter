import sys
import os
import re #regular expressions

'''
TO RUN:
paste this in the terminal - $ python3 JPGtoPNGConverter Pokedex/ Convert/
'''

from PIL import Image # pillow library

# grab the folder names from terminal
original_folder = str(sys.argv[1])
convert_folder = str(sys.argv[2])

# define sytem paths
parent_dir = os.getcwd()
old_dir_path = os.path.join(parent_dir,original_folder) # path for the original folder with jpg pictures
new_dir_path = os.path.join(parent_dir,convert_folder) # path for the new folder with png pictures

# check if the /Convert folder exists
if os.path.isdir(new_dir_path):
    print()
else:
    # create a new folder with the parent path
    path = os.path.join(parent_dir, convert_folder)
    os.mkdir(path)

# loop through Pokedex
for filename in os.listdir(old_dir_path):

    if filename.endswith(".jpg"):
        '''
        # regular expresions to extract picture name by excluding .jpg
        pattern = re.compile(r"^[a-zA-Z0-9]*")
        # store file name from Pokedex without '.jpg' into the new_name variable
        new_name = pattern.findall(filename)
        '''
        # split string to return without .jpg
        new_name = filename.split(".jpg")
        # convert images to png
        img = Image.open(f'./Pokedex/{filename}')
        # save to the new folder
        img.save(f"./{convert_folder}/{new_name[0]}.png",'png')


