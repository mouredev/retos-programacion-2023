'''/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */'''
 


win_options = {
    "🗿": ("✂️","🦎"),
    "📄": ("🗿","🖖"),
    "✂️": ("📄","🦎"),
    "🦎": ("📄","🖖"),
    "🖖": ("🗿","✂️")
}

def game(combinations: list):
    
    win_player_1 = 0
    win_player_2 = 0

    for combination in combinations:
        player_1, player_2 = combination
        
        if player_1 == player_2:
            return "Tie"
        
        if player_1 not in win_options or player_2 not in win_options:
            return "No ha indicado valores correctos para el juego"
    
        if player_2 in win_options[player_1]:
            win_player_1 += 1
        else:
            win_player_2 += 1 
    
    if win_player_1 > win_player_2:
        return "Player 1"
    else:
        return "Player 2"

print(game([("🗿","✂️"), ("🗿","✂️"), ("📄","✂️")]))
print(game([("🗿","🖖"), ("🗿","✂️"), ("📄","🦎")]))
print(game([("🗿","🗿"), ("✂️","✂️"), ("🦎","🦎")]))