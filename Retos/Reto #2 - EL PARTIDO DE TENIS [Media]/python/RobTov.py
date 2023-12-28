def tennis_game(sequence: list) -> None:
    score_values = ['Love', '15', '30', '40']
    player_scores = {'p1': 0, 'p2': 0}

    for s in sequence:
        if s == 'P1':
            player_scores['p1'] += 1
        else:
            player_scores['p2'] += 1
        if player_scores['p1'] < 4 and player_scores['p2'] < 4:
            if (player_scores['p1'] == 3 and player_scores['p2'] == 3):
                print('Deuce')
            else:
                print(
                    f'{score_values[player_scores["p1"]]}   -   {score_values[player_scores["p2"]]}')
        else:
            if player_scores['p1'] == player_scores['p2']:
                print('Deuce')
            if player_scores['p1'] == player_scores['p2'] + 2 or player_scores['p2'] == player_scores['p1'] + 2:
                print(
                    f'Ha ganado el {max(player_scores, key=player_scores.get).upper()}')
            elif player_scores['p1'] == player_scores['p2'] + 1 or player_scores['p2'] == player_scores['p1'] + 1:
                print(
                    f'Ventaja {max(player_scores, key=player_scores.get).upper()}')


def start() -> None:
    tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])


if __name__ == '__main__':
    start()
