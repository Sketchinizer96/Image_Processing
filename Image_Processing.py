# Documentation : https://pillow.readthedocs.io/en/stable
from sys import path
from typing import Optional, Any
import time
from PIL import Image, ImageFilter, ImageEnhance
import os
from os import path
import re
from PIL.ImageEnhance import Color


def convert_format(format):
    img_a = Image.open(format)
    print('Please specify the filter mode for conversion :')
    print(f'1:Blur \t 2:Detail \t 3:Emboss \t 4:Sharpen ')
    input_data = input(f'Please enter the number:\t')
    if input_data == '1':
        filter_img = img_a.filter(ImageFilter.BLUR)  # converts the images to greyscale
    elif input_data == '2':
        filter_img = img_a.filter(ImageFilter.DETAIL)
    elif input_data == '3':
        filter_img = img_a.filter(ImageFilter.EMBOSS)
    elif input_data == '4':
        filter_img = img_a.filter(ImageFilter.SHARPEN)
    else:
        print('No inputs provided')

    print('do you want to save the image')
    i = str(input(f'Enter yes /No:'))
    if i == 'Yes':
        print('Please enter the path to save the file ')
        file_location = input(f'File location: \t')
        print('please enter the name of the file to be converted')
        image_name = input('New Image Name : ')
        image_save_path = (f'{file_location}'f'\\{image_name}')
        filter_img.save(fr'{image_save_path}')
        print('Image Saved Successfully')
    return filter_img


def create_thumbnail(thumbnail):
    image_5 = Image.open(thumbnail)
    img1 = image_5.resize((200, 200))
    print('do you want to save the image')
    x = str(input(f'Enter yes /No:'))
    if x == 'Yes':
        print('Please enter the path to save the file ')
        file_location = input(f'File location: \t')
        print('please enter the name of the file to be converted')
        image_name = input('New Image Name : ')
        image_save_path = (f'{file_location}'f'\\{image_name}')
        img1.save(fr'{image_save_path}')
        print('Image Saved Successfully')
        display = str(input('Do you want to view :'))
        if display == 'Yes':
            img1.show()
    return img1


def convert_mode(mode):
    img_a = Image.open(mode)
    print('Please specify the color mode for conversion :')
    print(f'1:Black and white \t 2:RGBA \t 3:1-bit pixels, black and white ')
    input_data = input(f'Please enter the number:\t')
    if input_data == '1':
        image_convert = img_a.convert('L')  # converts the images to greyscale
    elif input_data == '2':
        image_convert = img_a.convert('RGBA')
    elif input_data == '3':
        image_convert = img_a.convert('1')
    else:
        print('No inputs provided')

    print('do you want to save the image')
    i = str(input(f'Enter yes /No:'))
    if i == 'Yes':
        print('Please enter the path to save the file ')
        file_location = input(f'File location: \t')
        print('please enter the name of the file to be converted')
        image_name = input('New Image Name : ')
        image_save_path = (f'{file_location}'f'\\{image_name}')
        image_convert.save(fr'{image_save_path}')
        print('Image Saved Successfully')
    return image_convert


