# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os
import tkinter

# importing Pillow library
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from img_wm_functions import *
import numpy as np
import time

# Importing pickle library
import pickle

# 


# ============================================ #
#                INICIO: MENU
# ============================================ #
sv_config_options_pkl()
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
            # time.sleep(3)
            read_files(file_path)
        else:
            print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")
       
    elif option_menu == 2:
        # Agregar marca de agua a un archivo
        img_name = input("\n1. Ingrese el nombre de la imagen para la marca de agua: \n")
        file_path = input("\n2. Ingrese la ruta del directorio de la imagen: \n")
        # time.sleep(3)
        
        if verify_dir(file_path):

            wm_data_dict = get_wm_data()
            add_watermark(img_name, file_path, wm_data_dict, p_sev_imgs=False)
            
        else:
            print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")
    
    elif option_menu == 3:
        file_path = input("\n1. Ingrese la ruta del directorio de las imágenes: \n")

        if verify_dir(file_path):
            img_list = get_several_imgs(file_path)
            wm_data_dict = get_wm_data()

            apply_wm_several_imgs(img_list, file_path, wm_data_dict)
            
        else:
            print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")
    
    elif option_menu == 4:
        config_menu()
        config_option = int(input("Seleccione una opción: \n"))

        exec_config_option(config_option)     

    else:
        print("Opción inválida.\n")

    main_menu()
    option_menu = int(input("Seleccione una opción: \n"))


print("\nGracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #

