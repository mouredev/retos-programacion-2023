"""
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
tijera gana a papel y lagarto
papel gana a piedra y spock
piedra gana a lagarto y tijera
lagarto gana a spock y papel
spock gana a tijera y piedra
"""
player_1 = 0
player_2 = 0
reglas = {'πΏ': {'βοΈ', 'π¦'},'βοΈ': {'π', 'π¦'},'π': {'πΏ', 'π'},'π¦': {'π', 'π'},'π': {'βοΈ', 'πΏ'}}
jugadas = [('πΏ', 'βοΈ'), ('π', 'πΏ'), ('π', 'βοΈ')]

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