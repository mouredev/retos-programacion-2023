
def match(moves: list[tuple[str, str]]) -> str:

    scores: dict[str, tuple[str, str, str]] = {
        'Result': ('Player1', 'Player2', 'Empate'),
    }

    points: dict[str, int] = {
        'player1': 0,
        'player2': 0,
    }

    # Create list with upper all values
    for i, (mov1, mov2) in enumerate(moves):
        moves[i] = mov1.upper(), mov2.upper()

    # check moves
    for i, (mov1, mov2) in enumerate(moves):
        print(f'Jugada {i + 1}: {mov1} vs {mov2}')

        if mov1 == mov2:
            points['player1'] += 0
            points['player2'] += 0

        if mov1 == 'PIEDRA' and mov2 == 'TIJERA' or mov1 == 'TIJERA' and mov2 == 'PAPEL' or mov1 == 'PAPEL' and mov2 == 'PIEDRA' or mov1 == 'LAGARTO' and mov2 == 'PAPEL' or mov1 == 'PAPEL' and mov2 == 'SPOCK' or mov1 == 'SPOCK' and mov2 == 'SPOCK' or mov1 == 'TIJERAS' and mov2 == 'LAGARTO' or mov1 == 'LAGARTO' and mov2 == 'SPOCK' or mov1 == 'PIEDRA' and mov2 == 'LAGARTO':
            points['player1'] += 1
        else:
            points['player2'] += 1

        print(f'{points}\n')

    # Match winner
    return f'El jugador {scores["Result"][0]} ha ganado' if points['player1'] > points['player2'] else f'El jugador {scores["Result"][1]} ha ganado' if points['player2'] > points['player1'] else f'El juego ha quedado en "{scores["Result"][2]}" con un {points["player1"]}:{points["player2"]} en el marcador'


if __name__ == '__main__':
    match1 = match([('Piedra', 'Tijera'), ('Papel', 'Tijera'),
                    ('Lagarto', 'Spock'), ('Spock', 'Tijera')])

    print(match1)
