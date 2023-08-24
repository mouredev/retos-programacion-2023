import os

def crear_archivo():
    archivo = open("text.txt", "r")
    print("--- Contenido del Archivo ---")
    print(f"\n{archivo.read()}\n")
    archivo = open("text.txt", "a")
    print("(Presiona Enter para Guardar o escribe !q para salir)Escribe a continuacion: ")
    while True:
        contenido = input()
        if contenido == ":!q":
            break
        else:
            archivo.write(f"\n{contenido}")
    archivo.close()

if os.path.isfile("text.txt"):
    respuesta = input("el archivo existe deseas modificarlo(si/no): ")
    if respuesta == "si":
        crear_archivo()
    else:
        archivo = open("text.txt", "w")
        print("Lo que escribas aqui sobreescribira lo que contiene el archivo")
        print("(Presiona Enter para Guardar o escribe !q para salir)Escribe a continuacion: ")
        while True:
            contenido = input()  
            if contenido == ":!q":
                break
            else:  
                archivo.write(contenido)
                archivo.close()
else:
    archivo = open("text.txt", "x")
    crear_archivo()