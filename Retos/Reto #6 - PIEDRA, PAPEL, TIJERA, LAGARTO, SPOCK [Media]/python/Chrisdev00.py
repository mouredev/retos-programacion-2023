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

"""
Reglas

Piedra: Derrota a tijera y lagarto, pero es aplastada por papel y vaporizada por Spock.
Papel: Derrota a piedra y Spock, pero es cortado por tijera y comido por lagarto.
Tijera: Derrota a papel y lagarto, pero es aplastada por piedra y destruida por Spock.
Lagarto: Derrota a papel y Spock, pero es decapitado por tijera y aplastado por piedra.
Spock: Derrota a tijera y piedra, pero es cubierto por papel y envenenado por lagarto.

"""

def game_rock_paper_scissors_lizard_spock(games):

    options = ["🪨", "📄", "✂️", "🐊", "🖖"]
    player_1_points = 0
    player_2_points = 0

    for game in games:

        player_1_game = game[0]
        player_2_game = game[1]
        if player_1_game != player_2_game:
            if( 
            (player_1_game == "🪨" and (player_2_game == "✂️" or player_2_game == "🐊")) or
            (player_1_game == "📄" and (player_2_game == "🪨" or player_2_game == "🖖")) or
            (player_1_game == "✂️" and (player_2_game == "🐊" or player_2_game == "📄")) or
            (player_1_game == "🐊" and (player_2_game == "📄" or player_2_game == "🖖")) or
            (player_1_game == "🖖" and (player_2_game == "✂️" or player_2_game == "🪨"))
            ):
                 player_1_points += 1
            
            else:
                player_2_points += 1

    return "Es un empate" if player_1_points == player_2_points else "El ganador es el player_1" if player_1_points > player_2_points else "El ganador es el player_2"

print(game_rock_paper_scissors_lizard_spock([("🐊", "🐊"), ("🖖", "🐊"), ("✂️", "📄"), ("🪨", "🐊")]))
print(game_rock_paper_scissors_lizard_spock([("✂️", "🐊"), ("🖖", "📄"), ("🪨", "📄"), ("✂️", "🖖")]))
print(game_rock_paper_scissors_lizard_spock([("🐊", "🖖"), ("🖖", "📄"), ("📄", "📄"), ("🪨", "🪨")]))
print(game_rock_paper_scissors_lizard_spock([("✂️", "✂️"), ("🪨", "🪨"), ("✂️", "🖖"), ("🪨", "📄")]))