# --------------- COMMANDS TO INSTALL LIBRARIES ---------------- #

#:numpy      - pip install numpy || pip3 install numpy
#:details    - NumPy is a Python library used for working with arrays

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

#:matplotlib - pip install matplotlib
#:details    - Matplotlib is a Python library used for creating static, animated, and interactive visualizations

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

# Codigo que ayuda a obtener la imagen...
# from PIL import Image
# import matplotlib.pyplot as plt
# import numpy as np

# image = Image.open("C:\ImgWatermark\Documents\/video_game_1.png")

# image.show()
# plt.imshow(image)

# *********************   *********************   ********************* #
# *********************   *********************   ********************* #
# w, h = 205, 213
# x, y = int(w/2), int(h/2)

# # Usar las variables y determinar cuál de los dos valores utilizar - altura o largo
# if x > y:
#     wm_size = y
# elif y > x:
#     wm_size = x
# else:
#     wm_size = x

# size_data = [x, y, wm_size]

# print(size_data[0])

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

# https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm

#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('C:/ImgWatermark/Documents/video_game_3.png')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "ImgWatermark"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
new_var = draw.text((x, y), text, font=font)
new_var
im.show()

#Save watermarked image
im.save('C:/ImgWatermark/Documents/video_game_3_wm.png')