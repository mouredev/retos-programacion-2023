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

def piedra_papel_tijera_lagarto_spock (game):
    to_win = {
        "piedra": {"tijera", "lagarto"},
        "papel": {"piedra", "spock"},
        "tijera": {"papel", "lagarto"},
        "lagarto": {"papel", "spock"},
        "spock": {"piedra", "tijera"},
    }
    pts_player1 = 0
    pts_player2 = 0
    
    for play in game:
        if play[1] in to_win[play[0]]:
            pts_player1 += 1
        elif play[0] in to_win[play[1]]:
            pts_player2 += 1
    
    if pts_player1 > pts_player2:
        print("Player 1")
    elif pts_player2 > pts_player1:
        print("Player 2")
    else: print("Tie")


piedra_papel_tijera_lagarto_spock ([("piedra", "piedra"), ("tijera", "spock"), ("papel", "lagarto"), ("tijera", "papel")])