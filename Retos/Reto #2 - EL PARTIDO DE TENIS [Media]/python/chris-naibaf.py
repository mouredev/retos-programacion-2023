puntos_de_juego = input(
    "Introduce la secuencia de puntos de la siguiente manera (P1,P2,P1, ...): "
).upper()

lista_de_puntos = puntos_de_juego.split(",")


def conteo_puntos(lista_de_puntos):
    puntosP1 = 0
    puntosP2 = 0
    rondas = []

    for punto in lista_de_puntos:
        if punto == "P1":
            puntosP1 += 1

        if punto == "P2":
            puntosP2 += 1

        rondas.append([puntosP1, puntosP2])

        if puntosP1 == 3 and puntosP2 == 3:
            return deuce(rondas, lista_de_puntos)
        elif puntosP1 == 4:
            rondas.append("Ha ganado el P1!")
            return rondas
        elif puntosP2 == 4:
            rondas.append("Ha ganado el P2!")
            return rondas

    return rondas


def deuce(rondas, lista_de_puntos):
    rondas_restantes = lista_de_puntos[len(rondas) :]
    puntosP1 = 0
    puntosP2 = 0

    rondas.append("Deuce")

    for punto in rondas_restantes:
        if punto == "P1":
            puntosP1 += 1
            if puntosP2 == 1:
                puntosP2 -= 1

        if punto == "P2":
            puntosP2 += 1
            if puntosP1 == 1:
                puntosP1 -= 1

        if puntosP1 == 0 and puntosP2 == 0:
            rondas.append("Deuce")
        elif puntosP1 == 1:
            rondas.append("Ventaja P1")
        elif puntosP2 == 1:
            rondas.append("Ventaja P2")
        elif puntosP1 == 2:
            rondas.append("Ha ganado el P1!")
            return rondas
        elif puntosP2 == 2:
            rondas.append("Ha ganado el P2!")
            return rondas


formato_puntaje = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40",
}

rondas_finales = conteo_puntos(lista_de_puntos)

for ronda in rondas_finales:
    if ronda == [3, 3]:
        continue
    if type(ronda) == list:
        print(f"{formato_puntaje[ronda[0]]} - {formato_puntaje[ronda[1]]}")
    else:
        print(ronda)
