from enum import Enum


class Player(Enum):
    P1 = 1
    P2 = 2


def tennis_game(points: list):
    scores = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0
    finished = False

    for player in points:
        if player == Player.P1:
            p1_points += 1
        elif player == Player.P2:
            p2_points += 1
        else:
            print("The points played are not correct")
            return

        if p1_points >= 4 or p2_points >= 4:
            if abs(p1_points - p2_points) >= 2:
                finished = True

        if finished:
            break

        if p1_points >= 3 and p2_points >= 3:
            if p1_points == p2_points:
                print("Deuce")
            else:
                winner = "P1" if p1_points > p2_points else "P2"
                print(f"Advantage {winner}")
        else:
            print(f"{scores[p1_points]} - {scores[p2_points]}")

    if not finished:
        winner = "P1" if p1_points > p2_points else "P2"
        print(f"It has won the {winner}")


tennis_game([Player.P1, Player.P1, Player.P2, Player.P2,
             Player.P1, Player.P2, Player.P1, Player.P1])

tennis_game([Player.P1, Player.P1, Player.P2, Player.P2,
             Player.P1, Player.P2, Player.P1, Player.P1, Player.P2, Player.P1])

tennis_game([Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1])

tennis_game([Player.P1, Player.P1])
