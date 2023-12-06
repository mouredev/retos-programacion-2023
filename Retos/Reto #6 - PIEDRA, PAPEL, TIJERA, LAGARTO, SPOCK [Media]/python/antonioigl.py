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


def get_winner(games: list[tuple[str, str]]) -> None:

    rules: map(str, list[str]) = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["📄", "🖖"],
        "🖖": ["✂️", "🗿"]
    }

    player_1: int = 0
    player_2: int = 1

    winner: str = "Tie"
    player_1_points: int = 0
    player_2_points: int = 0

    for game in games:
        if game[player_2] in rules[game[player_1]]:
            player_1_points += 1
        if game[player_1] in rules[game[player_2]]:
            player_2_points += 1

    if player_1_points > player_2_points:
        winner = "Player 1"
    if player_2_points > player_1_points:
        winner = "Player 2"

    print(winner)


if __name__ == "__main__":
    get_winner([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️"), ("🗿", "✂️"), ("🦎", "🦎")])
    get_winner([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
    get_winner([("🗿", "🖖"), ("✂️", "🦎"), ("🖖", "🦎"), ("✂️", "📄"), ("✂️", "📄")])
    get_winner([("🗿", "🖖"), ("✂️", "🦎"), ("🖖", "🦎"), ("✂️", "📄"), ("✂️", "📄"), ("🗿", "🗿")])
