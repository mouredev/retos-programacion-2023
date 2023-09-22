'''
/*
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */

'''

from pprint import pprint
import os
from itertools import cycle
import random


L = [['🔳🔳'],
     ['🔳🔲'],
     ['🔳🔲'],
     ['🔳🔲']]

L_90 = [['🔳🔳🔳🔳'],
        ['🔲🔲🔲🔳']]

L_180 = [['🔲🔳'],
         ['🔲🔳'],
         ['🔲🔳'],
         ['🔳🔳']]

L_270 = [['🔳🔲🔲🔲'],
         ['🔳🔳🔳🔳']]




def tamano(pieza: list):
    ancho = len(str(pieza[0])[2:-2])
    alto = len(pieza)
    # pprint(pieza)
    # print(f'{ancho=} // {alto=}')
    return ancho, alto


def creacion_de_fichas():
    fichas = []
    fichas.append(L)
    fichas.append(L_90)
    fichas.append(L_180)
    fichas.append(L_270)
    #random.shuffle(fichas)
    fichas = cycle(fichas)
    return fichas



if __name__ == '__main__':
    # * Ciclo principal
    salida = True
    vertical = 0
    horizontal = 0
    filas = 10
    columnas = 10

    fichas = creacion_de_fichas()
    pieza = next(fichas)
    while salida:
        tablero = ''
        ancho, alto = tamano(pieza)
        posterior = 10 - horizontal - ancho
        #* Construcción del tablero
        for x in range(filas-alto+1):
            if x < vertical:
                tablero = tablero + '🔲' * columnas + '\n'
            elif x == vertical:
                # * Genermos la pieza
                for i in range(alto):
                    tablero = tablero + '🔲' * horizontal + str(pieza[i])[2:-2] + '🔲' * posterior +'\n' # type: ignore
            elif x > vertical:
                tablero = tablero + '🔲' * columnas + '\n'
        os.system('clear')
        print(tablero)
        print(f'PIEZA: {ancho=} x {alto=} || POSICIÓN: {horizontal=}, {vertical=} || {columnas=} || {filas=}')

        salida = False if vertical > 9 else True
        print('"Q" a la izquierda // "W" a la derecha // "E" rotación // "A" bajar // "S" Salir')
        proximo_movimiento = True
        while proximo_movimiento:
            print()

            movimiento = input('¿Próximo movimiento? ')
            if movimiento == "q":
                if horizontal <= 0:
                    horizontal = 0
                    #print('No te puedes salir del tablero por la izquierda')
                else:
                    proximo_movimiento = False
                    horizontal -= 1
            elif movimiento == "w":
                if horizontal + ancho < columnas:
                    proximo_movimiento = False
                    horizontal += 1
                else:
                    horizontal = filas - ancho
                    #print('No te puedes salir del tablero por la derecha')
            elif movimiento == "a":
                if vertical + alto < columnas:
                    vertical += 1
                else:
                    vertical = columnas - alto
                proximo_movimiento = False
            elif movimiento == "e":
                pieza = next(fichas)
                proximo_movimiento = False
            elif movimiento == "s":
                print('Salimos del juego')
                exit()

