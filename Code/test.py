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

# WORKING - WITHOUT TRANSPARENCY!!!!

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

# resource: https://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #


# USEFUL LINKS
# - https://holypython.com/how-to-watermark-images-w-python-pil/
# - https://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil

# import datetime


# fecha_actual = datetime.datetime.now()
# print(fecha_actual)

# -----  -----  -----  -----  -----  -----  -----  -----  -----  #


# from PIL import Image, ImageDraw, ImageFont

# def trans_wm_text(p_alpha)

# num = int(input("Digite el numero:\n"))
# alpha = 0.5

# if num == 1:


# # get an image

# Image.open("C:/ImgWatermark/Documents/hacking_1.png").convert("RGBA") as base:

# # make a blank image for the text, initialized to transparent text color
# txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

# # get a font
# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
# # get a drawing context
# d = ImageDraw.Draw(txt)

# # draw text, half opacity
# d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
# # draw text, full opacity
# d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

# out = Image.alpha_composite(base, txt)

# out.show()


# -------------------------------------------------------------
# -------------------------------------------------------------

# """
# :function: update_wm_text_opacity()
# :description: Ejecuta la función para actualizar la transparencia de la marca de agua
# :params: 
# """
# def update_wm_text_opacity(p_file_path, p_img_name, p_new_alpha):
    
#     # Crear un objeto imagen desde la imagen original
#     # Se almacena en la variable 'image'
#     full_path = p_file_path+p_img_name
#     image = Image.open(full_path)
#     width, height = image.size

#     # Texto a pintar en el objeto imagen que se creó
#     draw = ImageDraw.Draw(image)
#     text = "ImgWatermark"
    
#     # Salvar la imagen en el folder que el usuario seleccione
#     # C:/ImgWatermark/Saved/
#     save_location = input("Seleccione la ubicación donde desea guardar la marca de agua: \n")
#     save_true = ""
#     if verify_dir(save_location):
#         save_true = save_location 
#     else:
#         print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")

#     font = ImageFont.truetype('arial.ttf', 24)
#     text_width, text_height = draw.textsize(text, font)

#     # calculate the x,y coordinates of the text
#     margin = 10
#     x = (width/text_width)+margin # width - text_width - margin
#     y = height/text_height # height - text_height - margin

#     # Pintar la marca de agua en la esquina superior izquierda 
#     new_watermark = draw.text((x,y), text, font=font, fill=(255,255,255,p_new_alpha))
#     image.show()

#     # Salvar la imagen en el folder predeterminado
#     image.save(save_true+ p_img_name.replace('.png','') +'_text_wm.png')
#     print("\nImagen guardada en la ruta destinada: " + save_true)
#     print("\nGracias por utilizar ImageWatermark Tool.\n")

# """
# :function: update_wm_img_opacity()
# :description: Ejecuta la función para actualizar la transparencia de la marca de agua
# :params: 
# """
# def update_wm_img_opacity(p_file_path, p_img_name, p_new_alpha, box=(0,0)):

#     return ""
    
# """
# :function: update_wm_dimension()
# :description: Ejecuta la función para redimensionar el tamaño de la marca de agua
# :params: 
# """
# def update_wm_dimemsion():
#     return print("")

# """
# :function: update_wm_location()
# :description: Ejecuta la función para actualizar la ubicación de la marca de agua en la imagen
# :params: 
# """
# def update_wm_location():
#     return print("")

# """
# :function: execute_config_opt()
# :description: Ejecuta la opción de config seleccionada e invoca la función respectiva
# :params: p_config_selection
# """
# def get_wm_config_values(p_config_selection, p_saved_dir, p_file_to_update):

#     while p_config_selection != 0:
#         if p_config_selection == 1:
#             # 1. Actualizar la transparencia de la MA
            
#             if "_text_wm.png" in p_file_to_update:
#                 new_alpha = float(input("Ingrese la nueva escala de opacidad de la marca de agua:\n- Valores entre: 0.1 y 1.0\n"))
#                 update_wm_text_opacity(p_saved_dir, p_file_to_update, new_alpha)
#             else:
#                 option_1 = False
#                 wm_image(p_saved_dir, p_file_to_update, option_1)
        
#         elif p_config_selection == 2:
#             # 2. Redimensionar la MA
#             print("")
        
#         elif p_config_selection == 3:
#             # 3. Cambiar ubicación de la MA
#             print("")

#         else:
#             print("\nOpción inválida. Vuelva a intentarlo nuevamente.\n")

#         p_config_selection = show_wm_options()

# """
# :function: select_wm_img()
# :description: Muestra las imágenes con marca de agua guardados y solicita ingresar el nombre de la imagen que se necesita actualizar la marca de agua 
# :params: N/A
# """
# def select_wm_img():
#     saved_dir = "C:/ImgWatermark/Saved/"

#     read_files(saved_dir)
#     # time.sleep(3)
    
#     file_to_update = input("Ingrese el nombre de la imagen a actualizar:\n")
#     full_path = saved_dir + file_to_update
#     file_exists = validate_file(full_path)

