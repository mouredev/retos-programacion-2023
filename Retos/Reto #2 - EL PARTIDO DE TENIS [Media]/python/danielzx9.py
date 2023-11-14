"""```
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
```"""

def puntaje(puntos_p1, puntos_p2):
    puntajes = ["Love", "15", "30", "40"]
    if puntos_p1 == puntos_p2:
        if puntos_p1 < 3:
            return f"{puntajes[puntos_p1]} - {puntajes[puntos_p2]}"
        elif puntos_p1 == 3:
            return "Deuce"
        else:
            return "Ventaja"
    elif puntos_p1 >= 4 or puntos_p2 >= 4:
        diferencia = abs(puntos_p1 - puntos_p2)
        if diferencia == 1:
            return f"Ventaja {'P1' if puntos_p1 > puntos_p2 else 'P2'}"
        else:
            return f"Ha ganado el {'P1' if puntos_p1 > puntos_p2 else 'P2'}"
    else:
        return f"{puntajes[puntos_p1]} - {puntajes[puntos_p2]}"

def game(partido):
    p1 = 0
    p2 = 0

    for punto in partido:
        if punto == "P1":
            p1 += 1
        elif punto == "P2":
            p2 += 1
        else:
            print("Entrada no válida")

        resultado = puntaje(p1, p2)
        print(resultado)

        if "Ha ganado" in resultado:
            break

secuenciaJuego = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
game(secuenciaJuego)
