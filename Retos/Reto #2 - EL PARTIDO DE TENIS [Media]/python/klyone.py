#!/usr/bin/env python3

class TennisMatch:
    def __init__(self):
        self.match_results = []
        self.value_scores = ["Love", "15", "30", "40"]
        self.winner = "None"
        self.ad_in = "None"
        self.p1_score = 0;
        self.p2_score = 0;

    def run_turn(self, result):
        if self.is_finished():
            return

        if result == "P1":
            self.p1_score = self.p1_score + 1
        elif result == "P2":
            self.p2_score = self.p2_score + 1

    def is_deuce(self):
        max_score = len(self.value_scores)-1

        if self.p1_score == self.p2_score and self.p1_score >= max_score:
            self.ad_in = "None"
            return True

        return False

    def is_ad_in(self):
        max_score = len(self.value_scores)-1

        if self.p1_score > self.p2_score and self.p2_score >= max_score:
            self.ad_in = "P1"
            return True
        if self.p2_score > self.p1_score and self.p1_score >= max_score:
            self.ad_in = "P2"
            return True

        return False

    def is_finished(self):
        max_score = len(self.value_scores)-1

        if self.p1_score > max_score and (self.p1_score-self.p2_score >= 2):
            self.winner = "P1"
            return True

        if self.p2_score > max_score and (self.p2_score-self.p1_score >= 2):
            self.winner = "P2"
            return True

        return False

    def print_status(self):
        if self.is_finished():
            print("Ha ganado el "+self.winner)
            return
        if self.is_ad_in():
            print("Ventaja "+self.ad_in)
            return
        if self.is_deuce():
            print("Deuce")
            return

        print(self.value_scores[self.p1_score]+" - "+self.value_scores[self.p2_score])


def read_turns_from_user():
    turns = []
    print("Introduce el turno (P1 o P2). Para finalizar, introduce X")

    current_turn = input("Turno actual: ")
    while current_turn != "X":
        if current_turn != "P1" and current_turn != "P2":
            print("Turno no reconocido, introduce P1 o P2. Para finalizar, introduce X")
        else:
            turns.append(current_turn)
        current_turn = input("Turno actual: ")
    return turns

if __name__ == "__main__":
    turns = read_turns_from_user()
    print("Turnos: "+str(turns))

    match = TennisMatch()

    # match.print_status()
    for t in turns:
        match.run_turn(t)
        match.print_status()
