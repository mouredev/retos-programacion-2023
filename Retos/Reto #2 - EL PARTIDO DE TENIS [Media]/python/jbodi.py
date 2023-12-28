# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

## Enunciado

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
#[P1, P1, P2, P2, P1, P2, P1, P2, P1, P2, P2, P2, P2, P2] 
#[P1, P1, P2, P2, P1, P2, P1, P1]
def printPuntos(punto):
    if puntosP1 > 3 and (puntosP1 - puntosP2) > 1:
        print("Ha ganado el P1")
        exit()

    if puntosP2 > 3 and (puntosP2 - puntosP1) > 1:
        print("Ha ganado el P2")
        exit()
    
    if punto == "P1" and puntosP1 > 3 and (puntosP1 - puntosP2) == 1:
        print("Ventaja P1")

    elif punto == "P2" and puntosP2 > 3 and (puntosP2 - puntosP1) == 1:
        print("Ventaja P2")
    
    elif puntosP1 == puntosP2 and puntosP1 >= 3:
        print("Deuce")

    else:
        resultadoP1 = puntuaciones[puntosP1]
        resultadoP2 = puntuaciones[puntosP2]
        print(f"{resultadoP1} - {resultadoP2}")

puntuaciones = {
    0 : "Love",
    1 : "15",
    2 : "30",
    3 : "40"
}
juego = input("Inserte la secuencia del juego [PX,]: ")
puntosP1 = 0
puntosP2 = 0

for punto in juego[1:-1].split(", "):
    if punto == "P1":
        puntosP1 += 1

    if punto == "P2":
        puntosP2 += 1
        
    printPuntos(punto)