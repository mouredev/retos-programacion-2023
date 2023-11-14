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

def control():
    p1=0
    p2=0
    win = ""
    while win == "":
        point_g = point()

        if point_g == "p1":
            p1 = p1+ 1
        else:
            p2 += 1
        win = tennis_game(p1,p2)
        print(win)
        

def point():
    point_p = input("Que jugador obtiene un punto?")
    if point_p == "p1" or point_p == "p2":
        return point_p
    else:
        print("El punto no es valido.")
        return point

def tennis_game(p1,p2):
    puntaje = ["Love", "15", "30", "40"]
    if p1 == 3 and p2 == 3:
        print("Deuce")
    elif p1 >= 4 or p2 >= 4:
        resto = p1 - p2
        if resto == 0:
            print("Deuce")
        elif resto == 1:
            print("Ventaja P1")
        elif resto == -1:
            print("Ventaja P2")
        elif resto >= 2:
            print("Ha ganado P1")
            return "P1"
        else:
            print("Ha ganado P2")
            return "P2"
    else:
        print(f"{puntaje[p1]} - {puntaje[p2]}")
    return ""


control()