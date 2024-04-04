#!/usr/bin/python3

"""
/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
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

from time import sleep

LONGITUD_PISTA = 18


def crear_pista(longitud, numero_arboles):
    pista = longitud * '_'
    choices = random.choices(range(1, longitud - 1), k=numero_arboles)
    print(choices)
    # pista[-1] = '🏁'
    pista = replace_string_index(pista, -1, '🏁')
    for item in choices:
        # pista[item] = '🌲'
        pista = replace_string_index(pista, item, '🌲')
    return pista


def colocar_auto(pista, auto_char, posicion):
    pista_salida = pista
    if pista_salida[posicion] == '🌲':
        # pista_salida[posicion] = '💥'
        pista_salida = replace_string_index(pista_salida, posicion, '💥')
    else:
        # pista_salida[posicion] = auto_char
        pista_salida = replace_string_index(pista_salida, posicion, auto_char)
    return pista_salida


def mostrar_pista(pista):
    print(pista)


def replace_string_index(string, index, char):
    s = list(string)
    s[index] = char
    return "".join(s)


def main():

    # -------------------------------------------------------------------------

    # crear las pistas 1
    numero_arboles_1 = random.randint(1,3)
    pista_1 = crear_pista(LONGITUD_PISTA, numero_arboles_1)

    # crear las pistas 2
    numero_arboles_2 = random.randint(1,3)
    pista_2 = crear_pista(LONGITUD_PISTA, numero_arboles_2)

    # -------------------------------------------------------------------------

    # variables de control del bucle
    ganador_1 = False
    ganador_2 = False

    # posicones de los autos
    posicion_auto_1 = 0
    posicion_auto_2 = 0

    choque_1 = False
    choque_2 = False

    while True: # not ganador_1 and not ganador_2:

        # colocar autos
        pista_salida_1 = colocar_auto(pista_1, "🚙", posicion_auto_1)
        pista_salida_2 = colocar_auto(pista_2, "🚗", posicion_auto_2)

        # mostrar pista
        mostrar_pista(pista_salida_1)
        mostrar_pista(pista_salida_2)
        print()

        if ganador_1 or ganador_2:
            break


        # calcular avances

        if not choque_1:
            avance_1 = random.randint(1,3)
            posicion_auto_1 += avance_1

            if posicion_auto_1 >= LONGITUD_PISTA - 1:
                ganador_1 = True
                posicion_auto_1 = LONGITUD_PISTA - 1

            if pista_1[posicion_auto_1] == '🌲':
                choque_1 = True
        else:
            choque_1 = False

        if not choque_2:
            avance_2 = random.randint(1,3)
            posicion_auto_2 += avance_2

            if posicion_auto_2 >= LONGITUD_PISTA - 1:
                ganador_2 = True
                posicion_auto_2 = LONGITUD_PISTA - 1

            if pista_2[posicion_auto_2] == '🌲':
                choque_2 = True
        else:
            choque_2 = False


        # delay
        sleep(1)

    if ganador_1 and ganador_2:
        print("EMPATE")
    elif ganador_1:
        print("HA GANADO 1")
    elif ganador_2:
        print("HA GANADO 2")


if __name__ == '__main__':
    main()




