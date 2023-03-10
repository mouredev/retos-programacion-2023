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
COMBINATIONS = {
	"πΏ": ["π¦", "βοΈ"],
	"π": ["πΏ", "π"],
	"βοΈ": ["π", "π¦"],
	"π¦": ["π", "π"],
	"π": ["βοΈ", "πΏ"]
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


print(get_winner([("πΏ", "βοΈ"), ("βοΈ", "πΏ"), ("π", "βοΈ")]))
print(get_winner([("πΏ", "πΏ"), ("βοΈ", "βοΈ"), ("π¦", "π¦")]))
print(get_winner([("βοΈ", "βοΈ"), ("π¦", "π"), ("π¦", "βοΈ")]))
print(get_winner([("βοΈ", "βοΈ"), ("π¦", "π"), ("πΏ", "βοΈ")]))
