from enum import Enum


class Player(Enum):
    PLAYER1 = 1
    PLAYER2 = 2


def tennis_match(move: list):
    game:list = ["Love", "15", "30", "40"]
    player1_points: int = 0
    player2_points: int = 0
    finished: bool = False
    error:bool = False

    for player in move:

        error = finished

        player1_points += 1 if player == Player.PLAYER1 else 0
        player2_points += 1 if player == Player.PLAYER2 else 0

        if player1_points >= 3 and player2_points >= 3:
            if not finished and abs(player1_points - player2_points) <= 1:
                print("Deuce" if player1_points == player2_points else
                      "Advantage PLAYER1" if player1_points > player2_points else "Advantage PLAYER2")
            else:
                finished = True
        else:
            if player1_points < 4 and player2_points < 4:
                print(f"{game[player1_points]} - {game[player2_points]}")
            else:
                finished = True

    print("The points played are not correct" if error or not finished else
          "PLAYER1 has won" if player1_points > player2_points else "PLAYER2 has won")


if __name__ == '__main__':
    tennis_match([Player.PLAYER1, Player.PLAYER1, Player.PLAYER2, Player.PLAYER2, Player.PLAYER1, Player.PLAYER1])
