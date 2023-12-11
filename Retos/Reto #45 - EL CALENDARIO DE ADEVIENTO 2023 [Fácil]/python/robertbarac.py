import os
from time import sleep
from random import choice

lista_regalos = [i for i in range(1,25)]
lista_participantes = []

def menu():
    mensaje_input = """
    Programa navideño aDEViento
    Seleccione una de las opciones:
    1. Añadir participante
    2. Eliminar participante
    3. Mostrar participantes
    4. Lanzar el sorteo
    5. Salir
    """
    print(mensaje_input)
    opcion = int(input())
    while True:
        if opcion == 1:
            os.system("cls")
            agregar_participante()
        elif opcion == 2:
            eliminar_participante()
        elif opcion == 3:
            os.system("cls")
            mostrar_participante()
        elif opcion == 4:
            os.system("cls")
            lanzar_sorteo()
        elif opcion == 5:
            os.system("cls")
            salir()
        else:
            print("Opción errada")
    

def agregar_participante():
    nombre = input("Ingresa el nombre del participante: ")
    nombre = nombre.title()
    if nombre in lista_participantes:
        print("Este participante está agregado previamente")
        sleep(1)
        os.system("cls")
        menu()
    else:
        lista_participantes.append(nombre)
        print("Participante agregado...")
        sleep(1)
        os.system("cls")
        menu()

def eliminar_participante():
    nombre = input("Escriba el nombre del participante a eliminar: ").title()
    if nombre in lista_participantes:
        indice = lista_participantes.index(nombre)
        print(f"Eliminando a {nombre}...")
        sleep(1)
        lista_participantes.remove(nombre)
        print(f"Ha sido eliminado {nombre}")
        sleep(1)
        os.system("cls")
        menu()
    else:
        print(f"{nombre} no está en los participantes")
        sleep(1)
        os.system("cls")
        menu()

def mostrar_participante():
    print("Éstos son los participantes:")
    for i in range(len(lista_participantes)):
        print(lista_participantes[i])
    sleep(1)
    os.system("cls")
    menu()

def lanzar_sorteo():
    nombre = choice(lista_participantes)
    regalo = choice(lista_regalos)
    print(f"Hoy ganó {nombre} el regalo {regalo}")
    sleep(2)
    lista_participantes.remove(nombre)
    os.system("cls")
    menu()

def salir():
    print("Saliendo de aplicación")
    print("Adiós")
    exit()

if __name__ == "__main__":
    menu()
