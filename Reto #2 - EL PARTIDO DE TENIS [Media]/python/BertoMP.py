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


def dime_jugador():
    jugador_check = input("¿Quién ha ganado el punto? (P1 o P2)\n").upper()
    while jugador_check != "P1" and jugador_check != "P2":
        print("Has introducido un jugador no válido (Introduce P1 o P2)")
        jugador_check = input("¿Quién ha ganado el punto? (P1 o P2)")
    return jugador_check


def dime_marcador(puntuacion_p1, puntuacion_p2):
    puntuaciones_posibles = ["Love", "15", "30", "40"]

    if puntuacion_p1 == 3 and puntuacion_p2 == 3:
        print("Deuce")
    elif puntuacion_p1 >= 4 or puntuacion_p2 >= 4:
        diferencia_puntos = puntuacion_p1 - puntuacion_p2
        if diferencia_puntos == 0:
            print("Deuce")
        elif diferencia_puntos == 1:
            print("Ventaja P1")
        elif diferencia_puntos == -1:
            print("Ventaja P2")
        elif diferencia_puntos >= 2:
            print("Ha ganado el P1")
            return True
        else:
            print("Ha ganado el P2")
            return True
    else:
        print(f"{puntuaciones_posibles[puntuacion_p1]} - {puntuaciones_posibles[puntuacion_p2]}")
    return False


def juego_tenis():
    puntuacion_p1 = 0
    puntuacion_p2 = 0
    juego_finalizado = False

    while not juego_finalizado:
        jugador_punto = dime_jugador()
        match jugador_punto:
            case "P1":
                puntuacion_p1 += 1
            case "P2":
                puntuacion_p2 += 1
        juego_finalizado = dime_marcador(puntuacion_p1, puntuacion_p2)


juego_tenis()
