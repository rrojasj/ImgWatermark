import os

# importing Pillow library
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time

import pickle

def sv_config_options_pkl():
    """
    function: sv_config_options_pkl()
    description: Guarda los valores por defecto en un archivo pickle
    params: None
    """
    default_config = {
        'Ancho MA Img': 130,
        'Altura MA Img': 30,
        'Tamaño MA Texto': 16,
        'Texto': 'ImgWatermark',
        'Transp_txt': 128,
        'Transp_img': 1.0,
        'Posicion X': 0,
        'Posicion Y': 0,
        'Auto-Ajuste': "Desactivado",
        'Repeticion-Tipo': "Automatico",
        'Repeticion-Activo': "Desactivado",
        'Repeticion-Cant': 2
    }

    with open('default_config.pkl', 'wb') as f:  # open a text file
        pickle.dump(default_config, f) # serialize the list
    f.close()

def ld_config_options_pkl():
    """
    function: ld_config_options_pkl()
    description: Muestra los valores por defecto guardados en el archivo pickle
    params: None
    """
    with open('default_config.pkl', 'rb') as f:

        config_options_loaded = pickle.load(f) # Deserializar usando la función load()
        print("\nValores por defecto actuales de la marca de agua:")

        for key, value in config_options_loaded.items():
            print('- ',key, ': ', value)

def ed_config_options_pkl(p_config_key:str, p_config_value):
    """
    function: ed_config_options_pkl()
    description: Actualiza los valores por defecto y los guarda en el archivo pickle
    params: p_config_key, p_config_value
    """
    key = p_config_key
    value = p_config_value

    with open('default_config.pkl', 'rb') as f:
        config_options_loaded = pickle.load(f)
        config_options_loaded[key] = value
        with open('default_config.pkl', 'wb') as f:  # open a text file
            pickle.dump(config_options_loaded, f) # serialize the list

            f.close()

def get_config_options_dict() -> dict:
    configs_dict = {}
    with open('default_config.pkl', 'rb') as f:
        configs_dict = pickle.load(f)
    return configs_dict

def main_menu():
    print("\n************** MENÚ DE OPCIONES **************")
    print("[1] Obtener la lista de archivos del directorio")
    print("[2] Agregar marca de agua a un archivo")
    print("[3] Aplicar marca de agua a diferentes imágenes")
    print("[4] Mostrar menú de configuraciones")
    print("[0] Salir del programa \n")

def config_menu():
    ld_config_options_pkl()
    print("\n************** MENÚ DE CONFIGURACIONES DE MARCAS DE AGUA **************")
    print("[1] Configuración de Tamaño")
    print("[2] Configuración de Texto")
    print("[3] Configuración de Opacidad")
    print("[4] Configuración de Ubicación")
    print("[5] Configuración de Auto ajuste")
    print("[6] Configuración de tipo de repeticiones")
    print("[7] Configuración de Cantidad de repeticiones")
    print("[8] Configuración de activación de repeticiones")
    print("[0] Salir de configuraciones \n") 

