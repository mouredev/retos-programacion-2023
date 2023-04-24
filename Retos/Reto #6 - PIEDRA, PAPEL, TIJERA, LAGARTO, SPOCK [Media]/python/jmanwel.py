"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
tijera gana a papel y lagarto
papel gana a piedra y spock
piedra gana a lagarto y tijera
lagarto gana a spock y papel
spock gana a tijera y piedra
"""
player_1 = 0
player_2 = 0
reglas = {'🗿': {'✂️', '🦎'},'✂️': {'📄', '🦎'},'📄': {'🗿', '🖖'},'🦎': {'📄', '🖖'},'🖖': {'✂️', '🗿'}}
jugadas = [('🗿', '✂️'), ('🖖', '🗿'), ('📄', '✂️')]

for j in jugadas:
    if j[1] in reglas[j[0]]:
        player_1 += 1
    else:
        player_2 += 1

if player_1 > player_2:
    print('Gana jugador 1')
elif player_2 > player_1:
    print('Gana jugador 2')
else:
    print('Empate')