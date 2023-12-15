class TennisMatch:
    """
    Represents a tennis match with scoring and game progression.
    """

    def __init__(self):
        """
        Initializes the TennisMatch instance.
        """
        self.score_p1 = 0
        self.score_p2 = 0
        self.points = ["Love", "15", "30", "40"]
        self.finished = False

    def record_point(self, player):
        """
        Records a point for the given player.

        Args:
        player (str): "P1" for Player 1, "P2" for Player 2.
        """
        if player == "P1":
            self.score_p1 += 1
        elif player == "P2":
            self.score_p2 += 1

    def display_score(self):
        """
        Displays the current score of the tennis match.
        """
        if self.score_p1 >= 3 and self.score_p2 >= 3:
            if not self.finished and abs(self.score_p1 - self.score_p2) <= 1:
                print(
                    "Deuce" if self.score_p1 == self.score_p2
                    else "Advantage P1" if self.score_p1 > self.score_p2
                    else "Advantage P2"
                )
            else:
                self.finished = True
        else:
            print(f"{self.points[self.score_p1]} - {self.points[self.score_p2]}")

    def determine_winner(self):
        """
        Determines and prints the winner of the tennis match.
        """
        if self.score_p1 > self.score_p2:
            print("Player 1 has won the match.")
        elif self.score_p1 < self.score_p2:
            print("Player 2 has won the match.")
        else:
            print("The match ended in a draw.")

# Example sequence of points
sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

# Create a TennisMatch instance
tennis_match = TennisMatch()

# Simulate the tennis match based on the sequence of points
for point in sequence:
    tennis_match.record_point(point)
    tennis_match.display_score()

# Determine and print the winner of the match
tennis_match.determine_winner()
