"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
 - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 - La función recibe un listado que contiene pares, representando cada jugada.
 - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

from enum import Enum


class Sign(Enum):
    Piedra = "🗿"
    Papel = "📄"
    Tijera = "✂️"
    Lagarto = "🦎"
    Spock = "🖖"


object_wins = {
    Sign.Piedra: (Sign.Tijera, Sign.Lagarto),
    Sign.Papel: (Sign.Piedra, Sign.Spock),
    Sign.Tijera: (Sign.Papel, Sign.Lagarto),
    Sign.Lagarto: (Sign.Papel, Sign.Spock),
    Sign.Spock: (Sign.Piedra, Sign.Tijera),
}


def player_wins(player_eval, oponent):
    return oponent in object_wins[player_eval]


def game(plays=[]):
    p1_points, p2_points = 0, 0

    for play in plays:
        if len(play) != 2:
            continue

        p1, p2 = play

        if player_wins(p1, p2):
            p1_points += 1

        if player_wins(p2, p1):
            p2_points += 1

    return "Player 1" if p1_points > p2_points else ("Player 2" if p2_points > p1_points else "Tie")


if __name__ == "__main__":
    print(game([(Sign.Piedra, Sign.Tijera),
          (Sign.Tijera, Sign.Piedra), (Sign.Papel, Sign.Tijera)]))

    print(game([(Sign.Piedra, Sign.Tijera)]))
