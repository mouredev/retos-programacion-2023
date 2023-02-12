from enum import Enum


class Jugada(Enum):
    PIEDRA = '🗿'
    PAPEL = '📄'
    TIJERAS = '✂️'
    LAGARTO = '🦎'
    SPOCK = '🖖'


def PiedraPapelTijerasLagartoSpock(juegos):
    p1_points = 0
    p2_points = 0

    ganador = {
        Jugada.PIEDRA: [Jugada.TIJERAS, Jugada.LAGARTO],
        Jugada.PAPEL: [Jugada.PIEDRA, Jugada.SPOCK],
        Jugada.TIJERAS: [Jugada.PAPEL, Jugada.LAGARTO],
        Jugada.LAGARTO: [Jugada.PAPEL, Jugada.SPOCK],
        Jugada.SPOCK: [Jugada.TIJERAS, Jugada.PIEDRA]
    }

    for juego in juegos:
        jugador1, jugador2 = juego
        if jugador1 == jugador2:
            p1_points += 1
            p2_points += 1
        elif jugador2 in ganador[jugador1]:
            p1_points += 1
        else:
            p2_points += 1

    if p1_points == p2_points:
        return "Empate a {} puntos".format(p1_points)
    elif p1_points > p2_points:
        return "Gana el jugador 1 por {} a {} puntos".format(p1_points, p2_points)
    else:
        return "Gana el jugador 2 por {} a {} puntos".format(p2_points, p1_points)


print(PiedraPapelTijerasLagartoSpock([
    [Jugada.PIEDRA, Jugada.TIJERAS],
    [Jugada.PIEDRA, Jugada.PAPEL],
    [Jugada.LAGARTO, Jugada.SPOCK]
]))

print(PiedraPapelTijerasLagartoSpock([
    [Jugada.TIJERAS, Jugada.TIJERAS],
    [Jugada.PIEDRA, Jugada.PAPEL],
    [Jugada.LAGARTO, Jugada.SPOCK],
    [Jugada.PIEDRA, Jugada.PAPEL],
    [Jugada.SPOCK, Jugada.PAPEL],
    [Jugada.LAGARTO, Jugada.LAGARTO],
    [Jugada.SPOCK, Jugada.LAGARTO],
]))
