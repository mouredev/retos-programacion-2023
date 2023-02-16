# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock

'''
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
La función recibe un listado que contiene pares, representando cada jugada.
El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
"✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''

# Solución
def game (games: list[tuple]):
    rules = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["🗿", "✂️"]
    }
    player_one = 0
    player_two = 0

    for game in games:
        player_one_game = game[0]
        player_two_game = game[1]
        if player_one_game != player_two_game:
            if player_two_game in rules[player_one_game]:
                player_one += 1
            else:
                player_two += 1

    if player_one > player_two:
        result = 'Player 1'
    elif player_two > player_one:
        result =  'Player 2'
    else:
        result = 'Tie'

    return result


print(game([["🖖", "📄"], ["🖖", "📄"], ["🗿", "🦎"]]))
print(game([["🗿", "✂️"],  ["🖖", "✂️"],  ["📄", "🦎"]]))
print(game([["🖖", "🖖"], ["🖖", "🗿"], ["✂️", "🖖"]]))