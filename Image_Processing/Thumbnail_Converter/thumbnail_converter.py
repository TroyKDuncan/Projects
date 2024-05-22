# create a jpg to png converter that is ran on the command line like this:

# python3 JPGtoPNGconverter.py [folder/] [new folder/]

# converts all the images in the first folder into png images and saves them in the second folder

import sys
import os
from PIL import Image

# grab first and second argument
path = sys.argv[1]
new_folder = sys.argv[2]

# check if second folder exists and if not, create it
try:
    os.makedirs(new_folder)
except FileExistsError:
    pass

# loop through first folder, converting everything to thumbnail PNGs and save in the second folder
for filename in os.listdir(path):
    img = Image.open(f'{path}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.thumbnail((400,400))
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print(f'Image {filename} converted successfully!')
