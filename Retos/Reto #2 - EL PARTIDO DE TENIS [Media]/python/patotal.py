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
"""

def convierte_punto(punto):
    if punto == 0:
        return "Love"
    if punto == 1:
        return "15"
    if punto == 2:
        return "30"
    if punto == 3:
        return "40"

marcador_p1 = 0
marcador_p2 = 0
while True:
    entrada = input(str("Ingrese punto p1 o p2: "))
    if entrada not in ("p1", "p2"):
        print("Valor inválido, vuelva a intentarlo")
        continue
    if entrada == "p1":
        marcador_p1 += 1
    if entrada == "p2":
        marcador_p2 += 1

    if marcador_p1 > 3 and marcador_p2 <= 2:
        print ("P1 ha ganado")
        break
    elif marcador_p2 > 3 and marcador_p1 <= 2:
        print ("P2 ha ganado")
        break
    elif marcador_p1 >= 3 and marcador_p2 >= 3:
        if marcador_p1 == marcador_p2:
            print ("Deuce")
        elif marcador_p1 > marcador_p2:
            if marcador_p1 - marcador_p2 >= 2:
                print ("P1 ha ganado")
                break
            else:
                print("Ventaja P1")
        elif marcador_p2 > marcador_p1:
            if marcador_p2 - marcador_p1 >= 2:
                print ("P2 ha ganado")
                break
            else:
                print("Ventaja P2")
    else:
        print(f"{convierte_punto(marcador_p1)} - {convierte_punto(marcador_p2)}")

