"""/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
"""

puntuacion = {0:"Love", 1:"15", 2:"30", 3:"40"}
player1 = 0
player2 = 0

secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

for i in secuencia:
    if i == "P1":
        player1 = player1+1
    else:
        player2 = player2+1
    
    if player1 == 3 and player2 == 3: 
        print("Deuce")  
    elif player1 >= 4 or player2 >= 4:
        diff = player1 - player2
        if diff == 0: 
            print("Deuce")
        elif diff == 1: 
            print("Ventaja P1")
        elif diff == -1: 
            print("Ventaja P2")
        elif diff >= 2: 
            print("Ha ganado el P1")
            
        else: print("Ha ganado P2")
    else:
        print(f"{puntuacion[player1]} - {puntuacion[player2]}")