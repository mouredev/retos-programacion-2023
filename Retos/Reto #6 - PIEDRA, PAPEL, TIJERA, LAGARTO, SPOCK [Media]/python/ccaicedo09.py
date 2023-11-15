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

def game(rounds: list) -> str:
    
    situations = {"🗿": "✂️🦎",
                  "📄": "🗿🖖",
                  "✂️": "📄🦎",
                  "🦎": "📄🖖",
                  "🖖": "🗿✂️"
                  }
    player_1 = 0
    player_2 = 0
    
    for game in rounds:
        if game[0] != game[1]:
            if game[1] in situations[game[0]]:
                player_1 +=1
            else:
                player_2 += 1 
        
    if player_1 == player_2:
        return  "Tie"
    elif player_1 > player_2:
        return "Player 1"
    else:
        return "Player 2"      
        
print(game([("🗿", "🗿")]))
print(game([("🗿", "✂️")]))
print(game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
