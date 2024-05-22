from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')  # this is now an image object

print(img)
print(img.format)
print(img.size)
print(img.mode)
print()
# print(dir(img))

# apply a filter
filtered_img = img.filter(ImageFilter.BLUR)
# must be PNG because jpg isn't supported with the ImageFilter
filtered_img.save('blur.png', 'png')

# convert it to greyscale and save it
filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')

# rotate, resize, show
crooked = filtered_img.rotate(90)
resize = filtered_img.resize((300, 300))  # Takes a tuple
# resize.show()

# crop
cropped_img = img.crop((100, 100, 400, 400))
cropped_img.save('cropped.png', 'png')
# cropped_img.show()

# new image scaling and thumbnail
img = Image.open('./beach.jpg')
img.thumbnail((400,400))
img.show()

