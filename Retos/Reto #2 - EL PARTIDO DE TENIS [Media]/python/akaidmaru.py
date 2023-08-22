'''
* Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
* El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
* gane cada punto del juego.
*
* - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
* - Ante la secuencia[P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
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
'''

def tennis_match(sequence):

    points = ['Love', '15', '30', '40']

    count_p1 = 0
    count_p2 = 0
    finished = False

    for element in sequence:
        if element == 'P1':
            count_p1 += 1
        elif element == 'P2':
            count_p2 += 1
            
        if count_p1 >= 3 and count_p2 >= 3:
            if not finished and abs(count_p1 - count_p2) <= 1:
                if count_p1 == count_p2:
                    print('Deuce')
                elif count_p1 > count_p2:
                    print('Advantage P1')
                elif count_p2 > count_p1:
                    print('Advantage P2')
            else:
                finished = True
        else:
            if count_p1 < 4 and count_p2 < 4:
                print(f'{points[count_p1]} - {points[count_p2]}')
            else:
                finished = True

    if count_p1 > count_p2:
        return 'Player 1 has won!'
    elif count_p1 < count_p2:
        return 'Player 2 has won!'
