#This program takes an image from the img folder and converts it to a picture you would see in the 60s
#or so. It does this via the Pillow library and its image features.

from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'  # Adjust the output path accordingly

# Create output directory if it doesn't exist
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    # Store image in img
    img = Image.open(f"{path}/{filename}")

    # Decrease sharpness by applying blur
    edit = img.filter(ImageFilter.BLUR).convert('L')

    # Image contrast
    img_enhance = ImageEnhance.Contrast(edit)
    edit = img_enhance.enhance(1.5)

    # Brightness
    img_enhance = ImageEnhance.Brightness(edit)
    edit = img_enhance.enhance(0.8)

    # Change image saturation
    img_enhance = ImageEnhance.Color(edit)
    edit = img_enhance.enhance(0.4)

    # Add grain (Gaussian Blur)
    grain_radius = 1
    edit = edit.filter(ImageFilter.GaussianBlur(radius=grain_radius))

    # Split filename and extension
    clean_name, extension = os.path.splitext(filename)

    # Save edited image in the output directory
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
