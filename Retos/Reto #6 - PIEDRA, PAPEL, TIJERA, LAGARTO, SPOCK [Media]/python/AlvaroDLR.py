""" * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

<NORMAS>
    Las tijeras cortan el papel - Gana: ✂️
    El papel cubre a la piedra - Gana: 📄
    La piedra aplasta las tijeras - Gana: 🗿
    La piedra aplasta al lagarto - Gana: 🗿
    El lagarto envenena a Spock - Gana: 🦎
    Spock destroza las tijeras - Gana: 🖖
    Las tijeras decapitan al lagarto - Gana: ✂️
    El lagarto se come el papel - Gana: 🦎
    El papel desautoriza a Spock - Gana: 📄
    Spock vaporiza la piedra - Gana: 🖖
"""

who_wins = {
    '🗿': ['🦎', '✂️'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['🖖', '📄'],
    '🖖': ['🗿', '✂️'],
}

def match(points: list):
    p1_points = 0
    p2_points = 0

    # print(points)
    for point in points:
        win = point[1] in who_wins[point[0]]
        if win == True:
            # print(f"Ha ganado {point[0]}")
            p1_points += 1
        else:
            # print(f"Ha ganado {point[1]}")
            p2_points += 1
    
    if p1_points > p2_points:
        print(f"Ha ganado Player 1 ({p1_points})")
    elif p2_points > p1_points:
        print(f"Ha ganado Player 2 ({p2_points})")
    else:
        print(f"Tie (empate) {p1_points} -- {p2_points}")

match([("🗿","✂️"), ("🦎","✂️"), ("📄","✂️"), ("🗿","✂️")])