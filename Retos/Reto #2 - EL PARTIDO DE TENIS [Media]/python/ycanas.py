def score(game):
    points_player1 = 0
    points_player2 = 0

    puntuation = {0: "love", 1: 15, 2: 30, 3: 40}

    for points in game:
        player1 = points == "P1"
        player2 = points == "P2"

        if player1:
            points_player1 += 1
        
        if player2:
            points_player2 += 1

        tie = points_player1 == points_player2 and points_player1 >= 3
        
        advantage_player1 = points_player1 >= 4 and points_player1 > points_player2
        advantage_player2 = points_player2 >= 4 and points_player2 > points_player1

        wins_player1 = points_player1 >= 4 and points_player1-points_player2 >= 2
        wins_player2 = points_player2 >= 4 and points_player2-points_player1 >= 2

        if tie:
            print("Deuce")

        elif wins_player1:
            print("Ha ganado el P1")

        elif wins_player2:
            print("Ha ganado el P2")

        elif advantage_player1:
            print("Ventaja P1")

        elif advantage_player2:
            print("Ventaja P2")

        else:
            print(f"{puntuation[points_player1]} - {puntuation[points_player2]}")

sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
score(sequence)
