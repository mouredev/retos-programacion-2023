def TennisMatch(players):
    p1Points = 0
    p2Points = 0

    for player in players:
        if player == "P1":
            p1Points += 1
        elif player == "P2":
            p2Points += 1
        else:
            print("Error en el tanteo")
            return

        if p1Points == 4 and p2Points == 4:
            p1Points = 3
            p2Points = 3

        PrintScore(p1Points, p2Points)


def PrintScore(P1, P2):
    score = ["Love", "15", "30", "40"]

    if P1 == P2 and P1 == 3:
        print("\tDeuce")
    elif P1 == 4 and P2 == 3:
        print("\tVentaja P1")
    elif P2 == 4 and P1 == 3:
        print("\tVentaja P2")
    elif P1 == 5 and P1 - P2 == 2:
        print("\tGana P1")
    elif P2 == 5 and P2 - P1 == 2:
        print("\tGana P2")
    else:
        print("P1:\t {} - {} \t:P2".format(score[P1], score[P2]))


TennisMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
TennisMatch(["P1", "P1", "P1", "P2", "P2", "P2",
            "P1", "P2", "P1", "P2", "P2", "P2"])