#     if file_exists == True:
#         print("\nCargando menú de configuraciones\n")
#         config_selection = show_wm_options()
#         execute_config_opt(config_selection, saved_dir, file_to_update);
#     else:
#         print("La imagen no existe, por favor trate nuevamente")

# Para ser implementada
# def show_wm_options():
#     """
#     :function: show_wm_options()
#     :description: Muestra el menú de configuraciones para la marca de agua
#     :params: N/A
#     """
#     print("\n************** OPCIONES PARA CONFIGURAR MARCA DE AGUA **************")
#     print("[1] Actualizar opacidad de la marca de agua en la imagen")
#     print("[2] Actualizar tamaño de la marca de agua en la imagen")
#     print("[3] Actualizar ubicación de la marca de agua en la imagen")
#     print("[0] Salir de la configuración \n")

#     config_selection = int(input("Seleccione una opción de configuración: \n"))
#     return config_selection

# wm_type = int(input("\nSeleccione el tipo de marca de agua:\n1. Texto\n2. Imagen\n"))
# default_values = int(input("\nIndique si desea los valores por defecto:\n1. Si\n2. No\n"))

# wm_data_dict = {'type': wm_type, 'option': default_values}

# counter = 0
# for opt in wm_data_dict:
#     print(wm_data_dict[opt])

# print(wm_data_dict['type'])

# *********************************************************************************** #
# *********************************************************************************** #

# import pickle

# def save_pkl():

#     students = {
#         'Student 1': {
#             'ID': "1", 'Name': "Alice", 'Age' :10, 'Grade':4,
#         },
#         'Student 2': {
#             'ID': "2", 'Name':'Bob', 'Age':11, 'Grade':5
#         },
#         'Student 3': {
#             'ID': "3", 'Name':'Elena', 'Age':14, 'Grade':8
#         }
#     }

#     with open('student_file.pkl', 'wb') as f:  # open a text file
#         pickle.dump(students, f) # serialize the list

#     f.close()

# def load_pkl():

#     with open('student_file.pkl', 'rb') as f:

#         student_names_loaded = pickle.load(f) # deserialize using load()
#         print(student_names_loaded) # print student names
#         print(type(student_names_loaded))

# def add_new_student():
#     id = int(input("ID del estudiante\n"))
#     std_dict = "Student " + str(id)
#     name = input("Nombre del estudiante:\n")
#     age = int(input("Edad del estudiante:\n"))
#     grade = int(input("Grado del estudiante:\n"))

#     with open('student_file.pkl', 'rb') as f:
#         student_names_loaded = pickle.load(f)
#         student_names_loaded[std_dict] = {'ID': str(id), 'Name':name, 'Age':age, 'Grade':grade}
#         with open('student_file.pkl', 'wb') as f:  # open a text file
#             pickle.dump(student_names_loaded, f) # serialize the list

#             f.close()

# def update_student():
#     id = int(input("ID del estudiante\n"))
#     std_dict = "Student " + str(id)
#     name = input("Nombre del estudiante:\n")

#     with open('student_file.pkl', 'rb') as f:
#         student_names_loaded = pickle.load(f)
#         student_names_loaded[std_dict]['Name'] = name
#         with open('student_file.pkl', 'wb') as f:  # open a text file
#             pickle.dump(student_names_loaded, f) # serialize the list

#             f.close()

# def get_student_id() -> str:
#     id = input("ID del estudiante:\n")
#     return id

# def get_student_info(p_id:str):
#     with open('student_file.pkl', 'rb') as f:
#         student = "Student "+ p_id 
#         student_names_loaded = pickle.load(f) # deserialize using load()
#         print(student_names_loaded[student])

# def pickle_menu():
#     print("\n************** MENÚ **************")
#     print("[1] Guardar lista de estudiantes")
#     print("[2] Obtener lista de estudiantes")
#     print("[3] Agregar nuevo estudiante")
#     print("[4] Información de un estudiante")
#     print("[5] Editar información de un estudiante")
#     print("[0] Salir del programa \n")

# pickle_menu()
# pickle_opt = int(input("Seleccione una opción: \n"))

# while pickle_opt != 0:

#     if pickle_opt == 1:
#         save_pkl()
#     elif pickle_opt == 2:
#         load_pkl()
#     elif pickle_opt == 3:
#         add_new_student()
#     elif pickle_opt == 4:
#         id = get_student_id()
#         get_student_info(id)
#     elif pickle_opt == 5:
#         update_student()
#     else:
#         print("Opción inválida.\n")

#     pickle_menu()
#     pickle_opt = int(input("Seleccione una opción: \n"))

# *********************************************************************************** #
# *********************************************************************************** #

from PIL import ImageFont, ImageDraw, Image

image = Image.open('C:/ImgWatermark/Documents/hacking_1.png')
draw = ImageDraw.Draw(image)
txt = "Hello World"
fontsize = 12  # starting font size

# portion of image width you want text width to be
img_fraction = 0.50

font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(txt)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype("arial.ttf", fontsize)

print('final font size',fontsize)
draw.text((10, 25), txt, font=font) # pu
new_name = "LasChanas"
p_image.save(f"{save_true}{new_name}.png")