
def points(tenis_match : list[str]):
    points_P1 = 0
    points_P2 = 0
    deuce = False
    adin = False

    for entry in tenis_match:
        if (entry == "P1" and points_P1 == "Love") or (entry == "P1" and points_P1 < 30):
            if points_P1 == "Love":
                points_P1 = 0
            points_P1 += 15
        elif entry == "P1" and points_P1 >= 30:
            points_P1 += 10
        if (entry == "P2" and points_P2 == "Love") or (entry == "P2" and points_P2 < 30):
            if points_P2 == "Love":
                points_P2 = 0
            points_P2 += 15
        elif entry == "P2" and points_P2 >= 30:
            points_P2 += 10

        if points_P1 == 0:
            points_P1 = "Love"
        if points_P2 == 0:
            points_P2 = "Love"
        
        if deuce:
            if (points_P1 > points_P2) and not adin:
                print("Ventaja para P1")
                adin = True
                continue
            elif (points_P1 > points_P2) and adin:
                print("El ganador es el jugador 1")
                break
            if (points_P2 > points_P1) and not adin:
                print("Ventaja para P2")
                adin = True
                continue
            elif (points_P2 > points_P1) and adin:
                print("El ganador es el jugador 2")
                break
        
        if (points_P1 == points_P2) and (points_P1 >= 40 or points_P2 >= 40):
            print("Deuce")
            deuce = True
            continue
        else:
            print(f"Player 1: {points_P1} - Player 2: {points_P2}")
        

if __name__ == "__main__":
    entry = ["P1", "P1", "P2", "P2", "P1", "P2", "P2","P2"]
    match_sequence = points(entry)