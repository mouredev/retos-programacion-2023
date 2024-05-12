"""
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.

 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"], el programa mostraría lo siguiente:
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


def translate_score(score):
    if score == 0:
        return "Love"
    elif score == 1:
        return "15"
    elif score == 2:
        return "30"
    elif score == 3:
        return "40"


def determine_winner(score_P1, score_P2):
    if score_P1 >= 4 and score_P1 - score_P2 >= 2:
        return "P1"
    elif score_P2 >= 4 and score_P2 - score_P1 >= 2:
        return "P2"
    else:
        return None


def tennis_game(sequence):
    score_P1 = 0
    score_P2 = 0

    for point in sequence:
        if point == "P1":
            score_P1 += 1
        elif point == "P2":
            score_P2 += 1

        if score_P1 >= 3 and score_P2 >= 3:
            if score_P1 == score_P2:
                print("Deuce")
            elif score_P1 > score_P2:
                print("Ventaja P1")
            else:
                print("Ventaja P2")
        else:
            print(f"{translate_score(score_P1)} - {translate_score(score_P2)}")

        winner = determine_winner(score_P1, score_P2)
        if winner:
            print(f"Ha ganado el {winner}")
            return


sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
tennis_game(sequence)
