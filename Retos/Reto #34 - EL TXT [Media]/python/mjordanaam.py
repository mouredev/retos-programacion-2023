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

FILENAME = "text.txt"

exists = False

# Check if file exists
if FILENAME in os.listdir():
    exists = True

if exists:
    print("File already exists.")
    option = input("Append/Erase ? a/e\n")

    if option == 'a':
        file = open(FILENAME, "r")
        print(file.read())
        file.close()
    elif option == 'e':
        os.remove(FILENAME)

file = open(FILENAME, "a")

while True:
    file = open(FILENAME, "a")
    text = input('Your new line: or  enter (quit)\n')

    if text == 'quit':
        file = open(FILENAME, "r")
        print(file.read())
        break

    file.write(f"{text}\n")
    file.close()
