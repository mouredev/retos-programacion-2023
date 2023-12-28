def tennis_game(points):

    score_P1 = ["Love", 15, 30, 40, "Ventaja P1", "Ha ganado el P1"]
    score_P2 = ["Love", 15, 30, 40, "Ventaja P2", "Ha ganado el P2"]
    score = []
    P1_points = 0
    P2_points = 0

    for point in points:
        if point == "P1":
            P1_points += 1
        elif point == "P2":
            P2_points += 1
        if P1_points == P2_points and P1_points >= 3:
            P1_points = 3
            P2_points = 3
            score.append("Deuce")
            continue
        try:
            if P1_points > 3:
                score.append(score_P1[P1_points])
                continue
            elif P2_points > 3:
                score.append(score_P2[P2_points])
                continue
        except:
            print("Se han introducido mas puntos de los necesarios")
            print("\n")
            return
        score.append(f"{score_P1[P1_points]} - {score_P2[P2_points]}")

    for point in points:
        if point != "P1" and point != "P2":
            print("Datos invalidos")
            print("\n")
            return
    
    for index, point in enumerate(score):
        print(score[index])

    print("\n")
        
        
tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P1", "P1"])
tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])
tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1"])
tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "FALLO" , "P1", "P1"])