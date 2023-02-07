def partido(puntuacion):
    puntos_1 = 0
    puntos_2 = 0
    score = ""
    winner = ""
    for i in puntuacion:
        if i == "P1":
            puntos_1 += 1
        elif i == "P2":
            puntos_2 += 1
        if (puntos_1 < 4 and puntos_2 < 4) and (puntos_1 + puntos_2 < 6):
            score = puntuacion_normalizada(puntos_1) + " - " + puntuacion_normalizada(puntos_2)
        elif (puntos_1 == puntos_2):
            score = "Deuce"
        elif (puntos_1 > puntos_2):
            score = "Ventaja P1" if (puntos_1 - puntos_2 == 1) else "Ha ganado el P1"
            winner = "P1"
        else:
            score = "Ventaja P2" if (puntos_2 - puntos_1 == 1) else "Ha ganado el P2"
            winner = "P2"
        print(score)
    return winner

def puntuacion_normalizada(puntuacion):
    if puntuacion == 0:
        return "Love"
    elif puntuacion == 1:
        return "15"
    elif puntuacion == 2:
        return "30"
    elif puntuacion == 3:
        return "40"

puntuacion = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
winner = partido(puntuacion)
print("Ha ganado el " + winner)
