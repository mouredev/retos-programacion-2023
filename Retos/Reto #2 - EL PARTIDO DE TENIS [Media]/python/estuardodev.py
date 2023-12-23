'''
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
    * - Consulta las reglas del juego si tienes dudas sobre el sistema de unidades.   
'''
def game_tennis(plays):
    points = {0: "Love", 1: "Deuce"}

    points_P1 = 0
    points_P2 = 0

    for p in plays:
        if p == "P1":
            if points_P1 < 30:
                points_P1 += 15
            else:
                points_P1 += 10
        elif p == "P2":
            if points_P2 < 30:
                points_P2 += 15
            else:
                points_P2 += 10

        if points_P1 == 0:
            print(f"{points[0]} - {points_P2} - (Ventaja P2)")
        elif points_P2 == 0:
            print(f"{points_P1} - {points[0]} - (Ventaja P1)")
        elif points_P1 == points_P2:
            print(points[1])
        else:
            if points_P1 < points_P2:
                print(f"{points_P1} - {points_P2} - (Ventaja P2)")
            else:
                print(f"{points_P1} - {points_P2} - (Ventaja P1)")

    if points_P1 > points_P2:
        print("Ganador P1")
    elif points_P2 > points_P1:
        print("Ganador P2")
    else:
        print(points[1])


def run():
    plays = ["P1", "P1", "P2", "P1", "P2", "P2", "P2"]
    game_tennis(plays)


if __name__ == "__main__":
    run()