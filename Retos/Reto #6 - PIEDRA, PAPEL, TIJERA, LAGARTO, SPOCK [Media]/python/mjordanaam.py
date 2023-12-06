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
COMBINATIONS = {
	"🗿": ["🦎", "✂️"],
	"📄": ["🗿", "🖖"],
	"✂️": ["📄", "🦎"],
	"🦎": ["🖖", "📄"],
	"🖖": ["✂️", "🗿"]
}


def get_winner(results: list) -> str:
	p1 = 0
	p2 = 0

	for t in results:
		if t[0] != t[1]:
			if t[1] in COMBINATIONS[t[0]]:
				p1 += 1
			else:
				p2 += 1

	if p1 > p2:
		return "Player 1"
	elif p2 > p1:
		return "Player 2"
	else:
		return "Tie"


print(get_winner([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]))
print(get_winner([("🗿", "🗿"), ("✂️", "✂️"), ("🦎", "🦎")]))
print(get_winner([("✂️", "✂️"), ("🦎", "🖖"), ("🦎", "✂️")]))
print(get_winner([("✂️", "✂️"), ("🦎", "🖖"), ("🗿", "✂️")]))
