scores = ("Love", "15", "30", "40")

points_player1 = 0
points_player2 = 0

player1 = input('Ingrese alias jugador 1: ')
player2 = input('Ingrese alias jugador 2: ')

winner = False
while not winner:

    if points_player1 >= 3 and points_player2 >= 3 and points_player1 == points_player2:
        print(f"\n{player1.upper()}(P1) VS {player2.upper()}(P2)\n\t=== Deuce ===\n")

    elif points_player1 > 3 or points_player2 > 3:

        if (points_player1-points_player2) >= 2:
            print(f"*** {player1.upper()}(Player1) - GANO ***")
            winner = True
        elif (points_player2-points_player1) >= 2:
            print(f"*** {player2.upper()}(Player2) - GANO ***")
            winner = True
        elif (points_player1-points_player2) == 1:
            print("\tAd-In")
        elif (points_player2-points_player1) == 1:
            print("\tAd-Out")
    else:
        print(
            f"\n{player1.upper()}(P1) VS {player2.upper()}(P2)\n{scores[points_player1]}\t\t{scores[points_player2]}\n")

    if not winner:
        points_of_game = input("Puntos para (P1 o P2): ")

    if points_of_game == "P1" or points_of_game == "p1":
        points_player1 += 1
    elif points_of_game == "P2" or points_of_game == "p2":
        points_player2 += 1
    else:
        print("entrada no válida")
