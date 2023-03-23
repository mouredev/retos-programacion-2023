def puntos_a_texto(puntaje):
    if puntaje == 0:
        return "Love"
    elif puntaje == 1:
        return "15"
    elif puntaje == 2:
        return "30"
    elif puntaje >= 3:
        return "40"

def partido_de_tenis(secuencia_de_puntos):
    p1, p2 = 0, 0

    for punto in secuencia_de_puntos:
        if punto == "P1":
            p1 += 1
        elif punto == "P2":
            p2 += 1
        else:
            print("Error: Solo se aceptan 'P1' o 'P2'.")

        if p1 == 3 and p2 == 3:
            print("Deuce")
        elif p1 == 4 and p2 == 3:
            print("Ventaja P1")
        elif p1 == 3 and p2 == 4:
            print("Ventaja P2")
        else:
            print(puntos_a_texto(p1), " - ", puntos_a_texto(p2))

        if (p1 >= 4 or p2 >= 4) and (abs(p1 - p2) >= 2):
            if p1 > p2:
                print("Ha ganado el P1")
            else:
                print("Ha ganado el P2")

partido_de_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])