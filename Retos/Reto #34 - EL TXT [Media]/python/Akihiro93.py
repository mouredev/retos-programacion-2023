import os


def Write(path):
    with open(path, "w+") as file:
        while True:
            text = input("Que quiere escribir, ESC para detener: ")
            if text == "ESC":
                break
            file.write(text + "\n")

def New_write(path):
    with open(path, "+a") as file:
        content = file.readlines()
        print(content)
        while True:
            text = input("Que quiere escribir, ESC para detener: ")
            if text == "ESC":
                break
            file.write(text + "\n")

path = "./test.txt"

file = open(path, "+r")
rd = file.readline
file.close()

if rd != "":
    print("El archivo tiene contenido, ¿Quiere borrarlo?, enter para confirmar")
    try:
        Int = input()
    except:
        Write(path)
    else:
        New_write(path)
else:
    Write(path)
