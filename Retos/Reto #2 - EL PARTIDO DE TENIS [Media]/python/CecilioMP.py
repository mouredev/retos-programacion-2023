"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Ventaja P1
Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

def juego_tenis(secuencia: list):
    puntuacionP1 = 0
    puntuacionP2 = 0
    puntuaciones = ("Love", "15", "30", "40")

    for punto in secuencia:
        if punto == "P1":
            if puntuacionP1 == 3 and puntuacionP2 == 4:
                puntuacionP2 = 3
            else:
                puntuacionP1 += 1
        elif punto == "P2":
            if puntuacionP1 == 4 and puntuacionP2 == 3:
                puntuacionP1 = 3
            else:
                puntuacionP2 += 1

        if puntuacionP1 == 3 and puntuacionP2 == 3:
            print("Deuce")
        elif puntuacionP1 == 4 and puntuacionP2 == 3:
            print("Ventaja P1")
        elif puntuacionP1 == 3 and puntuacionP2 == 4:
            print("Ventaja P2")
        elif puntuacionP1 == 5:
            print("Ha ganado el P1")
            break
        elif puntuacionP2 == 5:
            print("Ha ganado el P2")
            break
        else:
            print(f"{puntuaciones[puntuacionP1]} - {puntuaciones[puntuacionP2]}")

juego_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
