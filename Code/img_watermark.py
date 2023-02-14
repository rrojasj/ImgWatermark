# Allows to interact with the native OS Python is currently running on.
# It provides an easy way for the user to interact with several os functions
import os

"""
:function: read_files()
:\
"""
def read_files():
    ruta_archivos = input("Ingrese la ruta del directorio de las imágenes \n")
    ## Windows: C:/ImgWatermark/Documents
    ## Mac: /Users/robjimn/Documents/Roberto Rojas/Cenfotec
    print("Los archivos encontrados en la ruta indicada son: ")

    for imagen in os.listdir(ruta_archivos):
        if os.path.isfile(os.path.join(ruta_archivos, imagen)) and imagen.endswith('.png'):
            print('- '+imagen)
    print('\n')

# ============================================ #
#                INICIO: MENU                
# ============================================ #

def menu():
    print("[1] Obtener la lista de archivos del directorio")
    print("[2] Agregar marca de agua a un archivo")
    print("[0] Salir del programa \n")

opcion_menu = int(input("Seleccione una opción: \n"))

while opcion_menu != 0:
    if opcion_menu == 1:
        # Obtener la lista de archivos del directorio
        print("Opción 1 ha sido seleccionada.\n")
        read_files()
       
    elif opcion_menu == 2:
        # Agregar marca de agua a un archivo
        print("Opción 2 ha sido seleccionada.\n")
    else:
        print("Opción inválida.\n")

    menu()
    opcion_menu = int(input("Seleccione una opción: \n"))

print("Gracias por utilizar ImageWatermark Tool.\n")


# ============================================ #
#                FIN: MENU                
# ============================================ #