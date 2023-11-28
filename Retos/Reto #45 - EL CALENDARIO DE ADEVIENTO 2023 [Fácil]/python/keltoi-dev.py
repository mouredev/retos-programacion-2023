"""
* ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
"""

import random
import os

condicion = ""
particpantes = []

def menu():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    opciones = "1234"
    print("*** MENU ***")
    print("1.- Añadir un participante")
    print("2.- Eliminar un participante")
    print("3.- Listar los participantes")
    print("4.- Sortear premio")
    print("0.- Salir de la aplicacion")
    seleccion = input("\nSelecciones una opcion: ")
    global condicion
    if seleccion in opciones:
        condicion = True
    else:
        condicion = False

    return seleccion

def alta():
    global particpantes
    ingresante = input("Ingrese un participante: ")
    if ingresante != "":
        if ingresante.capitalize() in particpantes:
            print("El dato ingresado ya existe.")
            alta()
        else:
            particpantes.append(ingresante.capitalize())

    continuar = input("Desea ingresar otro participante? (s/n) ")
    if continuar.lower() == "s":
        alta()

def baja():
    ingresante = input("Ingrese el participante a eliminar: ")
    if ingresante != "":
        if ingresante.capitalize() in particpantes:
            particpantes.remove(ingresante.capitalize())
        else:
            print("El participante no existe:")
            baja()

    continuar = input("Desea eliminar otro participante? (s/n) ")
    if continuar.lower() == "s":
        baja()

def mostrar():
    print("Listado de participantes")
    for i in particpantes:
        print(i)
    continuar = input("Presione una tecla para continuar")


def sorteo():
    print("Sorteo de premio")
    if not particpantes:
        print("No hay perticipantes para realizar el sorteo")
    else:
        ganador = random.choice(particpantes)
        print(f"El ganador es {ganador}")
        particpantes.remove(ganador)
    continuar = input("Presione una tecla para continuar")

print("Bienvenido!!!")
seleccion = menu()
while condicion:
    if seleccion == "1":
        alta()
    elif seleccion == "2":
        baja()
    elif seleccion == "3":
        mostrar()
    else:
        sorteo()
    seleccion = menu()