class TenisGame:
    """This class represents a tennis game between the players P1 and P2."""

    def __init__(self) -> None:
        """This method initializes an instance with the default attributes"""
        self.game_status: bool = False
        self.game_score: str = None
        self.player1_name: str = None
        self.player1_score: int = None
        self.player2_name: str = None
        self.player2_score: int = None

    def identify_players(self, sequence: list) -> list:
        """This method identifies the players in the game.

        Args:
            sequence (list): sequence of player scores

        Returns:
            list: players in the game
        """
        self.sequence = sequence
        self.players = list(set(self.sequence))
        return self.players

    def validate_players(self, players: list) -> bool:
        """This method validates that the players in the sequence are P1 and P2

        Args:
            players (list): players identified by the identify_players method

        Returns:
            bool: True is returned if the players identified are P1 and P2. otherwise, False is returned.
        """
        if len(players) == 2 and "P1" in players and "P2" in players:
            self.player1_name, self.player2_name = "P1", "P2"
            return True
        return False

    def start_game(self) -> None:
        """This method initializes the player scores and the game status."""
        self.game_status = True
        self.player1_score = 0
        self.player2_score = 0

    def update_game_score(self, scorer: str) -> None:
        """This method updates the player scores and the game score.

        Args:
            scorer (str): player who scored point
        """
        self.POINTS = ["Love", 15, 30, 40]

        self.player1_score += 1 if scorer == self.player1_name else 0
        self.player2_score += 1 if scorer == self.player2_name else 0

        if self.player1_score >= 3 and self.player2_score >= 3:
            if self.game_status and abs(self.player1_score - self.player2_score) <= 1:
                self.game_score = (
                    "Deuce"
                    if self.player1_score == self.player2_score
                    else "Ventaja P1"
                    if self.player1_score > self.player2_score
                    else "Ventaja P2"
                )
            else:
                self.game_status = False
                self.game_score = (
                    "Ha ganado el P1"
                    if self.player1_score > self.player2_score
                    else "Ha ganado el P2"
                )
        else:
            if self.player1_score < 4 and self.player2_score < 4:
                self.game_score = f"{self.POINTS[self.player1_score]} - {self.POINTS[self.player2_score]}"
            else:
                self.game_status = False


if __name__ == "__main__":
    sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    tenis_game = TenisGame()
    players = tenis_game.identify_players(sequence)

    if tenis_game.validate_players(players):
        tenis_game.start_game()
        for scorer in sequence:
            tenis_game.update_game_score(scorer)
            print(tenis_game.game_score)
    else:
        print(
            "No fue posible iniciar el juego. Sólo pueden jugar dos jugadores: P1 y P2."
        )
