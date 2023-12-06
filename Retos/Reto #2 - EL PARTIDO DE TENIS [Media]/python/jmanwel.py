scoring = {0:"Love", 1:"15", 2:"30", 3: "40", 4: "Ventaja", 5: "45"}
points_P1 =  0
points_P2 = 0
sec = ["P1", "P2", "P2", "P2", "P1", "P1", "P1", "P2", "P1", "P1"]

for s in sec:
    if s == "P1":
        points_P1 = points_P1 + 1
    else:
        points_P2 = points_P2 + 1

    if points_P1 == 3 and points_P2 == 3:
        status = "deuce"
        print("deuce")
    elif points_P1 >= 4 or points_P2 >= 4:
        puntaje = points_P1 - points_P2
        if puntaje == 0: print("Deuce")
        elif puntaje == 1: print("La ventaja es para el Jugador 1")
        elif puntaje == -1: print("La ventaja es para el Jugador 2")
        elif puntaje >= 2: print("El ganador es el Jugador 1")
        else: print("El ganador es el Jugador 2")
    else:
        print(str(scoring[points_P1]) + " " + str(scoring[points_P2]))
    print("--------------------------------")