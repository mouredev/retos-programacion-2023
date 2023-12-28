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
winPlayerOne = {
    "🗿": ["✂️", "🦎"],
    "📄": ["🗿", "🖖"],
    "✂️": ["🦎", "📄"],
    "🦎": ["🖖", "📄"],
    "🖖": ["✂️", "🗿"],
}


def game(arr):
    p1 = 0
    p2 = 0
    for e in arr:
        if e[0] != e[1]:
            if e[0] in winPlayerOne and e[1] in winPlayerOne[e[0]]:
                p1 += 1
            else:
                p2 += 1
    if p1 > p2:
        return "Player 1"
    elif p1 < p2:
        return "Player 2"
    else:
        return "Tie"


print(game([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]))
