### Reto #6 - PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK [Media] ###
'''
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
 '''

### Decision type of development ###
# We will rely on a two-dimensional matrix with the five options on each axis, 
# and where we will define who wins at each crossroads, and of course also the ties.

import random

def calculate_result(move_player_1, move_player_2):
    if matrix_winner[move_player_1][move_player_2] == 1:
        game_result[name_player_1] += 1
        result_string = f'Gana {name_player_1} ({options[move_player_1]} )'
    elif matrix_winner[move_player_1][move_player_2] == 0:
        game_result[name_player_2] += 1
        result_string = f'Gana {name_player_2} ({options[move_player_2]} )'
    else:
        result_string = 'Empate'
        
    print(f'{options[move_player_1]} - {options[move_player_2]} : {result_string}. Puntuación: ({game_result[name_player_1]}-{game_result[name_player_2]})')


if __name__ == "__main__":
    # Winner crossover matrix
    matrix_winner = [
                    [-1, 0, 1, 1, 0],
                    [1, -1, 0, 0, 1],
                    [0, 1, -1, 1, 0],
                    [0, 1, 0, -1, 1],
                    [1, 0, 1, 0, -1]
                    ]
    
    # Name and score of players
    game_result = {"Player 1": 0, "Player 2": 0}
    name_player_1 = list(game_result)[0]
    name_player_2 = list(game_result)[1]

    # The five possible options
    options = ['🗿', '📄', '✂️', '🦎', '🖖']

    # List with the entries of the plays
    plays = [('🦎', '✂️'), ('📄', '🖖'), ('✂️', '📄'), ('🗿', '🖖'), ('🦎', '🖖'), 
             ('🗿', '✂️'), ('🦎', '🦎'), ('🗿', '🦎'), ('📄', '🦎'), ('🗿', '📄')]
    plays = []

    # This program works in two ways, if the previous line of "plays = []" is uncommented it will make random plays, 
    # otherwise it will be based on the example entries. 
    print("\n")
    if len(plays) > 0:
        for i in plays:
            # The position of the option is passed, not the option, so that you can find it in the matrix_winner
            calculate_result(options.index(i[0]), options.index(i[1]))
    else:
        for i in range(10):
            calculate_result(random.randint(0,len(options)-1), random.randint(0,len(options)-1))

    
    winner =    "Gana " + name_player_1 if game_result[name_player_1] > game_result[name_player_2] \
           else "Gana " + name_player_2 if game_result[name_player_1] < game_result[name_player_2] \
           else "Empate"
    score = f"{game_result[name_player_1]}-{game_result[name_player_2]}"
    print(f"\nResultado Final: {score}, {winner}")         
        
        