def image_enhance(enhance):
    img_a = Image.open(enhance)
    print('Please specify the Enhance Mode for conversion :')
    print(f'1:Color \t 2:Contrast  \t 3:Brightness \t 4:Sharpeness ')
    input_data = input(f'Please enter the number:\t')
    if input_data == '1':
        enhanced_img = ImageEnhance.Color(img_a)
        print('Enter the Enhancement factor between 0.0 to 5.0')
        en_input = float(input(f"Enhancement Factor:\t"))
        enhanced_img = enhanced_img.enhance(en_input)
        display = str(input('Do you want to view :'))
        if display == 'Yes':
            enhanced_img.show()
        else:
            pass
    elif input_data == '2':
        enhanced_img = ImageEnhance.Contrast(img_a)
        print('Enter the Contrast factor between 0.0 to 5.0')
        en_input = float(input(f"Contrast Factor:\t"))
        enhanced_img = enhanced_img.enhance(en_input)
        display = str(input('Do you want to view :'))
        if display == 'Yes':
            enhanced_img.show()
        else:
            pass
    elif input_data == '3':
        enhanced_img = ImageEnhance.Brightness(img_a)
        print('Enter the Brightness factor between 0.0 to 5.0')
        en_input = float(input(f"Brightness Factor:\t"))
        enhanced_img = enhanced_img.enhance(en_input)
        display = str(input('Do you want to view :'))
        if display == 'Yes':
            enhanced_img.show()
        else:
            pass
    elif input_data == '4':
        enhanced_img = ImageEnhance.Sharpness(img_a)
        print('Enter the Sharpness factor between 0.0 to 5.0')
        en_input = float(input(f"Sharpness Factor:\t"))
        enhanced_img = enhanced_img.enhance(en_input)
        display = str(input('Do you want to view :'))
        if display == 'Yes':
            enhanced_img.show()
        else:
            pass
    else:
        print('No inputs provided')
    print('do you want to save the image')
    i = str(input(f'Enter Yes /No:'))
    if i == 'Yes':
        print('Please enter the path to save the file ')
        file_location = input(f'File location: \t')
        print('please enter name of the file to be converted')
        image_name = input('New Image Name : ')
        image_save_path = (f'{file_location}'f'\\{image_name}')
        enhanced_img.save(fr'{image_save_path}')
        print('Image Saved Successfully')
    else:
        print('Exiting without Saving')
    return enhanced_img


print("*" * 10 + " Image Processing in Python " + "*" * 10)
print("-" * 100)
y = 0
while y != 1:
    print('Please mention the complete path of the image to fetch the file ')
    ip_path = input(f'Path:\t')
    pattern = re.compile('^[A-Z][:]{1}\\\(.*)')
    match = pattern.match(ip_path)
    if match:
        y = 1
    else:
        print('Please enter the correct path')
        time.sleep(3)
k = 0
while k != 1:
    file_name = input(f'Please enter the File Name to be opened:\t')
    image_path = fr'{ip_path}'f'\\{file_name}'
    img_exist = path.exists(fr'{image_path}')
    if img_exist:
        k = 1
    else:
        print('Entered file doesnot exist. Please check and try again')
        time.sleep(3)
exit_id: str = 'No'
while 'Yes' != exit_id:
    print("-" * 100)
    print("*" * 10 + " Image Processing Operations " + "*" * 10)
    print(
        f'1 : Create Thumbnail \n 2 : Convert Image mode \n 3 : Image Enhancement \n 4 : Convert Image Format \n 5 : Image Compression  ')
    print("-" * 100)
    data_input = input(f'Please enter the Choice : \t')
    if data_input == '1':
        create_thumbnail(image_path)
    elif data_input == '2':
        convert_mode(image_path)
    elif data_input == '3':
        image_enhance(image_path)
    elif data_input == '4':
        convert_format(image_path)
    elif data_input == '5':
        image_1 = Image.open(image_path)
        byte_size = os.path.getsize(image_path)
        img = tuple(image_1.size)
        print(fr'The Size of the image(X,Y) is' + str(image_1.size) + 'px and byte size is ' + str(
            byte_size / 1024) + 'Kb')
        input_data = input(f'Do you want to reduce the size (Yes/No):\t')
        if input_data == 'Yes':
            while l != 1:
                basewidth = int(input("Enter base width value between [100-500]: "))
                if 100 <= basewidth >= 500:
                    l = 1
                else:
                    print('Please enter the basewidth in the range specified:')
                    wpercent = (basewidth / float(image_1.size[0]))
                    hsize = int((float(image_1.size[1]) * float(wpercent)))
                    resize_img = image_1.resize((basewidth, hsize))
                    print('do you want to save the image')
                i = str(input(f'Enter Yes /No:'))
                if i == 'Yes':
                    print('Please enter the path to save the file ')
                    file_location = input(f'File location: \t')
                    print('please enter the name of the file to be converted with extension')
                    image_name = input('New Image Name : ')
                    quality = input('Please enter the Quality : ')
                    image_save_path = (f'{file_location}'f'\\{image_name}')
                    resize_img.save(fr'{image_save_path}', optimize=True, quality={quality})
                    print('Image Saved Successfully')
                    time.sleep(5)
                else:
                    print('Exiting without Saving')
                    print(f'New Image Size in Bytes : ' + os.path.getsize(resize_img))

    exit_id = input('Do you want  to End this Chat (Yes/No):  ')
print(f'Image Processing is exiting........ ')