def verify_dir(p_file_path:str):
    """
    function: show_wm_options()
    description: Muestra el menú de configuraciones para la marca de agua
    params: p_file_path
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

def save_one_img(p_sev_imgs:bool, p_image):
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

def apply_wm_auto_reps_img(image_path, watermark, hires=False):
    main = Image.open(image_path)
    mark = Image.open(watermark)
    mark = mark.rotate(30, expand=1)
    mask = mark.convert('L').point(lambda x: min(x, 25))
    mark.putalpha(mask)
    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.4
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.LANCZOS)
    tmp_img = Image.new('RGBA', main.size)
    for i in range(0, tmp_img.size[0], mark.size[0]):
        for j in range(0, tmp_img.size[1], mark.size[1]):
            main.paste(mark, (i, j), mark)
    if not hires:
        main.thumbnail((758, 1000), Image.LANCZOS)
        # main.save(final_image_path, 'PNG', quality=75)
    else:
        main.thumbnail((2048, 2048), Image.LANCZOS)
        # main.save(final_image_path, 'PNG', quality=85)
    return main


def apply_wm_qty_reps_img(image_path, watermark, hires=False):
    import random
    main = Image.open(image_path)
    mark = Image.open(watermark)
    mark = mark.rotate(30, expand=1)
    mask = mark.convert('L').point(lambda x: min(x, 25))
    mark.putalpha(mask)
    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.4
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.LANCZOS)
    tmp_img = Image.new('RGBA', main.size)

    for i in range(7):
        x=random.randint(0, mark_width-300)
        y+=random.randrange(0,int(mark_height/8), 19)+random.randint(0,100)
        main.paste(mark, i, mark)
            
    if not hires:
        main.thumbnail((758, 1000), Image.LANCZOS)
        # main.save(final_image_path, 'PNG', quality=75)
    else:
        main.thumbnail((2048, 2048), Image.LANCZOS)
        # main.save(final_image_path, 'PNG', quality=85)
    return main

def create_wm_qty_reps():
    print()


def apply_wm_txt_config_values(p_file_path:str, p_img_name:str, p_sev_imgs:bool):
    """
    function: config_values()
    description: Pinta el la marca de agua como texto usando valores ingresados por el usuario
    params: p_file_path, p_img_name
    """
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
    # txt = txt.rotate(45)
    
    wm_image = Image.alpha_composite(image, txt)

    # Salvar la información
    save_one_img(p_sev_imgs, wm_image)

    return wm_image

def apply_wm_txt(p_file_path:str, p_img_name:str, p_sev_imgs:bool):
    """
    function: wm_text()
    description: Agrega una marca de agua a la imagen indicada por el usuario
    params: p_image
    """
    # Obtener el diccionario con los valores de configuración por defecto
    config_dict = get_config_options_dict()

    d_size = config_dict['Tamaño MA Texto']
    d_text = config_dict['Texto']
    d_transp = config_dict['Transparencia']
    d_pos_x = config_dict['Posicion X']
    d_pos_y = config_dict['Posicion Y']
    # d_auto_adj = config_dict['Auto-Ajuste']
    d_reps = config_dict['Repeticiones']
    
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

def apply_auto_adj_txt(p_img_path, p_draw, p_d_text):
    image = Image.open(p_img_path).convert("RGBA")
    draw = ImageDraw.Draw(image)
    txt = p_d_text
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.8

    font = ImageFont.truetype("arial.ttf", fontsize)
    while font.getsize(txt)[0] < img_fraction*image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("arial.ttf", fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    adjusted_font = ImageFont.truetype("arial.ttf", fontsize)

    return adjusted_font

def apply_auto_adj_img(p_source_img:Image,p_alpha:float,box:tuple=(0,0)) -> Image:
    """
    function: apply_auto_adj_img()
    description: Aplicar el auto ajuste para una marca de agua como imagen
    params: p_source_img, p_alpha, p_pos_x, p_pos_y
    """
    wm_img = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_3_100x55_transparent.png")
    img_fraction = 0.8

    wm_width, wm_heigth = wm_img.size
    # src_width, src_heigth = p_source_img.size

    while wm_width < img_fraction*p_source_img.size[0]:
        wm_width += 1
        wm_heigth += 1
    
    wm_width -= 1
    wm_heigth -= 50
    wm_adjusted = wm_img.resize((wm_width, wm_heigth))

    # Agrega transparencia a la imagen marca de agua
    wm_img_trans = Image.new("RGBA",wm_adjusted.size)
    wm_img_trans = Image.blend(wm_img_trans,wm_adjusted,p_alpha)

    # Se une la imagen marca de agua con la imagen origen
    p_source_img.paste(wm_img_trans,box,wm_img_trans)

    return p_source_img

def apply_wm_txt_default(p_file_path:str, p_img_name:str, p_sev_imgs:bool):
    """
    function: wm_text()
    description: Agrega una marca de agua a la imagen indicada por el usuario (Valores guardados en pickle)
    params: p_file_path, p_img_name, p_sev_imgs
    """
    # Obtener el diccionario con los valores de configuración por defecto
    config_dict = get_config_options_dict()

    # Guardar los valores del diccionario en variables para mejor comprensión
    d_size = config_dict['Tamaño MA Texto']
    d_text = config_dict['Texto']
    d_transp = config_dict['Transp_txt']
    d_pos_x = config_dict['Posicion X']
    d_pos_y = config_dict['Posicion Y']
    d_auto_adj = config_dict['Auto-Ajuste']
    
    full_path = p_file_path+p_img_name
    image = Image.open(full_path).convert("RGBA")
    img_width, img_height = image.size

    txt = Image.new('RGBA', image.size, (255,255,255,0))

    # Obtener el tipo de fuente y tamaño
    # fnt = ImageFont.truetype('arial.ttf', d_size)

    # get a drawing context
    draw = ImageDraw.Draw(txt)

    # Tamaño depende de si el Auto-Ajuste se encuentra "Activado" o "Desactivado"
    if d_auto_adj == "Activado":
        fnt = apply_auto_adj_txt(full_path, draw, d_text)
    else:
        fnt = ImageFont.truetype('arial.ttf', d_size)
    
    draw.text((d_pos_x, d_pos_y), d_text, font= fnt, fill=(255,255,255,d_transp))
    
    wm_image = Image.alpha_composite(image, txt)

    # Salvar la información
    save_one_img(p_sev_imgs, wm_image)

    return wm_image

def trans_paste(p_src_img_path, p_source_img:Image,p_alpha:float,box:tuple=(0,0)) -> Image:
    """
    function: trans_paste()
    description: Agrega una imagen con transparencia como marca de agua
    params: bg
    """
    wm_img_path = r"C:\ImgWatermark\WM_Logo\IW_logo_3_100x55_transparent.png"
    wm_img = Image.open(r"C:\ImgWatermark\WM_Logo\IW_logo_3_100x55_transparent.png")
    config_dict = get_config_options_dict()

    # Agrega transparencia a la imagen marca de agua
    wm_img_trans = Image.new("RGBA",wm_img.size)
    wm_img_trans = Image.blend(wm_img_trans,wm_img,p_alpha)
    
    if config_dict['Repeticion-Activo'] == "Activado":

        if config_dict['Repeticion-Tipo'] == "Automatico":
            p_source_img = apply_wm_auto_reps_img(p_src_img_path, wm_img_path, True)
        else:
            print("Funcionalidad aún no desarrollada, se aplicará el tipo de repetición por defecto. Gracias por comprender.")
            time.sleep(3)
            p_source_img = apply_wm_auto_reps_img(p_src_img_path, wm_img_path, True)
    else:
        # Se une la imagen marca de agua con la imagen origen
        p_source_img.paste(wm_img_trans,box,wm_img_trans)

    return p_source_img

def apply_wm_img(p_file_path:str, p_img_name:str, default_option:int, p_sev_imgs:bool):
    """
    function: wm_image()
    description: Agrega una marca de agua a la imagen indicada por el usuario
    params: p_file_path, p_img_name, p_option_1, p_sev_imgs
    """
    src_full_path = p_file_path+p_img_name
    source_img = Image.open(src_full_path)
    if default_option == 1:
        config_dict = get_config_options_dict()
        transparency = config_dict['Transp_img']
        x = config_dict['Posicion X']
        y = config_dict['Posicion Y']
        auto_adj = config_dict['Auto-Ajuste']

        if auto_adj == "Activado":
            image = apply_auto_adj_img(source_img, transparency, (x,y))
        else:
            image = trans_paste(src_full_path,source_img,transparency,(x,y))
    else:
        new_alpha = float(input("Ingrese la nueva escala de opacidad de la marca de agua:\n- Valores entre: 0.1 y 1.0\n"))
        input_x = int(input("Nueva posición de la marca en el eje 'x': "))
        input_y = int(input("Nueva posición de la marca en el eje 'y': "))
        image = trans_paste(source_img,new_alpha,(input_x,input_y))

    # No es requerido mostrar la imagen - Deshabilitar
    # wm_image.show()
    
    # Salvar la información
    save_one_img(p_sev_imgs, image)

    return image

def add_watermark(p_file_name:str, p_file_path:str, p_sev_imgs:bool):
    """
    function: add_wm_image()
    description: Agrega una marca de agua a la imagen indicada por el usuario
    params: p_file_name, p_file_path, p_wm_type, p_default_values
    """
    file_path = p_file_path
    img_name = p_file_name
    try:
        for image in os.listdir(file_path):
            
            if image == img_name:
                
                wm_data_dict = get_wm_data()

                if wm_data_dict['type'] == 1:

                    if wm_data_dict['df_option'] == 1:
                        # wm_image = apply_wm_txt(file_path, img_name, p_sev_imgs)
                        wm_image = apply_wm_txt_default(file_path, img_name, p_sev_imgs)
                    else:
                        wm_image = apply_wm_txt_config_values(file_path, img_name, p_sev_imgs)
                    
                    break
                else:
                    wm_image = apply_wm_img(file_path, img_name, wm_data_dict['df_option'], p_sev_imgs)
                    break
        else:
            print("La imagen no se encuentra en el directorio.")

        return wm_image
    except:
        print("\nHa ocurrido una excepción.")

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

def apply_config_updates(p_actual_value,p_key_name,p_value1,p_value2,p_msg1,p_msg2,p_confirm_msg1,p_confirm_msg2):
    
    if p_actual_value == p_value1:    
        print(f"{p_key_name}: {p_actual_value}")
        change_req = int(input(p_msg1))
        if change_req == 1:
            new_value = p_value2
            ed_config_options_pkl(p_key_name, new_value)
        else:
            print(p_confirm_msg1)
    else:
        print(f"{p_key_name}: {p_value2}")
        change_req = int(input(p_msg2))
        if change_req == 1:
            new_value = p_value1
            ed_config_options_pkl(p_key_name, new_value)
        else:
            print(p_confirm_msg2)

def exec_config_option(p_config_option:int) -> str:

    while p_config_option != 0:

        if p_config_option == 1:

            config_size_type = int(input("Tipo de Marca de agua para configurar el tamaño: 1. Texto 2. Imagen\n"))

            if config_size_type == 1:
                fnt_size_key = "Tamaño MA Texto"
                fnt_size = int(input("Ingrese el nuevo tamaño de la marca de agua como texto:\n"))
                ed_config_options_pkl(fnt_size_key, fnt_size)
                break
            else:
                w_key = "Ancho MA Img"
                width = int(input("Ingrese el nuevo ancho de la marca de agua como imagen:\n"))
                ed_config_options_pkl(w_key, width)
                
                h_key = "Altura MA Img"
                height = int(input("Ingrese la nueva altura de la marca de agua como imagen:\n"))
                ed_config_options_pkl(h_key, height)
                break
            
        elif p_config_option == 2:
            text_key = "Texto"
            text = input("Ingrese el nuevo texto de la marca de agua:\n")
            ed_config_options_pkl(text_key, text)
            break

        elif p_config_option == 3:
            transp_wm_type = int(input("Seleccione el tipo de MA: \n1. Texto\n2. Imagen\n"))

            if transp_wm_type == 1:
                text_key = "Transp_txt"
                transp_value = int(input("Ingrese el nuevo grado de transparencia de la marca de agua:\nValor entre 0 y 255"))
                ed_config_options_pkl(text_key, transp_value)
                
            else:
                text_key = "Transp_img"
                transp_value = float(input("Ingrese el nuevo grado de transparencia:\nValor entre 0.0 y 1.0\n"))
                ed_config_options_pkl(text_key, transp_value)
                
            break

        elif p_config_option == 4:
            x_key = "Posicion X"
            x_pos = int(input("Ingrese la nueva posición en el eje 'x' de la marca de agua:\n"))
            ed_config_options_pkl(x_key, x_pos)
            
            
            y_key = "Posicion Y"
            y_pos = int(input("Ingrese la nueva posición en el eje 'y' de la marca de agua:\n"))
            ed_config_options_pkl(y_key, y_pos)
            break

        elif p_config_option == 5:

            actual_value = ""
            key_name = "Auto-Ajuste"
            value1 = "Activado"
            value2 = "Desactivado"
            msg1 = f"Desea Desactivar {key_name}? 1.Si  2.No\n"
            msg2 = f"Desea Activar {key_name}? 1.Si  2.No\n"
            confirm_msg1 = f"Sigue con {key_name}: {value1}"
            confirm_msg2 = f"Sigue con {key_name}: {value2}"

            with open('default_config.pkl', 'rb') as f:
                config_options_loaded = pickle.load(f)
                actual_value = config_options_loaded['Auto-Ajuste']

            apply_config_updates(actual_value,key_name,value1,value2,msg1,msg2,confirm_msg1,confirm_msg2)
            
            break

        elif p_config_option == 6:

            actual_value = ""
            key_name = "Repeticion-Tipo"
            value1 = "Automatico"
            value2 = "Cantidad"
            msg1 = "Desea cambiar el tipo de repetición? 1.Si  2.No\n"
            msg2 = "Desea cambiar el tipo de repetición? 1.Si  2.No\n"
            confirm_msg1 = f"Sigue con {key_name}: {value1}"
            confirm_msg2 = f"Sigue con {key_name}: {value2}"

            with open('default_config.pkl', 'rb') as f:
                config_options_loaded = pickle.load(f)
                actual_value = config_options_loaded['Repeticion-Tipo']
            
            apply_config_updates(actual_value,key_name,value1,value2,msg1,msg2,confirm_msg1,confirm_msg2)
            
            break

        elif p_config_option == 7:

            rep_cant_key = "Repeticion-Cant"
            cant_reps = int(input("Ingrese la nuevo cantidad de repeticiones:\n"))
            ed_config_options_pkl(rep_cant_key, cant_reps)

            break

        elif p_config_option == 8:
            
            actual_value = ""
            key_name = "Repeticion-Activo"
            value1 = "Activado"
            value2 = "Desactivado"
            msg1 = "Desea Desactivar las repeticiones? 1.Si  2.No\n"
            msg2 = "Desea Activar las repeticiones? 1.Si  2.No\n"
            confirm_msg1 = f"Sigue con {key_name}: {value1}"
            confirm_msg2 = f"Sigue con {key_name}: {value2}"

            with open('default_config.pkl', 'rb') as f:
                config_options_loaded = pickle.load(f)
                actual_value = config_options_loaded[key_name]
            
            apply_config_updates(actual_value,key_name,value1,value2,msg1,msg2,confirm_msg1,confirm_msg2)
            
            # if actual_value == value1:
            #     print(f"{key_name}: {actual_value}")
            #     change_req = int(input(msg1))
            #     if change_req == 1:
            #         new_value = value2
            #         ed_config_options_pkl(key_name, new_value)
            #     else:
            #         print(confirm_msg1)
            # else:
            #     print(f"{key_name}: {value2}")
            #     change_req = int(input(msg2))
            #     if change_req == 1:
            #         new_value = value1
            #         ed_config_options_pkl(key_name, new_value)
            #     else:
            #         print(confirm_msg2) 
            break

        else:
            msg = "Opción inválida. Seleccione nuevamente.\n"
            print(msg)
            
        config_menu()
        config_option = int(input("Seleccione una opción: \n"))
        exec_config_option(config_option)
        