from typing import Optional, Any
# Documentation : https://pillow.readthedocs.io/en/stable
from os import listdir
from PIL import Image, ImageFilter

# we add 'r' for converting the string into a raw string in windows
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
img = Image.open(r'C:\Users\A707272\Desktop\ppit_arct.png')
print(img)  # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=874x620 at 0x2F71BE0>
# for Properties of the image we do :
print('Properties of the image are : ')
img1 = img.size   # returns the size
print(f'Image size:' + str(img1)+'px')
img2 = img.format   # returns the type of the image [JPG,PNG,GIFF]
print(f'Image Format:' + str(img2))
img3 = img.mode   # returns the color mode[RBG,CYMK]
print(f'Image Mode :' + str(img3))
# for all the properties of the image do dir(img)

# for image filters we can use the filter command but PNG supports filter.
filter_img = img.filter(ImageFilter.BLUR)
filter_img.save(r"blur.png", 'png')

# to convert the file from one tone to another to another we can use the .convert
image_convert = img.convert('L')   # converts the images to greyscale
image_convert.save(r"black.png", 'png')
# image_convert.show() # Displays image on screen
# for more use cases please follow the following : https://dzone.com/articles/image-processing-in-python-with-pillow