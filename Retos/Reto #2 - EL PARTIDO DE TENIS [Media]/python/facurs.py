

score = {"P1": 0, "P2": 0}
points = {"Love": 0, 15: 15, 30: 30, 40: 40}

game = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

for point in game:
    score[point] += 1
    print(points.get(score["P1"], "Deuce" if score["P1"] >= 3 else "Advantage " + point) + " - " + points.get(score["P2"], "Deuce" if score["P2"] >= 3 else "Advantage " + point))
    if score["P1"] >= 4 and score["P1"] - score["P2"] >= 2:
        print("Ha ganado el P1")
        break
    elif score["P2"] >= 4 and score["P2"] - score["P1"] >= 2:
        print("Ha ganado el P2")
        break
