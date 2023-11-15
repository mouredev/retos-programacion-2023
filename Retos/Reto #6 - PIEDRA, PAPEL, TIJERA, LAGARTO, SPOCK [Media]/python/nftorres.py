"""This script shows the solution to the exercise "Reto #6: PIEDRA, PAPEL O TIJERA" from Brais Moure's official website."""

# Defining the weak opponents of each piece.


class Game:
    """This class represents a game of 'Piedra, Papel, Tijera, Lagarto, Spock'
    """

    def __init__(self, duels: list) -> None:
        """This method initializes the players' scores and establishes the duels and weak opponents of each player.

        Args:
            duels (list): duels played during the game.
        """
        self.duels = duels
        self.p1_score = 0
        self.p2_score = 0

        self.weak_opponents = {
            "piedra": ["tijera", "lagarto"],
            "papel": ["piedra", "spock"],
            "tijera": ["papel", "lagarto"],
            "lagarto": ["papel", "spock"],
            "spock": ["tijera", "piedra"],
        }

    def __check_pieces(self, piece1: str, piece2: str) -> bool:
        """This method checks if the pieces played are valid in the game.

        Args:
            piece1 (str): piece played by player1
            piece2 (str): piece played by player2
        Returns:
            bool: True is returned if the pieces played are valid, othercase, False if returned
        """
        self.piece1 = piece1
        self.piece2 = piece2
        return True if (self.piece1 in self.weak_opponents) and (self.piece2 in self.weak_opponents) else False

    def update_scores(self) -> None:
        """'This method updates the players' scores during the game.

        Returns:
            None: When everything works as planned, the scores are updated    correctly.

            Exception: an exception is thrown if one or both of the pieces are  invalid in the game.
        """
        try:
            for duel in self.duels:
                self.piece1 = duel[0].lower()
                self.piece2 = duel[1].lower()
                if self.__check_pieces(self.piece1, self.piece2):
                    self.p1_score += 1 if self.piece2 in self.weak_opponents[self.piece1] else 0
                    self.p2_score += 1 if self.piece1 in self.weak_opponents[self.piece2] else 0
                else:
                    raise Exception(
                        "Sólo se puede jugar con 'Piedra', 'Papel', 'Tijera', 'Lagarto' o 'Spock'")
        except Exception as e:
            return e

    def say_winner(self) -> str:
        """This method determines the winner of the game.

        Returns:
            str: The winner of the game.
        """
        if self.p1_score == self.p2_score:
            return "Tie!"
        elif self.p1_score > self.p2_score:
            return "Player 1 has won!"
        else:
            return "Player 2 has won!"


if __name__ == "__main__":
    duels = [
        ("Piedra", "Papel"),
        ("Tijera", "Papel"),
        ("Piedra", "Tijera"),
        ("Piedra", "Tijera"),
    ]
    # Creating the game
    game = Game(duels)
    # Reading the duels and updating the scores
    game.update_scores()
    # Determining the winner
    winner = game.say_winner()
    print("Result:", winner)
