def tennis_game(points: list):
    pos_puntuacion = ["Love", 15, 30, 40, ]
    punt_p1 = 0
    punt_p2 = 0

    for point in points:
        if point == "P1" or point == "P2":
            if point == "P1":
                punt_p1 += 1
            else:
                punt_p2 += 1

            diff = punt_p1 - punt_p2

            if abs(diff) >= 2 and (punt_p1 > 3 or punt_p2 > 3):
                # Hay un jugador que ha ganado
                if diff < 0:
                    print("Ha ganado el P2")
                else:
                    print("Ha ganado el P1")
            else:
                # El partido sigue en juego
                if punt_p1 > 2 and punt_p2 > 2:
                    if punt_p1 == punt_p2:
                        # Ambos tienen la misma puntuación y han superado los 40-40
                        print("Deuce")
                    else:
                        # Alguien de los dos tiene ventaja
                        if diff > 0:
                            print("Ventaja P1")
                        else:
                            print("Ventaja P2")
                else:
                    # Los dos no han llegado a 40
                    print(f'{pos_puntuacion[punt_p1]} - {pos_puntuacion[punt_p2]}')
        else:
            print("Error al pasar las puntuaciones.")
            break


tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])