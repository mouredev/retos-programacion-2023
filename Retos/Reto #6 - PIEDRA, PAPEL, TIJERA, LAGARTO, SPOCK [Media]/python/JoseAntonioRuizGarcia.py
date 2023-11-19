'''
    Diccionario con las Reglas del juego
    Las claves del diccionario ganan a los valores
'''
rules = {
    '🗿': ['🦎', '✂️'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['🖖', '📄'], 
    '🖖': ['✂️', '🗿']
}

def runGame(game: list) -> None:
    points = []
    for round in game:
        if round[0] == round[1]:
            result_round = [0, 0]
        elif round[0] in rules.get(round[1]):
            result_round = [0, 1]
        else:
            result_round = [1, 0]
        
        points.append(result_round)
    
    points_pj1 = sum([point[0] for point in points])
    points_pj2 = sum([point[1] for point in points])

    if points_pj1 == points_pj2:
        print('Tie')
    elif points_pj1 > points_pj2:
        print('Player 1')
    else:
        print('Player 2')

if __name__ == '__main__':
    runGame([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])
