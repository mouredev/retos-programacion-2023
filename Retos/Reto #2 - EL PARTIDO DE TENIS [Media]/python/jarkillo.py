'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
 '''


import os
import random


def tenis(secuencia):

    puntuacion = {
        '0': 'Love',
        '1': '15',
        '2': '30',
        '3': '40'
    }

    p1 = 0
    p2 = 0

    for punto in secuencia:

        if punto == 'P1':
            p1 += 1
        elif punto == 'P2':
            p2 += 1
        else:
            print('Error en la secuencia')
            return

        if p1 == 4 and p2 == 4:
            print('Deuce')
            empate = True

        if p1 == 4 or p2 == 4:
            if empate == False:
                print('Ha ganado el P1' if p1 == 4 else 'Ha ganado el P2')
                return
            else:
                print('Ventaja P1' if p1 == 4 else 'Ventaja P2')
                p1 -= 1
                p2 -= 1
                return

        else:
            print(puntuacion[str(p1)] + ' - ' + puntuacion[str(p2)])
            empate = False
    if p1 < 4 and p2 < 4:
        print('Fin del tiempo')
        print('Ha ganado el P1' if p1 > p2 else 'Ha ganado el P2')
        return

# Metemos secuencias Random


secuencia = []
for i in range(15):
    secuencia.append(random.choice(['P1', 'P2']))

os.system('PAUSE')
print(secuencia)
os.system('PAUSE')
tenis(secuencia)
