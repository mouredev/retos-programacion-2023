'''
# Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

# Todos las combinaciones ganan a 2, y pierden contra 2
# Piedra: Gana contra -> Tijeras y Lagarto, Pierde contra -> Papel y Spock
# Papel: Gana contra -> Piedra y Spock, Pierde contra -> Tijera y Lagarto
# Tijera: Gana contra -> Papel y Lagarto, Pierde contra -> Piedra y Spock
# Lagarto: Gana contra -> Papel y Spock, Pierde contra -> Piedra y Tijera
# Spock: Gana contra -> Tijeras y Piedra, Pierde contra -> Papel y Lagarto
'''

RULES = {
    '🗿': ['🦎', '✂️'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['🖖', '📄'],
    '🖖': ['🗿', '✂️'],
}

def who_wins(player_one: str, player_two: str) -> str:
    if player_two in RULES[player_one]:
        return "Player 1 wins"
    elif player_one in RULES[player_two]:
        return "Player 2 wins"
    else:
        "Tie"

def play_game(games: list[tuple[str,str]]) -> str:
    player1_score = 0
    player2_score = 0

    for game in games:
        player_one, player_two = game
        result = who_wins(player_one, player_two)
        if result == "Player 1 wins":
            player1_score +=1
        elif result == "Player 2 wins":
            player2_score +=1
    
    if player1_score > player2_score:
        return "Player 1 won the game."
    elif player2_score > player1_score:
        return "Player 2 won the game."
    else:
        return "Tie"

def main():
    print(play_game([('🦎','✂️'),('🖖','✂️'),('🗿','📄'),('🖖','🗿'),('🦎','📄')]))

if __name__ == "__main__":
    main()
