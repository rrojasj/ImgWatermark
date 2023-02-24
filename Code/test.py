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

# #Import required Image library
# from PIL import Image, ImageDraw, ImageFont

# #Create an Image Object from an Image
# im = Image.open('C:/ImgWatermark/Documents/video_game_3.png')
# width, height = im.size

# draw = ImageDraw.Draw(im)
# text = "ImgWatermark"

# font = ImageFont.truetype('arial.ttf', 36)
# textwidth, textheight = draw.textsize(text, font)

# # calculate the x,y coordinates of the text
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin

# # draw watermark in the bottom right corner
# new_var = draw.text((x, y), text, font=font)
# new_var
# im.show()

# #Save watermarked image
# im.save('C:/ImgWatermark/Documents/video_game_3_wm.png')

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

# https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm

# WORKING!!!!

# # Importing Image module from PIL package
# from PIL import Image
 
# # creating a image object (main image)
# im1 = Image.open(r"C:\ImgWatermark\Documents\video_game_3.png")
 
# # creating a image object (image which is to be paste on main image)
# im2 = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_2_100x61_trasparent.png")
 
# # pasting im2 on im1
# Image.Image.paste(im1, im2, (15, 15))
 
# # to show specified image
# im1.show()


# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

# https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm

# #Import required Image library
# from PIL import Image, ImageDraw, ImageFont

# #Create an Image Object from an Image
# image = Image.open('C:/ImgWatermark/Documents/video_game_3.png')
# width, height = image.size

# imgwm_logo = ('C:/ImgWatermark/WM_Logo/imgwatermark_logo_200x131')

# # calculate the x,y coordinates of the text
# # x = (width/8)+10 # width - text_width - margin
# # y = height/8 # height - text_height - margin


# # draw watermark in the bottom right corner
# image.paste(image, imgwm_logo, (0,0))
# image.show()

# #Save watermarked image
# image.save('C:/ImgWatermark/Documents/video_game_3_wm_logo.png')

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

# # Importing Image module from PIL package
# from PIL import Image, ImageDraw, ImageFilter
 
# # creating a image object (main image)
# im1 = Image.open(r"C:\ImgWatermark\Documents\video_game_3.png")
 
# # creating a image object (image which is to be paste on main image)
# im2 = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_2_100x61.png")

# im2 = im2.convert("RGBA")

# datas = im2.getdata()

# newData = []

# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# im2.putdata(newData)

# # pasting im2 on im1
# Image.Image.paste(im1, im2, (15, 15))
 
# # to show specified image
# im1.show()


# -----  -----  -----  -----  -----  -----  -----  -----  -----  #

# https://holypython.com/how-to-watermark-images-w-python-pil/

# from PIL import Image, ImageDraw

# def main():
#     # Open the original image
#     main = Image.open(r"C:\ImgWatermark\Documents\video_game_3.png")

#     # Create a new image for the watermark with an alpha layer (RGBA)
#     #  the same size as the original image
#     watermark = Image.new("RGBA", main.size)
#     # Get an ImageDraw object so we can draw on the image
#     waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
#     # Place the text at (10, 10) in the upper left corner. Text will be white.
#     # waterdraw.text((10, 10), "The Image Project")
#     Image.Image.paste(im1, im2, (15, 15))

#     # Get the watermark image as grayscale and fade the image
#     # See <http://www.pythonware.com/library/pil/handbook/image.htm#Image.point>
#     #  for information on the point() function
#     # Note that the second parameter we give to the min function determines
#     #  how faded the image will be. That number is in the range [0, 256],
#     #  where 0 is black and 256 is white. A good value for fading our white
#     #  text is in the range [100, 200].
#     watermask = watermark.convert("L").point(lambda x: min(x, 100))
#     # Apply this mask to the watermark image, using the alpha filter to 
#     #  make it transparent
#     watermark.putalpha(watermask)

#     # Paste the watermark (with alpha layer) onto the original image and save it
#     main.paste(watermark, None, watermark)
#     main.show(watermark)

# if __name__ == '__main__':
#     main()


# -----  -----  -----  -----  -----  -----  -----  -----  -----  #
# WINNER!!!

# from PIL import Image

# def trans_paste(bg_img,alpha=1.0,box=(0,0)):
#     fg_img = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_3_100x55_trasparent.png")
#     fg_img_trans = Image.new("RGBA",fg_img.size)
#     fg_img_trans = Image.blend(fg_img_trans,fg_img,alpha)
#     bg_img.paste(fg_img_trans,box,fg_img_trans)
#     return bg_img

# bg_img = Image.open(r"C:\ImgWatermark\Documents\hacking_1.png")
# wm_image = trans_paste(bg_img,.7,(15,15))
# wm_image.show()


# -----  -----  -----  -----  -----  -----  -----  -----  -----  #


# USEFUL LINKS
# - https://holypython.com/how-to-watermark-images-w-python-pil/
# - 