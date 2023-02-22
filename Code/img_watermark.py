# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os

# importing Pillow library
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import time


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
:function: set_wm_size()
:description: Darle el tamaño a la marca de agua
:params: p_image
"""
def set_wm_size(p_image):
    # Darle el valor a las variables para determinar el tamaño de la marca de agua
    w, h = p_image.size
    x, y = int(w/2), int(h/2)

    # Usar las variables y determinar cuál de los dos valores utilizar - altura o largo
    if x > y:
        wm_size = y
    elif y > x:
        wm_size = x
    else:
        wm_size = x

    return x, y, wm_size

"""
:function: wm_text()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_image
"""
def wm_text(p_image):

    # Abrir imágen - Es necesario para poder editar
    image = Image.open(p_image)

    # Abrir la imágen en photo viewer
    image.show()
    plt.imshow(image)

    # Hacer una copia de la imagen original
    watermark_image = image.copy()

    # Hacer la imagen editable por utilizar ImageDraw
    draw = ImageDraw.Draw(watermark_image)

    # Obtener el tamaño de la marca de agua
    wm_size = set_wm_size(watermark_image)

    # Tipo de fuente y atributos
    font = ImageFont.truetype("arial.ttf", int(wm_size[2]/6))
    
    # Agregar la marca de agua!
    print("TESTING")
    print(wm_size[0])
    print(wm_size[1])
    print("\n")
    draw.text((wm_size[0], wm_size[1]), "ImgWatermark", fill=(192, 192, 192), font=font, anchor='ms') 
    #subplot(nrows, ncols, index, **kwargs)
    # plt.subplots(1, 2, 1)
    plt.imshow(watermark_image)

"""
:function: wm_image()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_file_name
"""
def wm_image(p_image):
    print("")

"""
:function: add_wm_image()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_file_name
"""
def add_wm_image(p_file_name): # recibe parámetros
    file_path = "C:/ImgWatermark/Documents/"
    img_name = p_file_name

    for image in os.listdir(file_path):
        if image == img_name:
            wm_type = int(input("Seleccione el tipo de marca de agua:\n1. Texto\n2. Imágen\n"))
            if wm_type == 1:
                wm_text(file_path+image)
            else:
                wm_image(file_path+image)


    print("\n La imagen no se encuentra en el directorio.")
    time.sleep(4)

# ============================================ #
#                INICIO: MENU                
# ============================================ #

def menu():
    print("\n************** MENÚ DE OPCIONES **************")
    print("[1] Obtener la lista de archivos del directorio")
    print("[2] Agregar marca de agua a un archivo")
    print("[0] Salir del programa \n")

menu()
option_menu = int(input("Seleccione una opción: \n"))

while option_menu != 0:
    if option_menu == 1:
        # Obtener la lista de archivos del directorio
        file_path = input("\n1. Ingrese la ruta del directorio de las imágenes: \n")
        read_files(file_path)
       
    elif option_menu == 2:
        # Agregar marca de agua a un archivo
        img_name = input("\n2. Ingrese el nombre de la imagen para la marca de agua: \n")
        add_wm_image(img_name) # Envía argumentos

    else:
        print("Opción inválida.\n")

    menu()
    option_menu = int(input("Seleccione una opción: \n"))


print("Gracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #