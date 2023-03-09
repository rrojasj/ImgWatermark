# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os

# importing Pillow library
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time

# importing functions from img_wn_functions.py
from img_wm_functions import *

"""
:function: read_files()
:description: Lee e imprime el nombre de los archivos en un directorio específico
:params: p_file_path
"""
def read_files(p_file_path):
    ## Windows: C:/ImgWatermark/Documents
    ## Mac: /Users/robjimn/Documents/Roberto Rojas/Cenfotec
    print("\nLos archivos encontrados en la ruta indicada son: ")

                                             #0          1           2
    for image in os.listdir(file_path): #   [dir, "testing.png", "test.txt"]
        if os.path.isfile(os.path.join(file_path, image)) and image.endswith('.png'):
            print('- '+image)
    print('\n')

"""
:function: wm_text()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_image
"""
def wm_text(p_file_path, p_img_name):

    # Crear un objeto imagen desde la imagen original
    # Se almacena en la variable 'image'
    full_path = p_file_path+p_img_name
    image = Image.open(full_path)
    width, height = image.size

    # Texto a pintar en el objeto imagen que se creó
    draw = ImageDraw.Draw(image)
    text = "ImgWatermark"

    font = ImageFont.truetype('arial.ttf', 24)
    text_width, text_height = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = (width/text_width)+10 # width - text_width - margin
    y = height/text_height # height - text_height - margin

    # Pintar la marca de agua en la esquina superior izquierda 
    new_watermark = draw.text((x,y), text, font=font)
    image.show()

    # Salvar la imagen en el folder predeterminado
    image.save('C:/ImgWatermark/Saved/'+ p_img_name.replace('.png','') +'_img_wm.png')
    print("\nImagen guardada en la ruta destinada: \"C:/ImgWatermark/Saved/\"")
    print("\nGracias por utilizar ImageWatermark Tool.\n")

"""
:function: trans_paste()
:description: Agrega una imagen con transparencia como marca de agua
:params: bg
"""
def trans_paste(p_source_img,alpha=1.0,box=(0,0)):

    wm_img = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_3_100x55_transparent.png")

    # Agrega transparencia a la imagen marca de agua
    wm_img_trans = Image.new("RGBA",wm_img.size)
    wm_img_trans = Image.blend(wm_img_trans,wm_img,alpha)

    # Se une la imagen marca de agua con la imagen origen
    p_source_img.paste(wm_img_trans,box,wm_img_trans)

    return p_source_img

"""
:function: wm_image()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_file_name
"""
def wm_image(p_file_path, p_img_name):

    source_img = Image.open(p_file_path+p_img_name)
    wm_image = trans_paste(source_img,.7,(15,15))

    # No es requerido mostrar la imagen - Deshabilitar
    wm_image.show()

    # Salvar la imagen en el folder predeterminado
    wm_image.save('C:/ImgWatermark/Saved/'+ p_img_name.replace('.png','') +'_img_wm.png')
    print("\nImagen guardada en la ruta destinada: \"C:/ImgWatermark/Saved/\"")
    print("\nGracias por utilizar ImageWatermark Tool.\n")

"""
:function: add_wm_image()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_file_name
"""
def add_watermark(p_file_name, p_file_path): # recibe parámetros
    file_path = p_file_path
    img_name = p_file_name

    for image in os.listdir(file_path):
        if image == img_name:
            wm_type = int(input("Seleccione el tipo de marca de agua:\n1. Texto\n2. Imagen\n"))
            if wm_type == 1:
                wm_text(file_path, img_name)
                break
            else:
                wm_image(file_path, img_name)
                break
    else:
        print("\n La imagen no se encuentra en el directorio.")
        time.sleep(4)

# ============================================ #
#                INICIO: MENU                
# ============================================ #

main_menu()

option_menu = int(input("Seleccione una opción: \n"))

while option_menu != 0:
    if option_menu == 1:
        # Obtener la lista de archivos del directorio
        file_path = input("\n1. Ingrese la ruta del directorio de las imágenes: \n")

        if os.path.exists(file_path):
            read_files(file_path)
        else:
            print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")

       
    elif option_menu == 2:
        # Agregar marca de agua a un archivo
        img_name = input("\n2. Ingrese el nombre de la imagen para la marca de agua: \n")
        file_path = input("\n2. Ingrese la ruta del directorio de la imagen: \n")
        time.sleep(3)
        if os.path.exists(file_path):
            add_watermark(img_name, file_path) # Envía argumentos
        else:
            print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")

    elif option_menu == 3:
        while show_wm_options != 0:
            file_to_update = select_wm_img()

            config_selection = show_wm_options()
            if config_selection == 1:
                select_wm_img()
    else:
        print("Opción inválida.\n")

    menu()
    option_menu = int(input("Seleccione una opción: \n"))


print("\nGracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #

