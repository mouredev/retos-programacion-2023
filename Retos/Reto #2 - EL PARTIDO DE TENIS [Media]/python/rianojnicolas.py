"""
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
"""

def pointsCounter(Sequence):
    puntaje = {'P1': 0, 'P2': 0}
    for element in Sequence:
        if (element == 'P1'):
            puntaje['P1'] = puntaje['P1'] + 15
        elif (element == 'P2'):
            puntaje['P2'] = puntaje['P2'] + 15
        
        if (puntaje['P1'] == 45):
            puntaje['P1'] = 40
        elif (puntaje['P2'] == 45):
            puntaje['P2'] = 40
        
        # Imprimir puntaje
        if (puntaje['P2'] == 0 and puntaje['P1'] > 40):
            print('Ha ganado el P1')
        elif (puntaje['P1'] == 0 and puntaje['P2'] > 40):
            print('Ha ganado el P2')
        elif (puntaje['P1'] == 0):
            p2 = puntaje.get('P2')
            print(f'Love - {p2}')
        elif (puntaje['P2'] == 0):
            p1 = puntaje.get('P1')
            print(f'{p1} - Love')
        elif ((puntaje['P1'] >= 40 or puntaje['P2'] >= 40) and (puntaje['P1'] == puntaje['P2'])):
            print('Deuce')
        elif ((puntaje['P2']+30 == puntaje['P1']) or (puntaje['P2']+25 == puntaje['P1'])):
            print('Ha ganado el P1')
        elif ((puntaje['P1']+30 == puntaje['P2']) or (puntaje['P1']+25 == puntaje['P2'])):
            print('Ha ganado el P2')
        elif (puntaje['P1'] >= 55 and puntaje['P1'] > puntaje['P2']):
            print('Ventaja P1')
        elif (puntaje['P2'] >= 55 and puntaje['P2'] > puntaje['P1']):
            print('Ventaja P2')
        else:
            p1 = puntaje.get('P1')
            p2 = puntaje.get('P2')
            print(f'{p1} - {p2}')


def run():
    # test1
    print('TEST-1')
    pointsCounter(['P1','P1','P1','P1'])

    # test2
    print('TEST-2')
    pointsCounter(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])

    # test3
    print('TEST-3')
    pointsCounter(["P1", "P2", "P1", "P2", "P1", "P1"])

    # test4
    print('TEST-4')
    pointsCounter(["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P1"])

     # test5
    print('TEST-5')
    pointsCounter(["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])


if __name__ == '__main__':
    run()