'''
/*
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
'''

marcador = ["Love", "15", "30", "40"]

def juego(List):
    player1 = 0
    player2 = 0
    
    for p in List:
        if p == "jugador1": player1 += 1
        elif p == "jugador2": player2 += 1

        if player1 == 3 and player2 == 3: print("Deuce")
        
        elif player1 >= 4 or player2 >= 4:
            puntaje = player1 - player2
            if puntaje == 0: print("Deuce")
            elif puntaje == 1: print("La ventaja es para el Jugador 1")
            elif puntaje == -1: print("La ventaja es para el Jugador 2")
            elif puntaje >= 2: print("El ganador es el Jugador 1")
            
            else: print("El ganador es el Jugador 2")

        else: print(f"Jugador 1: {marcador[player1]} - Jugador 2: {marcador[player2]}")

juego (["jugador1", "jugador1", "jugador2", "jugador2", "jugador1", "jugador2", "jugador1", "jugador1"])
