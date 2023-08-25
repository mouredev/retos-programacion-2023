import os
import sys
import signal
import time
def terminar(sig,frame):
    print("\n[!] Saliendo...")

signal.signal(signal.SIGINT,terminar)

def seguir_escribiendo(file):
    while True:
        with open(file,'r',encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            for row in lineas:
                print(row,end="")

            with open(file,'a',encoding="utf-8") as archivo:
                contenido = str(input("\n> "))
                registro = contenido
                archivo.writelines([registro,"\n"])

            continuar = input("¿Deseas seguir escribiendo? (Sí/No): ")

        if  continuar.lower() != "si":
            print("Proceso finalizado.")
            break

def borrar_contenido(file):
    with open(file,'w',encoding="utf-8") as archivo:
        archivo.write("")
    print("[+] Contenido Borrado")
    print("[+] Escriba algo en su archivo: ")
    while True:
        with open(file,'r',encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            for row in lineas:
                print(row,end="")

            with open(file,'a',encoding="utf-8") as archivo:
                contenido = str(input("\n> "))
                registro = contenido
                archivo.writelines([registro,"\n"])

            continuar = input("¿Deseas seguir escribiendo? (Sí/No): ")

        if  continuar.lower() != "si":
            print("Proceso finalizado.")
            break

def menu(file):
    print("[+] Cosas que Puede Hacer con el archivo")
    print("[1]. Seguir Escribiendo")
    print("[2]. Borrar el contenido")
    op = int(input("> "))
 
    match op:
        case 1:
            if os.path.isfile(file):
                seguir_escribiendo(file)
        case 2:
            borrar_contenido(file)
            

def verificar_archivo(file):
    if os.path.isfile(file):
        print("El archivo  existe")
        menu(file)

    else:
        print("El archivo no existe.")
        time.sleep(2)
        print("[+] Procediendo a crearlo")
        with open("text.txt","w") as file:
            pass

if __name__ == '__main__':
    file = str(input("[+] Ingrese la ruta de su archivo: "))
    verificar_archivo(file)
