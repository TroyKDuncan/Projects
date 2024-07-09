from PIL import Image
import sys
import os

# img = Image.open('./Logos/Hazing_SS.png')

# cropped_img = img.crop((785,1620,3060,2190))
# cropped_img.save('Cropped/cropped_H_SS.png', 'PNG')


def check_if_done():
    while True:
        choice = input("Done cropping? y/n \n")
        if choice.lower() == 'y' or choice.lower() == 'n':
            return choice
        else:
            print('Invalid choice. Try again.\n')


def cropper(img) -> Image:
    while True:
        print(f'Working on {filename}')
        print('Enter values for the 4 corners:')
        left = int(input('Left side: '))
        top = int(input('Top side: '))
        right = int(input('Right side: '))
        bottom = int(input('Bottom side: '))
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(f'{cropped_folder}/cropped_{clean_name}.png', 'PNG')
        if check_if_done() == 'y':
            return cropped_img

def is_image(filename):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    return any(filename.lower().endswith(ext) for ext in valid_extensions)


# grab first and second argument
uncropped_folder = sys.argv[1]
cropped_folder = sys.argv[2]

# check if second folder exists and if not, create it
try:
    os.makedirs(cropped_folder)
except FileExistsError:
    pass


# loop through first folder, convert everything and save in the second folder
for filename in os.listdir(uncropped_folder):
    if is_image(filename):
        img = Image.open(f'{uncropped_folder}/{filename}')
        clean_name = os.path.splitext(filename)[0]
        cropped_img = cropper(img)
        print(f'Image {filename} converted successfully!')
