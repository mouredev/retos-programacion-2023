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

def tennis_game(points: tuple) -> str:

    print("PARTIDO DE TENIS:")
    print("P1 - P2")
    print()

    # Variables que usaremos.
    points_system = {0 : "Love", 1 : "15", 2 : "30", 3 : "40"}
    counter_P1 = 0
    counter_P2 = 0
    winner = ""

    for point in points:
        # Control de errores en los datos.
        if point != "P1" and point != "P2":
            return "No se ha introducido correctamente la secuencia de puntos."

        # Cuenta de puntos.
        if point == "P1": 
            counter_P1 += 1
        else: 
            counter_P2 += 1

        # Impresión de los resultados.
        if (counter_P1 <= 3 and counter_P2 < 3) or (counter_P1 < 3 and counter_P2 <= 3):
            print(f"{points_system[counter_P1]} - {points_system[counter_P2]}")
        elif counter_P1 == counter_P2:
            print("Deuce")
        elif counter_P1 - counter_P2 == 1:
            print("Ventaja P1")
        elif counter_P2 - counter_P1 == 1:
            print("Ventaja P2")
        else:
            if counter_P2>counter_P1: winner = "El ganador es P2"
            else: winner = "El ganador es P1"

    if winner == "":
        return "La longitud de los puntos introducidos no da como resultado un ganador."
    else:
        return winner

def main():
    points = ("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P1", "P1")
    print(tennis_game(points))

if __name__ == "__main__":
    main() 