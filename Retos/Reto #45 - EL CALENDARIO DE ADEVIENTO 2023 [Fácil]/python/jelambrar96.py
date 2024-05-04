#!/usr/bin/python3

"""
# Reto #45: El calendario de aDEViento 2023
/*
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
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import random


message_input_1 = """
Ingrese una opcion:
1. Añadir partipante
2. Borrar participante
3. Mostrar todos los participantes
4. Hacer un sorteo
5. Salir

"""


def main():

    participantes = []    

    while True:

        str_input = input(message_input_1)
        if not str_input in ('1', '2', '3', '4', '5'):
            print("ERROR. opcion invalida: ")
            print()
            continue

        if str_input == '1':
            nombre_participante = input("Ingrese el nombre del participante a agregar: ").upper()
            if not nombre_participante in participantes and len(nombre_participante) > 0:
                participantes.append(nombre_participante)
                print(f"El participante '{nombre_participante}' ha sido agregado exitosamente. ")
            else:
                print(f"No se puso agregar al participante '{nombre_participante}' porque ya existe.")
            print() 

        if str_input =='2':
            nombre_participante = input("Ingrese el nombre del participante a borrar: ").upper()
            if not nombre_participante in participantes:
                print(f"No se puso eliminar al participante '{nombre_participante}' porque NO existe.")
            else:
                index_participante = participantes.index(nombre_participante)
                nombre_participante_eliminado = participantes.pop(index)
                print(f"Se ha eliminado el participante '{nombre_participante}'")
            print()

        if str_input =='3':
            print("Etos son los participantes")
            for i, item in enumerate(participantes):
                print(i+1, item)
            print(f"En total son {len(participantes)} participantes")

        if str_input == '4':
            print("Has elegido realizar un sorteo")
            participante_ganador = random.choice(participantes)
            print(f"el participante ganador es {participante_ganador}")
            print("Felicidades!!!!")
            participantes = []

        if str_input == '5':
            print("Has elegido la opcion salir")
            break



if __name__ == '__main__':
    main()

            