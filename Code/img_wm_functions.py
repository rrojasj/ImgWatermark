import os
import time
from img_watermark import read_files

def main_menu():
    print("\n************** MENÚ DE OPCIONES **************")
    print("[1] Obtener la lista de archivos del directorio")
    print("[2] Agregar marca de agua a un archivo")
    print("[3] Configuración de marca de agua")
    print("[0] Salir del programa \n")

"""
:function: show_wm_options()
:description: Muestra el menú de configuraciones para la marca de agua
:params: N/A
"""
def show_wm_options():
    print("\n************** OPCIONES PARA CONFIGURAR MARCA DE AGUA **************")
    print("[1] Actualizar opacidad de la marca de agua en la imagen")
    print("[2] Actualizar tamaño de la marca de agua en la imagen")
    print("[3] Actualizar ubicación de la marca de agua en la imagen")
    print("[0] Salir de la configuración \n")

    config_selection = int(input("Seleccione una opción de configuración: \n"))
    return config_selection

"""
:function: validate_file()
:description: Valida si la imágen existe o no en el directorio
:params: 
"""
def validate_file(p_saved_dir, p_file_to_update):
    full_path = p_saved_dir+p_file_to_update
    isExisting = os.path.exists(full_path)
    return isExisting


"""
:function: select_wm_img()
:description: Muestra las imágenes con marca de agua guardados y solicita ingresar el nombre de la imagen que se necesita actualizar la marca de agua 
:params: N/A
"""
def select_wm_img():
    saved_dir = "C:/ImgWatermark/Saved"

    read_files(saved_dir)
    time.sleep(3)
    
    file_to_update = input("\nIngrese el nombre de la imagen a actualizar:\n")
    file_exists = validate_file(saved_dir, file_to_update)

    if file_exists == True:
        print("Archivo existe... Invocar función para actualizar")
    else:
        print("La imagen no existe, por favor trate nuevamente")
