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

WINS_OVER = {
    "🗿": ["✂️", "🦎"],
    "📄": ["🗿", "🖖"],
    "✂️": ["📄", "🦎"],
    "🦎": ["📄", "🖖"],
    "🖖": ["🗿", "✂️"]
}


def check_winner(lists):
    p1_counter, p2_counter = 0, 0

    for list in lists:
        if len(list) != 2: return "Falta alguno de los datos"

        if list[0] != list[1]:
            if list[1] in WINS_OVER[list[0]]:
                p1_counter += 1
            else:
                p2_counter += 1
        
    if p1_counter != p2_counter:
        if p1_counter > p2_counter: return "Player 1"
        else: return "Player 2"
    else:
        return "Tie"


print(check_winner([["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]]))      # Player 2
print(check_winner([["🗿","✂️"], ["📄","✂️"]]))                   # Tie
print(check_winner([["🗿","🗿"], ["✂️", "📄"]]))                  # Player 1
print(check_winner([["🦎","✂️"], ["🖖","🗿"], ["🖖","✂️"]]))      # Player 1