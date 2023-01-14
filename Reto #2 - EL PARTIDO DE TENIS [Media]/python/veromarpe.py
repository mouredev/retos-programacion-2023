def run():
    juegos = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    p1=0
    p2=0
    ronda=0
    points = ["Love", "15", "30", "40"]

    for i in juegos:
        ronda +=1
        if i == "P1":
            p1 += 1
        elif i == "P2":
            p2 += 1
        
        if p1 == 3 and p2 == 3:
           print(f"{ronda}. Deuce")
        elif (p1 < 3 or p2 < 3):
            print(f"{ronda}. Jugador 1: {points[p1]} | Jugador 2: {points[p2]}")  

        if (p1 >= 4 or p2 >= 4) and abs(p1 - p2) >= 2:
            if p1 > p2:
                print(f"{ronda}. ¡Ha ganado el Jugador 1!")
            else:
                print(f"{ronda}. ¡Ha ganado el Jugador 2!")
            return
        
        if (p1 >= 3 and p2 >= 3) and abs(p1 - p2) == 1:
            if p1 > p2:
                print(f"{ronda}. Punto Jugador 1")
            else:
                print(f"{ronda}. Punto Jugador 2")
            continue

if __name__ == "__main__":
    run()
