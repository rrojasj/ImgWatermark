import os

# importing Pillow library
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time

def show_alert(message):
    """
    function: select_wm_img()
    description: Muestra las imágenes con marca de agua guardados y solicita ingresar el nombre de la imagen que se necesita actualizar la marca de agua 
    params: N/A
    """
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
    print("[3] Aplicar marca de agua a diferentes imágenes")
    print("[0] Salir del programa \n")

def verify_dir(p_file_path:str):
    """
    function: show_wm_options()
    description: Muestra el menú de configuraciones para la marca de agua
    param
    """
    if os.path.exists(p_file_path):
        return True # Envía argumentos
    else:
        return False

def read_files(p_file_path:str):
    """
    :function: read_files()
    :description: Lee e imprime el nombre de los archivos en un directorio específico
    :params: p_file_path
    """
    ## Windows: C:/ImgWatermark/Documents/
    ## Mac: /Users/robjimn/Documents/Roberto Rojas/Cenfotec
    print("\nLos archivos encontrados en la ruta indicada son: ")

                                             #0          1           2
    for image in os.listdir(p_file_path): #   [dir, "testing.png", "test.txt"]
        if os.path.isfile(os.path.join(p_file_path, image)) and image.endswith('.png'):
            print('- '+image)
    print('\n')

def verify_save_dir() -> str:
    """
    function: verify_save_dir()
    description: Verifica que la ruta ingresada para guardar el archivo esté correcta
    params: None
    """
    save_location = input("\nSeleccione la ubicación donde desea salvar la información: \n")
    save_true = ""
    if verify_dir(save_location):
        save_true = save_location 
        return save_true
    else:
        print("\nLa ruta del directorio ingresada no existe.\nIntente nuevamente, gracias.")

def save_one_img(p_sev_imgs:bool, p_image:Image):
    """
    function: save_options()
    description: Verifica la ruta de guardado, la cantidad de imágenes y selecciona el proceso correcto y retorna el mensaje correspondiente
    params: p_sev_imgs, p_image
    """
    if p_sev_imgs == False:
        save_true = verify_save_dir()
        new_name = input("Por favor el nombre de la imagen para guardar:\n")
        p_image.save(f"{save_true}{new_name}.png")
        print(f"\nImagen guardada en la ruta destinada: {save_true}")
        print("\nGracias por utilizar ImageWatermark Tool.\n")

def apply_wm_txt_config_values(p_file_path:str, p_img_name:str, p_sev_imgs:bool):
    """
    function: config_values()
    description: Pinta el la marca de agua como texto usando valores ingresados por el usuario
    params: p_file_path, p_img_name
    """
    # Crear un objeto imagen desde la imagen original
    # Se almacena en la variable 'image'
    full_path = p_file_path+p_img_name
    image = Image.open(full_path).convert("RGBA")
    orig_width, orig_height = image.size

    txt = Image.new('RGBA', image.size, (255,255,255,0))

    # Obtener el tipo de fuente y tamaño
    fnt = ImageFont.truetype('arial.ttf', 24)
    # get a drawing context
    draw = ImageDraw.Draw(txt)
    wm_txt = "ImgWatermark"

    alpha = int(input("Ingresar el valor de la opacidad entre 0 y 255:\n"))    
    wm_width = int(input("Ingresar el ancho de la marca de agua:\n"))
    wm_height = int(input("Ingresar la altura de la marca de agua:\n"))

    coord_x = 0
    coord_y = 0
    msj = "El tamaño de la marca de agua debe ser menor que el tamaño de la imagen.\nPor favor intente nuevamente. Muchas gracias."
    if wm_width < orig_width:
        if wm_height < orig_height:
            coord_x = int(input("Ingresar la coordenada X de la marca de agua:\n"))
            coord_y = int(input("Ingresar la coordenada Y de la marca de agua:\n"))
        else:
            print(msj)
    else:
        print(msj)
    
    draw.text((coord_x, coord_y), wm_txt, font= fnt, fill=(255,255,255,alpha))
    txt = txt.rotate(45) 
    
    wm_image = Image.alpha_composite(image, txt)
    # wm_image.show

    # Salvar la información
    save_one_img(p_sev_imgs, image)

    return image

def apply_wm_txt(p_file_path:str, p_img_name:str, p_sev_imgs:bool):
    """
    function: wm_text()
    description: Agrega una marca de agua a la imagen indicada por el usuario
    params: p_image
    """
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
    x = (width/text_width)+margin # width - text_width - margin
    y = height/text_height # height - text_height - margin

    # Pintar la marca de agua en la esquina superior izquierda 
    new_watermark = draw.text((x,y), text, font=font)
    # image.show()

    # Salvar la información
    save_one_img(p_sev_imgs, image)

    return image

