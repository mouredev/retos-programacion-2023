import re


class Player:
    def __init__(self, player_id: int, score: int = 0, winner: bool = False):
        self.__player_id = player_id
        self.__score = score
        self.__winner = winner

    def get_player_id(self):
        return self.__player_id

    def set_player_id(self, player_id: int):
        self.__player_id = player_id

    def get_score(self):
        return self.__score

    def set_score(self, score: int):
        self.__score = score

    def get_winner(self):
        return self.__winner

    def set_winner(self, winner: bool): 
        self.__winner = winner

    def display_score(self) -> str:
        score_dict = {0: "Love", 1: "15", 2: "30", 3: "40", 4: f"Ventaja P{self.__player_id}"}
        if self.get_score() in score_dict:
            return score_dict[self.get_score()]
        else:
            self.set_winner(True)
            return f"Ha ganado el P{self.__player_id}"


def score_table(player1: Player, player2: Player):
    scores = {1: player1.get_score(), 2: player2.get_score()}
    if scores[1] >= 3 and scores[2] >= 3:
        if scores[1] == scores[2]:
            if scores[1] == 4 and scores[2] == 4:
                player1.set_score(3)
                player2.set_score(3)
            print("Deuce")
        elif scores[1] > scores[2]:
            print(player1.display_score())
        elif scores[1] < scores[2]:
            print(player2.display_score())
        if scores[1] >= 4 and scores[2] >= 4:
            player1.set_score(3)
            player2.set_score(3)
    else:
        if player1.get_score() == 4:
            player1.set_score(player1.get_score() + 1)
            print(player1.display_score())
        elif player2.get_score() == 4:
            player2.set_score(player2.get_score() + 1)
            print(player2.display_score())
        else:
            print(f"{player1.display_score()} - {player2.display_score()}")


def game(player1: Player, player2: Player):
    game_finished = False
    pattern = "^P[1|2]$"
    while not game_finished:
        has_scored = input("Anota: ").upper()
        if re.search(pattern, has_scored):
            if "1" in has_scored:
                player1.set_score(player1.get_score() + 1)
            elif "2" in has_scored:
                player2.set_score(player2.get_score() + 1)
            else:
                print("Ingresa a un jugador válido")
            score_table(player1, player2)
        else:
            print("El formato correcto de entrada es: P1 o P2")
        if player1.get_winner() or player2.get_winner():
            print("Juego terminado!")
            game_finished = True


p1 = Player(player_id=1)
p2 = Player(player_id=2)

game(p1, p2)
