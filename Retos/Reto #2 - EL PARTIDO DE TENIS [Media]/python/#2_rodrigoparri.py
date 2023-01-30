
def tennisMatch(win_point_iter):
    P1 = 0
    P2 = 0
    scoreboard = [0,0]
    winner = ""
    points = {
        0:"Love",
        1:"15",
        2:"30",
        3:"40",
        4:"Adv",
        5:" wins"
    }

    for P in win_point_iter:

        if P == "P1":
            P1 += 1

        elif P == "P2":
            P2 += 1

        if P1 >= 3 and P1 == P2:  # every time there´s a tie
            P1 = 3  # both return to 40 - 40
            P2 = 3
            print("Deuce")
        elif P1 == 5:
            winner = "P1"
            print(winner + points[5])
        elif P2 == 5:
            winner = "P2"
            print(winner + points[5])
        else:
            scoreboard[0] = points[P1]
            scoreboard[1] = points[P2]
            print(f"{scoreboard[0]}" + " - " + f"{scoreboard[1]}")


if __name__ == "__main__":
    match = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    tennisMatch(match)
