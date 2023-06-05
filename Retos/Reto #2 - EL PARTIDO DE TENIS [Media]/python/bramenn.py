
from typing import List

class Player:
    score: int
    name: str

    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0

class TennisMatch:

    player_1: Player
    player_2: Player

    history_sets: List[str]
    winner: Player

    tennis_dict = {
        0: "Love",
        1: "15",
        2: "30",
        3: "40",
    }

    def __init__(self, player_1: Player, player_2: Player, history_sets: List[str]) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.history_sets = history_sets


    def run_game(self):
        
        counter_set = 0
        for player_name in self.history_sets:

            if player_name == self.player_1.name:
                self.player_1.score += 1
            elif player_name == self.player_2.name:
                self.player_2.score += 1

            counter_set += 1

            self.load_winner()

            if counter_set in [6, 7]:
                if self.check_deuce:
                   print("Deuce")
                else:
                    print(f"Ventaja {self.winner.name}")
            elif counter_set in [8]:
                if self.check_deuce:
                    print("Deuce")
                    continue


                print(f"Ha ganado el {self.winner.name}")
            else:
                print(f"{self.tennis_dict.get(self.player_1.score)} - {self.tennis_dict.get(self.player_2.score)}") 

    @property
    def check_deuce(self) -> bool:
        return True if self.get_high_scoring_player() is None else False
    
    def load_winner(self):
        
        if self.check_deuce:
            self.winner = None
            return
        
        self.winner = self.get_high_scoring_player()
        


    def get_high_scoring_player(self) -> Player:

        if self.player_1.score > self.player_2.score:
            return self.player_1
        elif self.player_1.score < self.player_2.score:
            return self.player_2


def main():
    player_1 = Player(name="P1")
    player_2 = Player(name="P2")

    history_sets = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    # history_sets = ["P1", "P2", "P2", "P2", "P1", "P2", "P1", "P1"]
    # history_sets = ["P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2"]
    
    tennis_match = TennisMatch(player_1=player_1, player_2=player_2, history_sets=history_sets)

    tennis_match.run_game()

main()