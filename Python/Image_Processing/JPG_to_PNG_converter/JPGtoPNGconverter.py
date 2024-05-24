# create a jpg to png converter that is ran on the command line like this:

# python3 JPGtoPNGconverter.py [folder/] [new folder/]

# converts all the images in the first folder into png images and saves them in the second folder

import sys
import os
from PIL import Image

# grab first and second argument
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

# check if second folder exists and if not, create it
try:
    os.makedirs(png_folder)
except FileExistsError:
    pass

# loop through first folder, convert everything and save in the second folder
for filename in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{png_folder}{clean_name}.png', 'png')
    print(f'Image {filename} converted successfully!')
