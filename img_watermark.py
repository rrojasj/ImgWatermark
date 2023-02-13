import os

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

        basepath = input("Ingrese la ruta del directorio de las imágenes \n")
        ## C:/ImgWatermark/Documents
        print("Los archivos encontrados en la ruta indicada son: \n")
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)) and entry.endswith('.png'):
                print('- '+entry)
        print('\n')
        
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