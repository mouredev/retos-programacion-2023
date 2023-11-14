import os

file_name = "text.txt"

if os.path.exists(file_name):

    print("El fichero ya existe. ¿Qué quieres hacer?")
    text = input("Pulsa \"enter\" para continuar o escribe \"delete\" para eliminar: ")

    if text == "delete":
        os.remove(file_name)
    else:
        file = open(file_name, "r")
        print(file.read())

file = open(file_name, "a")

while True:

    text = input("Escribe el texto a añadir o \"exit\" para salir: ")

    if text == "exit":
        break

    file.write(text + "\n")
    file.flush()

file.close()

