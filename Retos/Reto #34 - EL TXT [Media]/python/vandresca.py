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

class FileManager:
    __MODE_OVERWRITE = "w"
    __MODE_APPEND = "a"
    __MODE_READING = "r"
    __FILE_NAME = "text.txt"

    def __init__(self, file):
        self.__FILE_NAME = file

    def exists(self):
        return os.path.exists(self.__FILE_NAME)
    
    def readContent(self):
        lines = open(self.__FILE_NAME, self.__MODE_READING).readlines()
        if len(lines) > 0:  print("El contenido actual del fichero es el siguiente: ")
        for line in lines:
            print("\t"+line)

    def newFile(self):
        print(f"El fichero '{self.__FILE_NAME}' no existia y se ha creado. Escribe nuevas lineas.")
        self.__write(self.__MODE_OVERWRITE)

    def deleteContent(self):
        print(f"Contenido de '{self.__FILE_NAME}' eliminado, escribe nuevas líneas")
        self.__write(self.__MODE_OVERWRITE)

    def append(self):
        self.readContent()
        print(f"Añade lineas al fichero '{self.__FILE_NAME}' existente")
        self.__write(self.__MODE_APPEND)
    
    def __write(self, mode):
        file = open(self.__FILE_NAME, mode)
        while True:
            line = input("Introduce una línea o pulsa escape, en ambos casos termina con enter: \n")
            if line.__contains__("\x1b"):
                file.close()
                sys.exit()
            else:
                file.write(line+"\n")

class Terminal:
    def requestOption(self):
        option = ""
        while not re.match("^[1-2]|(\\x1b$)", option):
            print("Elige una opción [1, 2] o escape y pulsa enter:")
            print("  1 - Eliminar contenido")
            print("  2 - Continuar escribiendo")
            option = input()
        return option

    def exit(self):
        sys.exit()



if __name__ == "__main__":
    fileManager = FileManager("text.txt")
    terminal = Terminal()

    if (fileManager.exists()):
        print("El fichero 'text.txt' ya existe.")
        print("¿Deseas eliminar  el contenido o continuar escribiendo?")
        option = terminal.requestOption()
        if option == "1": fileManager.deleteContent() 
        else: fileManager.append() 
    else:
        fileManager.newFile()
