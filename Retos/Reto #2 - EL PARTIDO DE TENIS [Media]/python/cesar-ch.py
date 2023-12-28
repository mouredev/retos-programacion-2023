#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  *
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.


def play_tennis(points):
    p1 = 0
    p2 = 0
    scores = {0: "Love", 1: "15", 2: "30", 3: "40"}
    winner = False
    final = len(points)
    for i in range(final):
        if (winner == False):
            p1 += 1 if points[i] == 'P1' else 0
            p2 += 1 if points[i] == 'P2' else 0
            if (p1 >= 3 and p2 >= 3 and p1 == p2):
                print('Deuce')
            elif (p1 < 4 and p2 < 4):
                print(f'{scores[p1]} - {scores[p2]}')
            elif (p1 == 4 or p2 == 4):
                print('Ventaja P1') if p1 == 4 else print('Ventaja P2')
            elif (p1 == 5 or p2 == 5):
                winner = True
                print('Ha ganado P1') if p1 == 5 else print(
                    'Ha ganado el P2')

        if (winner == False and final == i + 1):
            print('Los puntos jugados no son correctos')
            break
        if (winner == True and final != i + 1):
            print('Los puntos jugados no son correctos')
            break


# play_tennis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
# play_tennis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2", "P1"])
# play_tennis(["P1", "P1", "P1", "P1", "P1", "P1"])
# play_tennis(["P1", "P1"])
