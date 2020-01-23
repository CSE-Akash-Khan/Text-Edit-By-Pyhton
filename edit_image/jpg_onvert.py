from PIL import Image,ImageEnhance
import os
for item in os.listdir():
    if item.endswith('.png'):
        img1 = Image.open(item)
        image_color = ImageEnhance.Color(img1)
        file_name,extention = os.path.splitext(item)
        img1.convert('RGB').save(f"{file_name}.jpg")
        os.remove(item)
