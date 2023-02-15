# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os

# importing Pillow library
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


"""
:function: read_files()
:\
"""

def read_files():
    file_path = input("Ingrese la ruta del directorio de las imágenes \n")
    ## Windows: C:/ImgWatermark/Documents
    ## Mac: /Users/robjimn/Documents/Roberto Rojas/Cenfotec
    print("Los archivos encontrados en la ruta indicada son: ")

                                             #0          1           2
    for image in os.listdir(file_path): #   [dir, "testing.png", "test.txt"]
        if os.path.isfile(os.path.join(file_path, image)) and image.endswith('.png'):
            print('- '+image)
    print('\n')

# ============================================ #
#                INICIO: MENU                
# ============================================ #

def menu():
    print("[1] Obtener la lista de archivos del directorio")
    print("[2] Agregar marca de agua a un archivo")
    print("[0] Salir del programa \n")

option_menu = int(input("Seleccione una opción: \n"))

while option_menu != 0:
    if option_menu == 1:
        # Obtener la lista de archivos del directorio
        print("Opción 1 ha sido seleccionada.\n")
        read_files()
       
    elif option_menu == 2:
        # Agregar marca de agua a un archivo
        print("Opción 2 ha sido seleccionada.\n")

    else:
        print("Opción inválida.\n")

    menu()
    option_menu = int(input("Seleccione una opción: \n"))

print("Gracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #