"""
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
"""

import os.path
from os import remove

filename = "text.txt"
menu = True


def check_exist() -> bool:
    if os.path.isfile(filename):
        return True
    else:
        return False


def main():
    global menu

    if check_exist():
        print(f"El archivo {filename} existe y tiene el siguiente contenido:")
        f = open(filename, "r")
        print(f.read())
        f.close()
    else:
        f = open(filename, "x")
        f.write("Hola Mundo")
    while menu == True:
        menu_add = "y"
        print("Que deseas hacer?:")
        print("1. Añadir Contenido:")
        print("2. Borrar el archivo y empezar de nuevo")
        print("3. Salir y Guardar")
        opcion = input("Elige una opcion 1,2 o 3: ")
        match opcion:
            case "1":
                while menu_add == "y":
                    f = open(filename, "r")
                    print(f.read())
                    f.close()
                    text_add = input("Escribe tu texto a añadir:")
                    f = open(filename, "a+")
                    f.write(f"\n{text_add}")
                    f.close()
                    menu_add = input("Deseas agregar mas texto? (y/n):")

            case "2":
                remove("text.txt")
                f = open(filename, "x")
                f.close()
            case "3":
                menu = False


if __name__ == "__main__":
    main()
