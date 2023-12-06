'''
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
'''

#Codigo para borrar la pantalla#
from os import system
system("cls")

# Definimos la función juego, a la que pasamos la tupla
def juego(x):
    puntos_player1 = 0
    puntos_player2 = 0
    for i in range (0,len(x)): # Recorremos la tupla
        if x[i][0] == x[i][1]: # Si ambos jugadores sacan lo mismo no se asigna punto a ninguno
            puntos_player1 += 0 
            puntos_player2 += 0
        # Vemos las diferentes posibilidades en las que ganaría el Player 1
        elif x[i][0] == "🗿" and (x[i][1] != "📄" and x[i][1] != "🖖"):
            puntos_player1 += 1
        elif x[i][0] == "🦎" and (x[i][1] != "✂️" and x[i][1] != "🗿"):
            puntos_player1 += 1
        elif x[i][0] == "🖖" and (x[i][1] != "📄" and x[i][1] != "🦎"):
            puntos_player1 += 1
        elif x[i][0] == "✂️" and (x[i][1] != "🗿" and x[i][1] != "🖖"):
            puntos_player1 += 1
        elif x[i][0] == "📄" and (x[i][1] != "✂️" and x[i][1] != "🦎"):
            puntos_player1 += 1
        else: # Si no gana el Player 1, gana el Player 2
            puntos_player2 += 1
    
    print("")
    print("***Partida finalizada***")
    print (f"   Puntos Player 1: {puntos_player1}")
    print (f"   Puntos Player 2: {puntos_player2}")
    if puntos_player1>puntos_player2:
        print("-Ha ganado el Player 1")
    elif puntos_player1<puntos_player2:
        print("-Ha ganado el Player 2")
    else:
        print("-EMPATE")
        

# Definimos tuplas con las diferentes jugadas
jugada_1 = (("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")) # Debería dar ganador Player 2
jugada_2 = (("🗿","🗿"), ("✂️","🗿"), ("📄","✂️"),("🦎","📄"),("🖖","📄"),("🦎","📄"),("🗿","🦎")) # Debería dar Empate
jugada_3 = (("🗿","✂️"), ("📄","🖖"), ("📄","✂️")) # Debería dar ganador Player 1

# Lanzamos las partidas
juego(jugada_1)
juego(jugada_2)
juego(jugada_3)