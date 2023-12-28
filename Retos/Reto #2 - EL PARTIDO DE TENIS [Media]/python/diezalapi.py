class Player:
    points_def = ["Love", "15", "30", "40"]

    def __init__(self) -> None:
        self.score = 0

    def point(self) -> None:
        self.score += 1

    def get_score(self) -> int:
        return self.score


class Match:
    players = ["P1", "P2"]

    def __init__(self, points_sequence: list) -> None:
        self.p1 = Player()
        self.p2 = Player()
        self.diff = 0
        self.points_sequence = points_sequence
        self.finished = False

    def update_diff(self) -> None:
        self.diff = abs(self.p1.get_score() - self.p2.get_score())

    def print_status(self) -> None:
        winner = self.match_status()
        result1 = self.p1.get_score()
        result2 = self.p2.get_score()
        if winner == 0: 
            if result1 >= 3 and result2 >= 3:
                if self.diff == 0:
                    print("Deuce")
                else:
                    print(f"Ventaja {Match.players[0] if result1 > result2 else Match.players[1]}")
            else:
                print(f"{Player.points_def[result1]} - {Player.points_def[result2]}")
        else:
            print(f"Ha ganado el {Match.players[0] if result1 > result2 else Match.players[1]}")
 
    def register_point(self, point: str) -> None:
        if point == "P1":
            self.p1.point()
        elif point == "P2":
            self.p2.point()
        else:
            print("Error en formato de punto")
            return
        self.update_diff()

    def match_status(self) -> int: # 0-> no winner, 1-> win P1, 2-> win P2
        if self.diff < 2:
            return 0
        elif self.p1.get_score() >= 4 or self.p1.get_score() >= 4:
            self.finished = True
            return 1 if self.p1.get_score() >=4 else 2
        else:
            return 0

    def proccess(self) -> None:
        for point in self.points_sequence:
            self.register_point(point)
            self.print_status()
            if self.finished:
                break


if __name__ == '__main__':
    my_match = ["P1", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2"]

    match = Match(my_match)
    match.proccess()

    print("*** Fin ***")
