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

""" The dictionary defines the symbols againts which a given symbol wins """
model = {
    '🗿': ['🦎', '✂️'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['🖖', '📄'],
    '🖖': ['🗿', '✂️'],
}
points_p1 = 0
points_p2 = 0


def game(player1: str, player2: str):
    global points_p1, points_p2
    if player2 in model[player1]:
        points_p1 += 1
    elif player1 in model[player2]:
        points_p2 += 1


def new_game(plays: list[tuple[str, str]]):
    global points_p1, points_p2
    points_p1, points_p2 = 0, 0
    for play in plays:
        p1, p2 = play
        game(p1, p2)
    if points_p1 == points_p2:
        return 'Tie'
    elif points_p1 > points_p2:
        return 'Player 1'
    else:
        return 'Player 2'


if __name__ == '__main__':
    print(new_game([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]))
