
#? for editing image we will use pillow liberary. and we have to install pilo liberary. its not a part of python standard liberary lets see
from PIL import Image, ImageEnhance,ImageFilter # Image,ImageEnhance,ImageFilter for bluring image. is a module of Pillow liberary
import os
#?Image module er ekti class ase Image class. ekhon seitir object banabo
# img1 = Image.open('dog1.jpg')
# img1.save('dog1.jpg') #? we can change our image formate
# img1.show() #for showing

#! image resize  - use thumbnail
# img1 = Image.open('dog1.jpg')
# max_size = (250,250)
# img1.thumbnail(max_size)
# img1.save('dog_resize.jpg')

#! many images change extention  - use endwith,splitext
for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        file_name,extention = os.path.splitext(item)
        img1.save(f"{file_name}.png")

#! Image sharpness
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Sharpness(img1) #?ImageEnhance is a module. and Sharpness is a class of ImageEnhance module
# enhancer.enhance(4).save('dog1_sharp.jpg')
# #? we can pass many value here if pass
# #? 0 : blurry
# #? 1: orginal image
# #? 2 : image with incarased sharpness 3-4-5-6----incdresed

#! image color 
# img_obj = Image.open('dog2.jpg')
# img_color = ImageEnhance.Color(img_obj) #?color also a class of ImageEnhance module
# img_color.enhance(3).save('dog2_color.jpg')
# #? if pass
# #? 0 : black and white image
# #? 1: orginal image
# #? 2-3-4-5-6--: incrised color

#! image brightness
#? have to use brightness class. and every thing is same
# img_obj = Image.open('dog2.jpg')
# brightness = ImageEnhance.Brightness(img_obj)
# brightness.enhance(1.5).save('dog2_bright.jpg')
# #? if pass
# #? 0 : black and white image
# #? 1: orginal image
# #? 2-3-4-5-6--: incrised brightness
# #? we can also pass for every class 1.5-2.5-5.5---exetra

#! image contrast -- also same
# img_obj = Image.open('dog2.jpg')
# brightness = ImageEnhance.Contrast(img_obj)
# brightness.enhance(4).save('dog2_bright.jpg')
# # s = Image.open('dog2_bright.jpg')
# # s.show()
# #? if pass
# #? 0 : black and white image
# #? 1: orginal image
# #? 2-3-4-5-6--: incrised brightness
# #? we can also pass for every class 1.5-2.5-5.5---exetra

#! image blur -- use GaussianBlur
# img1 = Image.open('dog1.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1_blur.jpg') #? (radious=4) its defult 2. you can use it for incresing blur