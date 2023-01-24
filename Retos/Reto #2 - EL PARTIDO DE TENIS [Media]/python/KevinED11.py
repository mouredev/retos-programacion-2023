scores = {'love': 0, 1: 15, 2: 30, 3: 40, 'Deuce': 'Empate'}


def match_winner(points) -> str:

    points_players = {'P1': 0, 'P2': 0}

    for point in points:

        if point == 'P1':
            points_players[point] += scores[1]
        else:
            points_players[point] += scores[1]

    if points_players['P1'] == points_players['P2']:
        return f"{scores.get('Deuce')}"

    elif points_players['P1'] >= 40 and points_players['P1'] - points_players['P2'] >= 20:
        return f'el ganador del partido es el jugador 1, ¡FELICIDADES! y estas son las puntuaciones {points_players}'
    else:
        return f'el ganador del partido fue el jugador 2 y estas son las puntuaciones {points_players}'


def match_points() -> list[str]:
    players_points = []

    print('ingrese "P1" o "P2" 8 VECES para indicar el jugador que ha ganado el punto o ingrese "exit" para finalizar: ')

    turno = input('ingrese el jugador: ').upper()
    intentos = 8

    while turno != 'exit' and intentos > 0:
        intentos -= 1

        if turno != 'P1' and turno != 'P2':
            print('Jugador ingresado no valido')
            return

        else:
            players_points.append(turno)

        if intentos == 0:
            print('Estos fueron los resultados del partido')
            print(players_points)

            return players_points

        turno = input('ingrese el jugador: ').upper()


if __name__ == '__main__':
    points = match_points()
    player_win = match_winner(points)
    print(player_win)
