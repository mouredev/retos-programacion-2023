""" 
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia[P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
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


def tennis_game(points_game):
    POINTS = ["Love", "15", "30", "40", "Ventaja"]
    player1 = 0
    player2 = 0

    # Recorremos el array de puntos del partido
    for point in points_game:
        # Gestionamos los puntos que tienen P1 y P2
        if point == "P1":
            if player2 == 4:
                player2 -= 1
            else:
                if player1 == 3 and player2 != 3:
                    player1 = player1 + 2
                else:
                    player1 += 1
        else:
            if player1 == 4:
                player1 -= 1
            else:
                if player2 == 3 and player1 != 3:
                    player2 = player2 + 2
                else:
                    player2 += 1

        # Mostramos por pantalla el resultado
        if player1 == 3 and player2 == 3:
            print("Deuce")
        elif player1 == 4:
            print("Ventaja P1")
        elif player2 == 4:
            print("Ventaja P2")
        elif player1 == 5:
            print("Ha ganado el P1")
            return
        elif player2 == 5:
            print("Ha ganado el P2")
            return
        else:
            print(POINTS[player1], " - ", POINTS[player2])


points_array_1 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
points_array_2 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2", "P1"]
points_array_3 = ["P1", "P1", "P1", "P1", "P1", "P1", "P1", "P1"]
points_array_4 = ["P1", "P1"]
points_array_5 = ["P1", "P1", "P2", "P2", "P1",
                  "P2", "P1", "P2", "P2", "P1", "P2", "P2"]
tennis_game(points_array_1)
tennis_game(points_array_2)
tennis_game(points_array_3)
tennis_game(points_array_4)
tennis_game(points_array_5)
