# Escribe un programa en python que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "'P1'" (Player 1) o "'P2'" (Player 2), según quien
# gane cada punto del juego.
#
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

import time
#game = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2','P2']
#game = ['P1', 'P1', 'P1', 'P1', 'P1'] #---> FALLA antes del refactor!!
#game = ['P1', 'P1'] #---> FALLA antes del refactor!!
#game = [] #---> FALLA antes del refactor!!
#game = 'String' #---> FALLA antes del refactor!!
games =[
    #'String', 
    #[],
    #['P1', 'P1'],
    #['P1', 'P1','P1', 'P1','P1', 'P3'],
    #['P1', 'P1', 'P2', 1, 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2','P2'],
    #['P1', 'P1', 'P1', 'P1', 'P1'],
    ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2','P2'], ##---> Correcta!!
]

"""
def tennis_game(scores_game):
    scores = ['Love', '15', '30', '40']
    p1_score, p2_score = 0, 0
    p1, p2 = 0, 0

    for score in scores_game:
        if score == 'P1':
            p1_score += 1
            print('Point for P1')
        elif score == 'P2':
            p2_score += 1
            print('Point for P2')
        else:
            print(f'This input {score} is not valid')
            return 

        if p1_score < 4:
            p1 = scores[p1_score]
        else:
            p1 = p1_score
        
        if p2_score < 4:
            p2 = scores[p2_score]
        else:
            p2 = p2_score

        if (p1_score >= 4 or p2_score >= 4) and abs(p1_score - p2_score) >=2:
            if p1_score > p2_score:
                result_game = 'The winner is: Player 1'
            else:
                result_game = 'The winner is: Player 2'
        
            # refactor condicional anterior
            # result_game = 'The winner is: Player 1' if p1_score > p2_score else 'The winner is: Player 2'
        
        elif (p1_score >= 3 or p2_score >= 3) and p1_score == p2_score:
            result_game = 'Deuce'
        elif (p1_score >= 3 or p2_score >= 3) and p1_score > p2_score:
            result_game = 'Advantage P1'
        elif (p1_score >= 3 or p2_score >= 3) and p1_score < p2_score:
            result_game = 'Advantage P2'
        else:            
            result_game = (p1, p2)
        
        print(str(result_game) + '\n')
        time.sleep(1)
    return print('Full time!!')
"""

### REFACTORING ###

def check_data(game):
    if type(game) != list:
        return False, 'It only accepts list() as an argument!'
    
    if not game:
        return False, 'It only accepts not-empty list() as an argument!'

    if len(game) <= 4:
        return False, 'The number of games played is not valid!'
    
    for i in game:
        if i != 'P1' and i != 'P2':
            return False, 'The list of player is not valid!\nIt is only valid P1 and P2 for the points of Player1 and Player2 respectively.'

    return True, ''

def tennis_game(game):
    is_valid, error_msg = check_data(game)
    
    if not is_valid:
        print(error_msg)
        print('Game Over!!\n')
    else:
        print('Star the match!!\n')
    
        scores = ['Love', '15', '30', '40']
        p1_score, p2_score = 0, 0
        finished = False
        
        for point in game:
            time.sleep(1)
            
            if finished:
                print('The game is finished!\nNo more game points can be counted!\n')
                break
            
            if point == 'P1':
                p1_score += 1
                print('Point for P1')
            elif point == 'P2':
                p2_score += 1
                print('Point for P2')
            else:
                return print(f'This input {point} is not valid\n')

            if (p1_score >= 3 or p2_score >= 3) and p1_score == p2_score:
                result_game = 'Deuce\n'

            elif (p1_score >= 4 or p2_score >= 4):
                if abs(p1_score - p2_score) >=2:
                    result_game = 'The winner is: Player 1\n' if p1_score > p2_score else 'The winner is: Player 2\n'
                    finished = True
                elif p1_score > p2_score:
                    result_game = 'Advantage P1\n'
                else:
                    result_game = 'Advantage P2\n'
            
            else:
                result_game = f'({scores[p1_score]} - {scores[p2_score]})\n'

            print(result_game)

    return print('Full time!!\n')


for index, game in enumerate(games):
    time.sleep(1)
    print(index)
    tennis_game(game)