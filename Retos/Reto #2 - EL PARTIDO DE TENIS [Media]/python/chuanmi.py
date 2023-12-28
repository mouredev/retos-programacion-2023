"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.
- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""


def partido():
    player1 = 0
    player2 = 0
    winner = ""

    while winner == "":
        live_point = point_winner()
        if live_point == "P1":
            player1 += 1
        elif live_point == "P2":
            player2 += 1
        winner = live_score(player1, player2)
        print(winner)


def point_winner():
    point = input("El punto actual lo gana...: ").upper()
    if point != "P1" and point != "P2":
        print("El ganador del punto tiene que ser P1 o P2")
    elif point == "P1" or point == "P2":
        return point


def live_score(player1, player2):
    scores = ["Love", "15", "30", "40"]

    if player1 == 3 and player2 == 3:
        print("Deuce")
    elif player1 >= 4 or player2 >= 4:
        resto = player1 - player2
        if resto == 0:
            print("Deuce")
        elif resto == 1:
            print("Ventaja P1")
        elif resto == -1:
            print("Ventaja P2")
        elif resto >= 2:
            print("Ha ganado P1")
            return "P1"
        else:
            print("Ha ganado P2")
            return "P2"
    else:
        print(f"{scores[player1]} - {scores[player2]}")
    return ""


partido()
