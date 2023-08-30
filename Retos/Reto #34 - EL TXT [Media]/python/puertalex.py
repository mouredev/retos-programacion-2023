import os

path = "text.txt"

if os.path.exists(path):
    print("El archivo ya existe, que desea hacer:")
    message = input("Presiona \"enter\" para continuar editando o escribe \"delete\" para eliminar el archivo: ")
    if message == "delete":
        os.remove(path)
    else:
        print(open(path).read())

file = open(path,"a")

while True:
    message = input("Escribe el texto que quieres agregar o escribe \"exit\" para salir: ")
    if message == "exit":
        break
    file.write(message + "\n")
    file.flush()

file.close()
