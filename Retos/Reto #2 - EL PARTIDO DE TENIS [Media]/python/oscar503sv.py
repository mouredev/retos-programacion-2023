'''
* Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
* El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
* gane cada punto del juego.
*
* - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
* - Ante la secuencia[P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
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
'''

def calcular_puntuacion(puntuacion):
    if puntuacion == 0:
        return "Love"
    elif puntuacion == 1:
        return 15
    elif puntuacion == 2:
        return 30
    elif puntuacion == 3:
        return 40
    else:
        return "Ventaja"

def mostrar_puntuacion(p1_puntuacion, p2_puntuacion):
    if p1_puntuacion >= 3 and p2_puntuacion >= 3:
        if p1_puntuacion == p2_puntuacion:
            return "Deuce"
        elif p1_puntuacion > p2_puntuacion:
            return "Ventaja P1"
        else:
            return "Ventaja P2"
    else:
        return f"{calcular_puntuacion(p1_puntuacion)} - {calcular_puntuacion(p2_puntuacion)}"
    
def jugar_tenis(secuencia):
    p1_puntuacion = 0
    p2_puntuacion = 0

    for punto in secuencia:
        if punto == "P1":
            p1_puntuacion += 1
        elif punto == "P2":
            p2_puntuacion += 1
        else:
            print("Error: Entrada inválida")
            return

        puntuacion_actual = mostrar_puntuacion(p1_puntuacion, p2_puntuacion)
        print(puntuacion_actual)

        if puntuacion_actual == "Ventaja P1":
            print("Ha ganado el P1")
            return
        elif puntuacion_actual == "Ventaja P2":
            print("Ha ganado el P2")
            return

secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
jugar_tenis(secuencia)
