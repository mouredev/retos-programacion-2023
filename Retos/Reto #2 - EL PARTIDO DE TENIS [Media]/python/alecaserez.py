"""
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
"""

def tennis_game():
    # Variables
    score = {0:"Love", 1:15, 2:30, 3:40}
    p1 = 0
    p2 = 0
    game = []

    # Input
    while True:
        player = input("\nQuien anoto el punto? P1 o P2: ").upper()

        if player == "P1" or player == "P2":
            match player:
                case "P1":
                    p1 += 1
                case "P2":
                    p2 += 1

            if p1 == 3 and p2 == 3:
                print("Deuce")
                continue

            if p1 == 4 and p2 < 3:
                print("Ha ganado el P1")
                break
            elif p2 == 4 and p1 < 3:
                print("Ha ganado el P2")
                break

            if p1 == 4 and p2 == 3:
                print("Ventaja P1")
                continue
            elif p2 == 4 and p1 == 3:
                print("Ventaja P2")
                continue

            if p1 == 5 and p2 < 4:
                print("Ha ganado el P1")
                break
            elif p2 == 5 and p1 < 4:
                print("Ha ganado el P2")
                break


        else:
            print("Error")
            continue
        
        print(f"{score[p1]} - {score[p2]}")
        
        

tennis_game()