def trans_paste(p_source_img:Image,p_alpha:float,box:tuple=(0,0)) -> Image:
    """
    function: trans_paste()
    description: Agrega una imagen con transparencia como marca de agua
    params: bg
    """
    wm_img = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_3_100x55_transparent.png")

    # Agrega transparencia a la imagen marca de agua
    wm_img_trans = Image.new("RGBA",wm_img.size)
    wm_img_trans = Image.blend(wm_img_trans,wm_img,p_alpha)

    # Se une la imagen marca de agua con la imagen origen
    p_source_img.paste(wm_img_trans,box,wm_img_trans)

    return p_source_img

def apply_wm_img(p_file_path:str, p_img_name:str, default_option:int, p_sev_imgs:bool):
    """
    function: wm_image()
    description: Agrega una marca de agua a la imagen indicada por el usuario
    params: p_file_path, p_img_name, p_option_1, p_sev_imgs
    """

    source_img = Image.open(p_file_path+p_img_name)
    if default_option == 1:
        image = trans_paste(source_img,1.0,(15,15))
    else:
        new_alpha = float(input("Ingrese la nueva escala de opacidad de la marca de agua:\n- Valores entre: 0.1 y 1.0\n"))
        image = trans_paste(source_img,new_alpha,(15,15))

    # No es requerido mostrar la imagen - Deshabilitar
    # wm_image.show()
    
    # Salvar la información
    save_one_img(p_sev_imgs, image)

    return image

def add_watermark(p_file_name:str, p_file_path:str, p_wm_data_dict:dict, p_sev_imgs:bool):
    """
    function: add_wm_image()
    description: Agrega una marca de agua a la imagen indicada por el usuario
    params: p_file_name, p_file_path, p_wm_type, p_default_values
    """
    file_path = p_file_path
    img_name = p_file_name

    for image in os.listdir(file_path):
        
        if image == img_name:
            
            if p_wm_data_dict['type'] == 1:

                if p_wm_data_dict['df_option'] == 1:
                    wm_image = apply_wm_txt(file_path, img_name, p_sev_imgs)
                else:
                    wm_image = apply_wm_txt_config_values(file_path, img_name, p_sev_imgs)
                
                break
            else:
                wm_image = apply_wm_img(file_path, img_name, p_wm_data_dict['df_option'], p_sev_imgs)
                break
    else:
        print("\n La imagen no se encuentra en el directorio.")
        time.sleep(4)

    return wm_image

def validate_file(p_full_path:str) -> bool:
    """
    function: validate_file()
    description: Valida si la imágen existe o no en el directorio
    params: 
    """
    isExisting = os.path.exists(p_full_path)
    return isExisting

def get_several_imgs(p_img_path:str) -> list:
    """
    function: get_several_imgs(String)
    description: Obtener la lista de imágenes que se debe agregar la marca de agua
    params: p_img_path
    """
    img_path = p_img_path
    breaker = 0
    img_list = []

    while breaker != 1:
        image = input("\nIngrese el nombre de la imagen - ingrese 1 para terminar)\n")
        if image != "1":
            full_path = img_path+image
            if validate_file(full_path):
                img_list.append(image)
            else:
                print("La imagen no existe en el directorio.") 
        else:
            break

    return img_list

def apply_wm_several_imgs(p_img_list:list, p_file_path:str, p_wm_data_dict:dict):
    """
    function: apply_wm_several_imgs()
    description: Aplicar la marca de agua a diferentes imágenes
    params: p_img_list, p_file_path, p_wm_data_dict
    """

    save_true = verify_save_dir()
    new_name = input("\nIndique el nombre del conjunto de imágenes a guardar:\n")
    sev_imgs = True
    i = 0

    while i < len(p_img_list):
        wm_image = add_watermark(p_img_list[i], p_file_path, p_wm_data_dict, sev_imgs)
        wm_image.save(f"{save_true}{new_name}_{(i+1)}.png")
        i += 1

    print(f"\nImágenes guardadas en la ruta destinada: {save_true}. Nombre del conjunto: {new_name}")
    print("\nGracias por utilizar ImageWatermark Tool.\n")

def get_wm_data() -> dict:
    
    wm_type = int(input("\nSeleccione el tipo de marca de agua:\n1. Texto\n2. Imagen\n"))
    default_option = int(input("\nIndique si desea los valores por defecto:\n1. Si\n2. No\n"))

    add_wm_data_dict = {'type': wm_type, 'df_option': default_option}

    return add_wm_data_dict
