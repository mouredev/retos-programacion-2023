# Reto #2: EL PARTIDO DE TENIS

scores = ("love", "15", "30", "40", "win")
points_won = ("P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P2", "P1", "P1", "P1")
p1_points = 0
p2_points = 0
deuce_score = 1

for point in points_won:
    if point == "P1":
      p1_points = p1_points + 1
    elif point == "P2":
       p2_points = p2_points + 1
    
    p1_score = scores[p1_points]
    p2_score = scores[p2_points]
    
    if p1_score == "40" and p2_score == "40":
        print("deuce # ", deuce_score)
        p1_points = 3
        p2_points = 3
        deuce_score = deuce_score + 1
    elif (p1_points == 4 and p2_points == 3) or (p2_points == 4 and p1_points == 3):
        if (p1_points > p2_points):
            print("ventaja", point)
            p1_points = 3
            p2_points = 2
        elif (p2_points > p1_points):
            print("ventaja", point)
            p1_points = 2
            p2_points = 3
    elif (p1_points > 3 or p2_points > 3):
        print("GAME", point)
        break
    else: 
        print(p1_score, p2_score)