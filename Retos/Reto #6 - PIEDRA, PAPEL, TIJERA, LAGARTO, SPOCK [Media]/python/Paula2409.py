"""
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
"""
game_rules = {
    '🗿': ['🦎','✂️'], # rock crushes lizard and scissors
    '📄': ['🗿','🖖'], # paper covers rock and invalidates spock
    '✂️': ['📄','🦎'], # scissors cuts paper and beheads lizard
    '🦎': ['🖖', '📄'], # lizard poison spock and eats paper 
    '🖖': ['✂️', '🗿'] # spock breaks scissors and crushes rock
    }

def rock_paper_scissors(play):
    """
    Determines the winner of a game based on the rules of 
    'rock, paper, scissors, lizard, spock'.

    Args:
        play(list): a list with the option of each player

    Returns:
        str: returns which player wins
    """
    points_player1, points_player2 = 0,0
    index_play = 0
    while index_play < len(play):
        if play[index_play][0] in game_rules[play[index_play][1]]:
            points_player2 += 1
            print(f'Points player 2: {points_player2}')
        else:
            points_player1 += 1
            print(f'Points player 1: {points_player1}')

        index_play += 1
    if points_player1 > points_player2:
        return 'Player 1'
    elif points_player2 > points_player1:
        return 'Player 2'
    else:
        return 'Tie'
               
print(rock_paper_scissors([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
        
                