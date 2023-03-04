""" 
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

moves = {
    "🗿": ["🦎", "✂️"],
    "📄": ["🗿", "🖖"],
    "✂️": ["📄", "🦎"] ,
    "🖖": ["✂️", "🗿"],
    "🦎": ["🖖", "📄"]    
    }




def run(plays_list):
    player_1_score = 0  
    player_2_score = 0


    for play in plays_list:
          player_1_move = play[0]
          player_2_move = play[1]
        
          # list of all moves that would win against the move played by player 2.
          player_1_winning_moves = moves[player_1_move]

          player_2_move_in_player_1_winning_moves = player_1_winning_moves.count(player_2_move)

          if player_2_move_in_player_1_winning_moves > 0:
              player_1_score += 1
              print(f"{player_1_move} beats {player_2_move}")

          elif player_1_move == player_2_move:
              player_1_score += 1
              player_2_score += 1
              print(f"Tie: {player_1_move}  =  {player_2_move}")

          else:
              player_2_score += 1
              print(f"{player_2_move} beats {player_1_move}")

 

    if player_1_score > player_2_score:
        print("Player 1 wins")

    elif player_1_score == player_2_score:
        print("Tie")

    else: 
        print("Player 2 wins")


if __name__ == "__main__":
    run([("✂️", "✂️"), ("✂️", "✂️"), ("✂️", "✂️")])