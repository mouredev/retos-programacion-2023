"""
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

SCORES = ["Love", "15", "30", "40"]


def check_winner(p1: int, p2: int) -> bool:
    if p1 == 3 and p2 == 3:
        print("Deuce")

    elif p1 >= 4 or p2 >= 4:
        point_diff = p1 - p2
        if point_diff == 0:
            print("Deuce")
        elif point_diff == 1:
            print("Ventaja P1")
        elif point_diff == -1:
            print("Ventaja P2")
        elif point_diff >= 2:
            print("Ha ganado el P1")
            return True
        else:
            print("Ha ganado el P2")
            return True

    else:
        print(f"{SCORES[p1]} - {SCORES[p2]}")

    return False


def tennis_match(points: list) -> None:
    p1, p2 = 0, 0
    end_match = False

    for point in points:
        if point == "P1":
            p1 += 1
        elif point == "P2":
            p2 += 1

        end_match = check_winner(p1, p2)

        if end_match: break

tennis_match(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])