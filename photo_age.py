from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'
for filename in os.listdir(path):
    #store image in img
    img = Image.open(f"{path}/{filename}")

    #sharpen the image
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    #image contra st
    img_enhance = ImageEnhance.contrast(edit)
    edit = img_enhance.enhance(1.5)
   
    #brightness
    img_enhance = ImageEnhance.Brightness(edit)
    edit = img_enhance(.8)
    
    #change image saturation
    img_enhance = ImageEnhance.color(edit)
    edit = img_enhance(.4)


    clean_name = os.path.splittext(filename)[0]
    edit.save(f'{path}/{clean_name}")_edited.jpg')