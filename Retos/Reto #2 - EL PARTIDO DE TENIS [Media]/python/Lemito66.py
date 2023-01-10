""" 
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
"""


def primer_game(lista_de_puntos: list):
    jugadores = {'P1': 0,
                 'P2': 0}
    resultado_P1 = ''
    resultado_P2 = ''
    try:
        if len(lista_de_puntos) > 0:
            for puntos in lista_de_puntos:
                jugadores[puntos.upper()] += 1
                if jugadores['P1'] == 3 and jugadores['P2'] == 3:
                    print('Deuce')
                elif jugadores['P1'] >= 4 or jugadores['P2'] >= 4:
                    if jugadores['P1'] == jugadores['P2']:
                        print('Deuce')
                    elif jugadores['P1'] > jugadores['P2']:
                        if jugadores['P1'] - jugadores['P2'] == 1:
                            print('Ventaja P1')
                        else:
                            print(f'Game P1')
                    else:
                        if jugadores['P2'] - jugadores['P1'] == 1:
                            print('Ventaja P2')
                        else:
                            print(f'Game P2')
                else:
                    if jugadores['P1'] == 0:
                        resultado_P1 = 'Love'
                    elif jugadores['P1'] == 1:
                        resultado_P1 = '15'
                    elif jugadores['P1'] == 2:
                        resultado_P1 = '30'
                    else:
                        resultado_P1 = ('40')
                    if jugadores['P2'] == 0:
                        resultado_P2 = 'Love'
                    elif jugadores['P2'] == 1:
                        resultado_P2 = '15'
                    elif jugadores['P2'] == 2:
                        resultado_P2 = '30'
                    else:
                        resultado_P2 = ('40')
                    print(f'{resultado_P1}-{resultado_P2}')
        else:
            print('La lista esta vacia')
    except:
        print(f'Error, el valor no es el correcto')


primer_game(["P1", "P2", "P1", "P2", "P1", "P2",
            "P1", "P2", "P1", "P2", "P2", "P2"])
