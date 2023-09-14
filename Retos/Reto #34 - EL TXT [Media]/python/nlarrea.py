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

import os


def ask_mode() -> str:
    while True:
        print("What do you want to do?")
        print("\tA - keep writing on the existing file")
        print("\tW - remove the content and start writing from the beginning")
        mode = input("Enter your choice (a/w) or Q to exit: ")

        if mode.lower() == "a" or mode.lower() == "w" or mode.lower() == "q":
            return mode


def write_file():
    FILE_PATH = "./text.txt"
    mode = "w"

    if os.path.exists(FILE_PATH):
        mode = ask_mode()

        if mode == "q": return

    with open(FILE_PATH, mode) as f:
        while True:
            user_text = input("Type a line to insert (type 'q' to exit) and press ENTER:\n")
            
            if user_text == "q":
                break

            f.write(f"{user_text}\n")


write_file()