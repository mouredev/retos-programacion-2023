"""
/*
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
 */
 """

import os
import sys
import re

MODE_OVERWRITE = "w"
MODE_APPEND = "a"

def writeFromTerminalToFile(mode):
    file = open('text.txt', mode)
    while True:
        line = input("Introduce una línea o pulsa escape, en ambos casos termina con enter: \n")
        if line.__contains__("\x1b"):
            file.close()
            sys.exit()
        else:
            file.write(line+"\n")


if os.path.exists("text.txt"):
    print("El fichero 'text.txt' ya existe.")
    print("¿Deseas eliminar  el contenido o continuar escribiendo?")
    option = ""
    while not re.match("^[1-2]|(\\x1b$)", option):
        print("Elige una opción [1, 2] o escape y pulsa enter:")
        print("  1 - Eliminar contenido")
        print("  2 - Continuar escribiendo")
        option = input()
    if option == "1":
        print("Contenido de 'text.txt' eliminado, escribe nuevas líneas")
        writeFromTerminalToFile(MODE_OVERWRITE) 
    elif option == "2":
        print("Añade lineas al fichero 'text.txt' existente")
        writeFromTerminalToFile(MODE_APPEND)
    else:
        sys.exit()
else:
    writeFromTerminalToFile(MODE_OVERWRITE)


