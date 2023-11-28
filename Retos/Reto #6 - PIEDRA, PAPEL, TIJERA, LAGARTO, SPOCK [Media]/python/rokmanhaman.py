
"""Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */"""


def who_win(games):

    rules_win = {
    "ROCK" : ["SCISSORS", "LIZARD"],
    "PAPER" : ["ROCK", "SPOCK"],
    "SCISSORS" : ["PAPER", "LIZARD"],
    "SPOCK" : ["ROCK", "SCISSORS"],
    "LIZARD" : ["PAPER", "SPOCK"]
    }

    pp1 = 0 # puntos player 1
    pp2 = 0 # puntos player 2
    for game in games:
        if game[0] != game[1]:
            if game[1] in rules_win[game[0]]:
                pp1 +=1
            else:
                pp2 +=1
        print(f"{pp1} a {pp2}")



    return "Tie" if pp1 == pp2 else "Player 1" if pp1 > pp2 else "Player 2"
 

print(who_win([("SCISSORS", "LIZARD"), ("PAPER", "LIZARD"), ("ROCK", "SCISSORS"), ("ROCK", "SCISSORS"), ("ROCK", "SCISSORS")]))                






