'''
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
'''

def match(points: list):
    scores = ['Love','15','30','40']
    p1,p2 = 0,0

    for point in points:
        if point == 'P1':
            p1 += 1

        if point == 'P2':
            p2 += 1

        deuce = p1 == 3 and p2 == 3

        advantage_p1 = p1 >= 4 and p1>p2 

        advantage_p2 = p2 >= 4 and p2>p1

        p1_winner = p1 >= 4 and p1-p2 >=2

        p2_winner = p2 >= 4 and p2-p1 >=2


        if deuce:
            print('Deuce')

        elif p1_winner:
            print('Ha ganado el P1')
            break

        elif p2_winner:
            print('Ha ganado el P2')
            break

        elif advantage_p1:
            print('Ventaja P1')   

        elif advantage_p2:
            print('Ventaja P2')  


        else:
            print(f'{scores[p1]} - {scores[p2]}')



if __name__== "__main__":
    points1 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    points2 = ['P2','P1','P1','P2','P2','P1','P2','P2']
    match(points1)
    print('\nNew match\n')
    match(points2)
