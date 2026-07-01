partido = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

def tenis(partido):
    print("**TENIS🎾**")
    
    player_uno = 0
    player_dos = 0
    puntos = {0: "Love", 1: 15, 2: 30, 3:40}

    for punto in partido:
        if punto == "P1":
            player_uno += 1
         
        else:
            player_dos += 1

        if(player_uno == 3 and player_dos == 3):
            print("Deuce")
        print(f"{player_uno} - {player_dos}")

    
tenis(partido)