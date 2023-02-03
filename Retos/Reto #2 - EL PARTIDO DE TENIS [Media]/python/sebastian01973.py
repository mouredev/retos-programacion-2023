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


players = ("P1", "P2")
points = ("Love", 15, 30, 40)

countP1 = 0
countP2 = 0


def result(value):
    return points[value]


def rules(player):
    global countP1, countP2
    if player == players[0]:
        countP1 += 1
    if player == players[1]:
        countP2 += 1
    logic(countP1,countP2)
    

def logic(countP1,countP2):
    if countP1 <= 3 and countP2 <= 3:
        if countP2 == 3 or countP1 == 3:
            if countP2 == countP1:
                print("Deuce")
            else:
                print(f"{result(countP1)} - {result(countP2)}")
        else:
            print(f"{result(countP1)} - {result(countP2)}")
    else:
        if countP1 > countP2:
            if (countP1 > countP2 + 1):
                print(f"Ha ganado el {players[0]}")
            else:
                print(f"Ventaja {players[0]}")
        else:
            if (countP2 > countP1 + 1):
                print(f"Ha ganado el {players[1]}")
            else:
                print(f"Ventaja {players[1]}")


def game(sequence):
    for i in sequence:
        rules(i)


if __name__ == '__main__':
    sequence = ("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")
    sequence1 = ("P1", "P1", "P2", "P2", "P1", "P2", "P2", "P2")
    sequence2 = ("P1","P1", "P1","P1")
    game(sequence)