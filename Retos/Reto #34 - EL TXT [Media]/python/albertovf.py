import os

file_name = "pruebas.txt"

if os.path.exists(file_name):
    print("Fichero existente")
    text = input("Escribe <enter> para continuar. Escribe <delete> para sobreescribir: ")
    os.remove(file_name) if (text == "delete") else print(open(file_name, "r").read())

file = open(file_name, "a")

while True:
    text = input("Escribe el texto. Escribe <exit> para salir: ")
    if text == "exit":
        break

    file.write(f'{text}\n')
    file.flush()

file.close()
