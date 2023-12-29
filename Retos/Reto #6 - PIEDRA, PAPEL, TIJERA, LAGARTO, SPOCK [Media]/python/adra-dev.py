"""
Crea un programa que calcule quien gana mas partidas al piedra,
papel, tijera, lagartija, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La funcion recibe un listado que contiene pares,
representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄"
(papel), 
"✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. 
Resultado: "Player 2".
"""

def rpsls(games):

    rules = {"🗿": ["✂️", "🦎"],
             "📄": ["🗿", "🖖"],
             "✂️": ["📄", "🦎"],
             "🦎": ["🖖", "📄"],
             "🖖": ["🗿", "✂️"]}


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
    return "Tie" if player_one_game == player_two_game else "Player1" if player_one_game > player_two_game else "Player 2"


print(rpsls([("🗿", "🗿")]))
print(rpsls([("🗿", "✂️")]))
print(rpsls([("✂️", "🗿")]))
print(rpsls(
    [("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]))
print(rpsls(
    [("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]))
