# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os
import tkinter

# importing Pillow library
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time

from img_wm_functions import *

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
            #alert_title = "Lista de imágenes"
            alert_message = "Cargando imágenes..."
            show_alert(alert_message) # No está mostrando el pop-up
            print("\nCargando imágenes...")
            time.sleep(3)
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
        select_wm_img()

    else:
        print("Opción inválida.\n")

    main_menu()
    option_menu = int(input("Seleccione una opción: \n"))


print("\nGracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #

