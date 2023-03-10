""" 
* Crea un programa que calcule quien gana mรกs partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciรณn recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "๐ฟ" (piedra), "๐" (papel),
 *   "โ๏ธ" (tijera), "๐ฆ" (lagarto) o "๐" (spock).
 * - Ejemplo. Entrada: [("๐ฟ","โ๏ธ"), ("โ๏ธ","๐ฟ"), ("๐","โ๏ธ")]. Resultado: "Player 2".
 * - Debes buscar informaciรณn sobre cรณmo se juega con estas 5 posibilidades.
"""


def rock_paper_scissors_lizard_spock(games):
    rules = {"๐ฟ": ["โ๏ธ", "๐ฆ"],
             "๐": ["๐ฟ", "๐"],
             "โ๏ธ": ["๐", "๐ฆ"],
             "๐ฆ": ["๐", "๐"],
             "๐": ["๐ฟ", "โ๏ธ"]}

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
    return "Tie" if player_one == player_two else "Player 1" if player_one > player_two else "Player 2"



print(rock_paper_scissors_lizard_spock([("โ๏ธ", "โ๏ธ")]))
