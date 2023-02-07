#
# Manuel C. C. - Proenotec
# 2023/02/06
#
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
 */
"""
# GANA:          1          2            2          1         0          2           2           2          1
partidas = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"),("🦎","📄"),("✂️","✂️"),("🗿","📄"),("🗿","🖖"),("📄","✂️"),("🦎","🖖")]
#partidas = [("🗿","🗿"), ("🦎","🦎"), ("📄","📄"),("🗿","✂️"), ("✂️","🗿")]

relaciones = {"🗿":"✂️🦎","📄":"🗿🖖","✂️":"📄🦎","🦎":"📄🖖","🖖":"✂️🗿"}
puntos_1 = 0
puntos_2 = 0

for jugada in partidas:
    if jugada[0] != jugada[1]:
        if jugada[1] in relaciones[jugada[0]]:
            puntos_1 += 1
        else:
            puntos_2 += 1
print("Player 1 wins") if puntos_1 > puntos_2 else print("Player 2 wins") if puntos_1 < puntos_2 else print("Tie")
