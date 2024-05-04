#!/usr/bin/python3

"""
# Reto #34: El TXT
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

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import os



class FicheroTXT:

    def __init__(self, archivo):
        self._archivo = archivo
        pass

    def mostrar_contenido(self,):
        with open(self._archivo, "r") as f:
            for line in f.readlines():
                print(line, end="")

    def modificar_contenido(self, append=True):
        if append:
            self.mostrar_contenido()
        mode = "a" if append else "w"
        nueva_linea = input()
        with open(self._archivo, mode) as f:
            f.write(nueva_linea + "\n")

if __name__ == '__main__':
    ruta = input("ingrese la ruta del archivo: ").strip()
    append = False
    if os.path.isfile(ruta):
        print("el archivo existe, desea abirlo en modo append? [S/n]")
        mode_opcion = input()
        if mode_opcion.lower() in ["no", "n"]:
            append = False
        else:
            append = True
    print("Abriendo el archivo: Modo append ", append)
    print()
    print()
    ftxt = FicheroTXT(ruta)
    ftxt.modificar_contenido(append=append)






