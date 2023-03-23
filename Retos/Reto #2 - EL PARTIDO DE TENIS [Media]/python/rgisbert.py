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

from enum import Enum


class Player(Enum):
    P1 = 1
    P2 = 2


def game(points: list):
    players_points = {
        Player.P1: 0,
        Player.P2: 0
    }
    game_finished = False
    game_structure = ("Love", "15", "30", "40")

    for pointFor in points:
        players_points[pointFor] += 1

        if players_points[Player.P1] > 2 and players_points[Player.P2] > 2:
            if not game_finished and abs(players_points[Player.P1] - players_points[Player.P2]) < 2:
                if (players_points[Player.P1] == players_points[Player.P2]):
                    print("Deuce")
                else:
                    print(
                        f"Ventaja {'P1' if players_points[Player.P1] > players_points[Player.P2] else 'P2'}")
            else:
                game_finished = True
                break
        else:
            if players_points[Player.P1] < 4 or players_points[Player.P2] < 4:
                print(
                    f"{game_structure[players_points[Player.P1]]} - {game_structure[players_points[Player.P2]]}")
            else:
                game_finished = True
                break

    if game_finished:
        print(
            f"Ha ganado el {'P1' if players_points[Player.P1] > players_points[Player.P2] else 'P2'}")
    else:
        print("Ha habido un error al pasar los puntos")


if __name__ == "__main__":
    # points = [Player.P1, Player.P1, Player.P2, Player.P2,
    #   Player.P1, Player.P2, Player.P1, Player.P1, Player.P2, Player.P2, Player.P2, Player.P2]
    points = [Player.P1, Player.P1, Player.P2,
              Player.P1, Player.P2, Player.P2, Player.P2, Player.P1, Player.P2, Player.P2]
    game(points)
