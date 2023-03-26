import os

# importing Pillow library
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time

# importing TKinter library


"""
:function: select_wm_img()
:description: Muestra las imágenes con marca de agua guardados y solicita ingresar el nombre de la imagen que se necesita actualizar la marca de agua 
:params: N/A
"""
def show_alert(message):
    from tkinter import Tk, Label

    #Create an instance of tkinter frame
    win = Tk()

    #Set the geometry of tkinter frame
    win.geometry("750x270")

    #Initialize a Label widget
    Label(win, text= message,
    font=('Helvetica 20 bold')).pack(pady=20)

    #Automatically close the window after 3 seconds
    win.after(3000,lambda:win.destroy())

    win.mainloop()

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

def verify_dir(p_file_path):
    if os.path.exists(p_file_path):
        return True # Envía argumentos
    else:
        return False

"""
:function: read_files()
:description: Lee e imprime el nombre de los archivos en un directorio específico
:params: p_file_path
"""
def read_files(p_file_path):
    ## Windows: C:/ImgWatermark/Documents/
    ## Mac: /Users/robjimn/Documents/Roberto Rojas/Cenfotec
    print("\nLos archivos encontrados en la ruta indicada son: ")

                                             #0          1           2
    for image in os.listdir(p_file_path): #   [dir, "testing.png", "test.txt"]
        if os.path.isfile(os.path.join(p_file_path, image)) and image.endswith('.png'):
            print('- '+image)
    print('\n')


def wm_text(p_file_path, p_img_name):
    """
    :function: wm_text()
    :description: Agrega una marca de agua a la imagen indicada por el usuario
    :params: p_image
    """
    # Crear un objeto imagen desde la imagen original
    # Se almacena en la variable 'image'
    full_path = p_file_path+p_img_name
    image = Image.open(full_path)
    width, height = image.size

    # Texto a pintar en el objeto imagen que se creó
    draw = ImageDraw.Draw(image)
    text = "ImgWatermark"
    
    # Salvar la imagen en el folder que el usuario seleccione
    # C:/ImgWatermark/Saved/
    save_location = input("Seleccione la ubicación donde desea guardar la marca de agua: \n")
    save_true = ""
    if verify_dir(save_location):
        save_true = save_location 
    else:
        print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")

    font = ImageFont.truetype('arial.ttf', 24)
    text_width, text_height = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = (width/text_width)+margin # width - text_width - margin
    y = height/text_height # height - text_height - margin

    # Pintar la marca de agua en la esquina superior izquierda 
    new_watermark = draw.text((x,y), text, font=font)
    image.show()

    # Salvar la imagen en el folder predeterminado
    image.save(save_true+ p_img_name.replace('.png','') +'_text_wm.png')
    print("\nImagen guardada en la ruta destinada: " + save_true)
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
:function: update_wm_opacity()
:description: Agrega una imagen con transparencia como marca de agua desde un inicio
:params: bg
"""
def update_wm_opacity(p_source_img,alpha=1.0,box=(0,0)):

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

    # Salvar la imagen en el folder que el usuario seleccione
    # C:/ImgWatermark/Saved/
    save_location = input("Seleccione la ubicación donde desea guardar la marca de agua: \n")
    save_true = ""
    if verify_dir(save_location):
        save_true = save_location 
    else:
        print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")

    source_img = Image.open(p_file_path+p_img_name)
    wm_image = trans_paste(source_img,.7,(15,15))

    # No es requerido mostrar la imagen - Deshabilitar
    # wm_image.show()
    print(save_true)
    wm_image.save(save_true+ p_img_name.replace('.png','') +'_text_wm.png')
    print("\nImagen guardada en la ruta destinada:" +save_true)
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
            wm_type = int(input("\nSeleccione el tipo de marca de agua:\n1. Texto\n2. Imagen\n"))
            if wm_type == 1:
                wm_text(file_path, img_name)
                break
            else:
                wm_image(file_path, img_name)
                break
    else:
        print("\n La imagen no se encuentra en el directorio.")
        time.sleep(4)


"""
:function: validate_file()
:description: Valida si la imágen existe o no en el directorio
:params: 
"""
def validate_file(p_saved_dir, p_file_to_update):
    full_path = p_saved_dir+p_file_to_update
    isExisting = os.path.exists(full_path)
    return isExisting

# -------------------------------------------------------------
# -------------------------------------------------------------

"""
:function: update_wm_text_transp()
:description: Ejecuta la función para actualizar la transparencia de la marca de agua
:params: 
"""
def update_wm_text_transp():
    return print("")

"""
:function: update_wm_img_transp()
:description: Ejecuta la función para actualizar la transparencia de la marca de agua
:params: 
"""
def update_wm_img_transp():
    return print("")

"""
:function: update_wm_dimension()
:description: Ejecuta la función para redimensionar el tamaño de la marca de agua
:params: 
"""
def update_wm_dimemsion():
    return print("")

"""
:function: update_wm_location()
:description: Ejecuta la función para actualizar la ubicación de la marca de agua en la imagen
:params: 
"""
def update_wm_location():
    return print("")

"""
:function: execute_config_opt()
:description: Ejecuta la opción de config seleccionada e invoca la función respectiva
:params: p_config_selection
"""
def execute_config_opt(p_config_selection, p_file_to_update):

    config_option = p_config_selection
    image = p_file_to_update
    
    while config_option != 0:
        if config_option == 1:
            # 1. Actualizar la transparencia de la MA
            
            if "_text_wm.png" in image:
                new_alpha = input("Ingrese la nueva escala de opacidad de la marca de agua - 0.1 - 1.0: \n")
                update_wm_text_transp()
            else:
                update_wm_img_transp()
        
        elif config_option == 2:
            # 2. Redimensionar la MA
            print("")
        
        elif config_option == 3:
            # 3. Cambiar ubicación de la MA
            print("")

        else:
            print("\nOpción inválida. Vuelva a intentarlo nuevamente.\n")

        config_option = show_wm_options()
        


"""
:function: select_wm_img()
:description: Muestra las imágenes con marca de agua guardados y solicita ingresar el nombre de la imagen que se necesita actualizar la marca de agua 
:params: N/A
"""
def select_wm_img():
    saved_dir = "C:/ImgWatermark/Saved/"

    read_files(saved_dir)
    time.sleep(3)
    
    file_to_update = input("Ingrese el nombre de la imagen a actualizar:\n")
    file_exists = validate_file(saved_dir, file_to_update)

    if file_exists == True:
        print("\nCargando menú de configuraciones\n")
        config_selection = show_wm_options()
        execute_config_opt(config_selection, file_to_update);
    else:
        print("La imagen no existe, por favor trate nuevamente")

