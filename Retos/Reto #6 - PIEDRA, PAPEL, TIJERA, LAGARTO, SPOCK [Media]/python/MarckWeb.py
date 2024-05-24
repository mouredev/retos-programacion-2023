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


def rpsls_winner(pairs):
    # Define the winning rules
    wins = {
        '🗿': ['✂️', '🦎'],
        '📄': ['🗿', '🖖'],
        '✂️': ['📄', '🦎'],
        '🦎': ['📄', '🖖'],
        '🖖': ['✂️', '🗿']
    }

    player1_wins = 0
    player2_wins = 0

    for p1, p2 in pairs:
        if p1 == p2:
            continue
        elif p2 in wins[p1]:
            player1_wins += 1
        else:
            player2_wins += 1

    if player1_wins > player2_wins:
        return "Player 1"
    elif player2_wins > player1_wins:
        return "Player 2"
    else:
        return "Tie"


# Ejemplo de uso
pairs = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
result = rpsls_winner(pairs)
print(result)  # Resultado: Player 2
