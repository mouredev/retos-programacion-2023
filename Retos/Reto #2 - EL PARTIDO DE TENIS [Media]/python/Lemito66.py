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


def juego_del_tenis(lista_de_puntos: list):
    jugadores = {'P1': 0,
                 'P2': 0}
    marcador = ['Love', '15', '30', '40']
    try:
        if len(lista_de_puntos) > 0:
            for puntos in lista_de_puntos:
                jugadores[puntos.upper()] += 1
                impresion_de_marcador(jugadores, marcador)
        else:
            print('La lista esta vacia')
    except:
        print(f'Error, el valor no es el correcto')

def impresion_de_marcador(jugadores, marcador):
    if jugadores['P1'] == 3 and jugadores['P2'] == 3:
        print('Deuce')
    elif jugadores['P1'] >= 4 or jugadores['P2'] >= 4:
        diferencia_de_puntos = jugadores['P1']-jugadores['P2']
        if diferencia_de_puntos == 0:
            print('Deuce')
        elif diferencia_de_puntos == 1:
            print('Ventaja P1')
        elif diferencia_de_puntos == -1:
            print(f'Ventaja P2')
        elif diferencia_de_puntos >=2:
            print(f'Game P1')
        else:
            print(f'Game P2')
    else:
        print(f'{marcador[jugadores["P1"]]}-{marcador[jugadores["P2"]]}')


juego_del_tenis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])
