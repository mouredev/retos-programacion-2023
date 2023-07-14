''' Reto #6 Piedra, papel, tijera, lagarto, spock

 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''

manos = ['Piedra','Papel','Tijera','Spock','Lagarto']

def game__(opctions):

	dif = manos.index(opctions[1]) - manos.index(opctions[0])

	if (dif == 2) | (dif == 4) | (dif == -1) | (dif == -3):
		return 1
	elif dif == 0:
		return 0
	else:
		return -1

def game(jugadas):
	win_player_1 = 0

	for game in jugadas:
		win_player_1 += game__(game)

	return 'Player 1' if win_player_1 > 0 else 'Player 2' if win_player_1 < 0 else 'Tie'

lista = []
while True:
	a = input('Introduce la opcion de Player 1 --> ')
	b = input('Introduce la opcion de Player 2 --> ')
	lista.append((a,b))

	if input('¿Fin del juego? (y/n) --> ') == 'y':
		break

print(game(lista))