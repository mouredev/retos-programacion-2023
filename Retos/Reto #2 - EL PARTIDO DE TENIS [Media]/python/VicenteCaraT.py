import unittest
from io import StringIO
from contextlib import redirect_stdout

class Player:
    def __init__(self, name:str, score = 0):
        self.name = name
        self.score = score
    
    def __repr__(self):
        return f"---{self.name}---\nscore: {self.score}"

class Match:
    def __init__(self, player1: Player, player2: Player, sets: list[str]):
        self.player1 = player1
        self.player2 = player2
        self.points = ["Love", "15", "30", "40"]
        self.sets = sets
        self.finished = False

    def match_main(self):
        for point in self.sets:
            if point == "P1":
                self.player1.score += 1
            elif point == "P2":
                self.player2.score += 1
            self.match_logic()
        self.winner()
                
    def match_logic(self):
        if self.player1.score >= 3 and self.player2.score >= 3:
            if not self.finished and abs(self.player1.score - self.player2.score) <= 1:
                print(
                    "Deuce" if self.player1.score == self.player2.score
                    else f"Advantage {self.player1.name}" if self.player1.score > self.player2.score
                    else f"Advantage {self.player2.name}"
                )
            else:
                self.finished = True
        else:
            print(f"{self.points[self.player1.score]} - {self.points[self.player2.score]}")

    def winner(self):
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} has won the match")
        elif self.player1.score < self.player2.score:
            print(f"{self.player2.name} has won the match")

class TestTennis(unittest.TestCase):
    def test_p1_win(self):
        player1 = Player("P1")
        player2 = Player("P2")
        sets = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
        match = Match(player1, player2, sets)
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            match.match_main()
        printed_output = captured_output.getvalue()
        expected_output = """15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Advantage P1
P1 has won the match
"""
        self.assertEqual(printed_output, expected_output)

    def test_p2_win(self):
        player1 = Player("P1")
        player2 = Player("P2")
        sets = ["P1", "P1", "P2", "P2", "P1", "P2", "P2", "P2"]
        match = Match(player1, player2, sets)
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            match.match_main()
        printed_output = captured_output.getvalue()
        expected_output = """15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Advantage P2
P2 has won the match
"""
        self.assertEqual(printed_output, expected_output)

if __name__ == "__main__":
    unittest.main()