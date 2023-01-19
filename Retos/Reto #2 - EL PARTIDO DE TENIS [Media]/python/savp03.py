""""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.

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
"""

def run ():
    
    punto_jugador1 , punto_jugador2, diferencia = 0 , 0 , 0
    puntos = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"] 
    puntajes = ["Love", "15", "30", "40"]

    for punto in puntos:

        if punto == "P1":
            punto_jugador1 += 1

        elif punto == "P2":
            punto_jugador2 += 1

        if punto_jugador1 == punto_jugador2 == 3:
            print("Deuce")

        elif punto_jugador1 >= 4 or punto_jugador2 >= 4:
            diferencia = punto_jugador1 - punto_jugador2

            if diferencia == 0:
                print("Deuce")

            elif diferencia == 1: 
                print("Ventaja P1")

            elif diferencia == -1: 
                print("Ventaja P2")

            elif diferencia >= 2: 
                print("Ha ganado el P1")
            
            else: print("Ha ganado P2")

        else:
            print(f"{puntajes[punto_jugador1]} - {puntajes[punto_jugador2]}")
        
if __name__ == "__main__":
    run()