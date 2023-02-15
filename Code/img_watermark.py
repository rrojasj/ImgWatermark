# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os

# importing Pillow library
from PIL import Image
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
:function: add_wm_image()
:description: Agrega una marca de agua a la imagen indicada por el usuario
:params: p_file_name
"""
def add_wm_image(p_file_name):
    file_path = "C:/ImgWatermark/Documents"
    img_name = p_file_name

    for image in os.listdir(file_path):
        if image == img_name:
            print("Si sirve")
            

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
        add_wm_image(img_name)

    else:
        print("Opción inválida.\n")

    menu()
    option_menu = int(input("Seleccione una opción: \n"))


print("Gracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #