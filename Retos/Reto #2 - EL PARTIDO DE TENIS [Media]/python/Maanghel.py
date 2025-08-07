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
40 - 40
Deuce
Ventaja P1
Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

from typing import List, Literal

class TenisGame():
    """
    A class to simulate a tennis game given a sequence of points won by each player.

    The score follows standard tennis rules:
    - Love, 15, 30, 40, Deuce, Advantage, and Winner.
    """

    def __init__(self, points: List[Literal["P1", "P2"]]) -> None:
        self._validate_data(points)
        self._play_game(points)

    def _validate_data(self, points_list: List[Literal["P1", "P2"]]) -> None:
        """
        Validates that the points list is a non-empty list containing only 'P1' or 'P2'.

        Args:
            points_list (List[Literal["P1", "P2"]]): List of points.

        Raises:
            TypeError: If the input is not a list.
            ValueError: If the list is empty or contains invalid elements.
        """
        if not isinstance(points_list, list):
            raise TypeError("La entrada debe ser una lista.")
        if not points_list:
            raise ValueError("La lista no puede estar vacia.")
        if not all(point in ["P1", "P2"] for point in points_list):
            raise ValueError("La lista solo puede contener 'P1' o 'P2'.")

    def _print_game_state(self, points_p1: int, points_p2: int) -> None:
        """
        Prints the current score of the game according to tennis rules.

        Args:
            points_p1 (int): Points scored by player 1.
            points_p2 (int): Points scored by player 2.
        """
        score_names = ["Love", "15", "30", "40"]
        if points_p1 >= 3 and points_p2 >= 3:
            if points_p1 == points_p2:
                print("Deuce")
            elif points_p1 == points_p2 + 1:
                print("Ventaja P1")
            elif points_p2 == points_p1 + 1:
                print("Ventaja P2")
        else:
            print(f"{score_names[points_p1]} - {score_names[points_p2]}")

    def _play_game(self, points: List[Literal["P1", "P2"]]) -> None:
        """
        Simulates the game, printing the score after each point
        and announcing the winner.

        Args:
            points (List[Literal["P1", "P2"]]): Sequence of points won.
        """
        points_p1 = 0
        points_p2 = 0

        for point in points:
            if point == "P1":
                points_p1 += 1
            else:
                points_p2 += 1

            if (points_p1 >= 4 or points_p2 >= 4) and abs(points_p1 - points_p2) >= 2:
                print(f"Ha ganado el P{'1' if points_p1 > points_p2 else '2'}")
                break

            self._print_game_state(points_p1, points_p2)


if __name__ == "__main__":
    game = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    first_game = TenisGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
