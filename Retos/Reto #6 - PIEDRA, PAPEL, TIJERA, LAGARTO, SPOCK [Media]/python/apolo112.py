"""
```
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
```
"""
"""
spoke gana -> tijera, piedra
lagarto gana -> spoke, papel
tijera gana -> papel, lagarto
papel gana -> piedra, spock
piedra gana -> tijeras, lagarto 
"""

def game_ptls(partida:list):
    l_manos = ['spoke','lagarto','tijera','papel','piedra']
    puntos_j1=0
    puntos_j2=0
    for game in partida:
        j1 = game[0]
        j2 = game[1]

        if j1 == l_manos[0] and (j2 == l_manos[2] or j2 == l_manos[4]):
            puntos_j1 +=1
        elif j1 == l_manos[1] and (j2 == l_manos[0] or j2 == l_manos[3]):
            puntos_j1 +=1
        elif j1 == l_manos[2] and (j2 == l_manos[1] or j2 == l_manos[3]):
            puntos_j1 +=1
        elif j1 == l_manos[3] and (j2 == l_manos[0] or j2 == l_manos[4]):
            puntos_j1 +=1
        elif j1 == l_manos[4] and (j2 == l_manos[1] or j2 == l_manos[2]):
            puntos_j1 +=1
        elif puntos_j1 == j2:
            pass
        else:
            puntos_j2 +=1

    if puntos_j1 > puntos_j2:
        print ("Player 1")
    elif puntos_j1 == puntos_j2:
        print ("Empate")
    else:
        print("Player 2")   





game1 = [("piedra","tijera"),("tijera", "piedra"),("papel", "tijera")]
game_ptls(game1)
game2 =[('spoke','piedra'),('spoke','lagarto')]
game_ptls(game2)