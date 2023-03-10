"""
/*
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
 */
"""


def get_winner(games: list[tuple[str, str]]) -> None:

    rules: map(str, list[str]) = {
        "πΏ": ["βοΈ", "π¦"],
        "π": ["πΏ", "π"],
        "βοΈ": ["π", "π¦"],
        "π¦": ["π", "π"],
        "π": ["βοΈ", "πΏ"]
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
    get_winner([("πΏ", "βοΈ"), ("βοΈ", "πΏ"), ("π", "βοΈ"), ("πΏ", "βοΈ"), ("π¦", "π¦")])
    get_winner([("πΏ", "βοΈ"), ("βοΈ", "πΏ"), ("π", "βοΈ")])
    get_winner([("πΏ", "π"), ("βοΈ", "π¦"), ("π", "π¦"), ("βοΈ", "π"), ("βοΈ", "π")])
    get_winner([("πΏ", "π"), ("βοΈ", "π¦"), ("π", "π¦"), ("βοΈ", "π"), ("βοΈ", "π"), ("πΏ", "πΏ")])
