'''
Reto #2: EL PARTIDO DE TENIS

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

def mostrar_marcador(secuencia):
    score_map = {0: "Love", 1: "15", 2: "30", 3: "40"}
    p1_score = 0
    p2_score = 0
    
    for punto in secuencia:
        if punto == "P1":
            p1_score += 1
        elif punto == "P2":
            p2_score += 1
        
        if p1_score >= 3 and p2_score >= 3:
            if p1_score == p2_score:
                print("Deuce")
            elif p1_score == p2_score + 1:
                print("Ventaja P1")
            elif p2_score == p1_score + 1:
                print("Ventaja P2")
            elif p1_score >= p2_score + 2:
                print("Ha ganado el P1")
                break
            elif p2_score >= p1_score + 2:
                print("Ha ganado el P2")
                break
        else:
            if p1_score > 3:
                print("Ha ganado el P1")
                break
            elif p2_score > 3:
                print("Ha ganado el P2")
                break
            else:
                p1_display = score_map[p1_score] if p1_score in score_map else "40"
                p2_display = score_map[p2_score] if p2_score in score_map else "40"
                print(f"{p1_display} - {p2_display}")

secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
mostrar_marcador(secuencia)