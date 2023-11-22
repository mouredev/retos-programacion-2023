# /*
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
#  * Desde el 1 al 24 de diciembre.
#  *
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
#  */
import os
import random
import time

participantes = []

def empty_list():
    if len(participantes) <= 0:
        return True

def add_user():
    os.system("cls")
    print("=== AÑADIR USUARIOS ===")
    while True:
        try:
            cantidad = int(input("Cuantos participante te gustaría añadir: "))
            for x in range(cantidad):
                encontrado = False
                user = input("Nombre del participantes a agregar: ")
                if empty_list():
                    participantes.append(user.capitalize())
                else:
                    for z in participantes:
                        if z.lower() == user.lower():
                            print("El participante ya existe!")
                            encontrado = True
                            break 
                    if not encontrado:
                        participantes.append(user.capitalize())
            break
        except:
            print("El valor introducido no es correcto!")
    input("Pulsa una tecla para continuar...")
    menu()

def remove_user():
    os.system("cls")
    print("=== QUITAR USUARIOS ===")
    if empty_list():
        print("No existen usuarios dentro de la lista.")
        input("Pulsa una tecla para continuar...")
        menu()
    else:
        user = input("Que usuario te gustaría eliminar: ")
        encontrado = False
        for x in participantes:
            if user.capitalize() == x.capitalize():
                encontrado = True
        if encontrado:
            participantes.remove(user.capitalize())
            print("El usuario ha sido eliminado!")
        else:
            print("El usuario no se ha encontrado!")
    input("Pulsa una tecla para continuar...")       
    menu()
    
def list_users():
    os.system("cls")
    print("=== LISTA DE PARTICIPANTES ===")
    for i in participantes:
        print(i)
    print("Hay {} participantes en la lista".format(len(participantes)))
    input("Pulsa una tecla para continuar...")
    menu()

def start_giveway():
    os.system("cls")
    print("=== SORTEO ===")
    if empty_list():
        print("¡No hay participantes! ¡El sorteo no se puede realizar!")
        input("Pulsa una tecla para salir....")
        menu()
    else:
        print("El ganador es....")
        for x in range(3,0, -1):
            print(x)
            time.sleep(1)
        winner = random.choice(participantes)
        print("¡{} se lleva el premio! ¡Muchas felicidades!".format(winner))
        participantes.remove(winner) 
    input("Pulsa una tecla para salir....")
    menu()

def showapp(option):
    if option == 1:
        add_user()
    elif option == 2:
        remove_user()
    elif option == 3:
        list_users()
    elif option == 4:
        start_giveway()
    elif option == 5:
        print("¡Que tengas un buen dia!")
        exit()

def menu():
    option = 0
    try:
        while(int(option) not in {1, 2, 3, 4, 5}):
            os.system("cls")
            print("=== MENU CALENDARIO ADVIENTO 2023 ===")
            print("[1] Añadir participante")
            print("[2] Borrar participante")
            print("[3] Listar participante")
            print("[4] Comenzar sorteo")
            print("[5] Salir")
            option = int(input("Introduce tu opción: "))
    except:
        print("¡El valor introducido no es correcto!")
        menu()
    showapp(int(option))

menu()