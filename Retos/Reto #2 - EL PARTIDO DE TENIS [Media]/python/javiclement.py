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

# He hecho el ejercicio para que cada vez que lo ejecutemos inicie un nuevo juego al azar entre el P1 y P2

import random

# Nombre de los jugadores
players = ["P1","P2"]

# A que equivale cada punto
points = {
    0:"Love",
    1:"15",
    2:"30",
    3:"40"
}

# Creamos los contadores de cada jugador
count_p1 = 0
count_p2 = 0

# Mientras no lleguemos al resultado deseado se ejecuta el programa
while True:
    if random.choice(players) == "P1": # selección al azar el ganador del punto
        count_p1 += 1
    else:
        count_p2 += 1
    # condiciones para ganar el partido
    if count_p1 == 4 and count_p2 < 3:
        print("Ha ganado el P1")
        break
    elif count_p2 == 4 and count_p1 < 3:
        print("Ha ganado el P2")
        break
    elif count_p1 == 3 and count_p2 == 3:
        print("Deuce")
        count = 0
        #si hay empate a 3 entonces se decide al mejor de 2 consecutivos
        while count > -2 and count < 2:
            if random.choice(players) == "P1":
                count += 1
            else:
                count -=1

            if count == 0:
                print("Deuce")
            elif count == 1:
                print("Ventaja P1")
            elif count == -1:
                print("Ventaja P2")
            elif count == 2:
                print("Ha ganado el P1")
            elif count == -2:
                print("Ha ganado el P2")
        break
    else:
        print(f'{points[count_p1]} - {points[count_p2]}')
