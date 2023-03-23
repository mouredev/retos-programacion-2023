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
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''

puntuacion_P1 = [0]
puntuacion_P2 = [0]

cantidad_juegos = 1

def marcador():
    global cantidad_juegos
    cantidad_juegos += 1
    print(puntuacion_P1)
    print(puntuacion_P2)

while cantidad_juegos:
    ganador_juego = input(f"Ganador del punto #{cantidad_juegos}? ")
    if ganador_juego == "P1":
        if puntuacion_P1[-1] == 0:
            puntuacion_P1.append(15)
            puntuacion_P2.append(puntuacion_P2[-1])
            marcador()
        elif puntuacion_P1[-1] == 15:
            puntuacion_P1.append(30)
            puntuacion_P2.append(puntuacion_P2[-1])
            marcador()
        elif puntuacion_P1[-1] == 30 and puntuacion_P2[-1] == 40:
            puntuacion_P1.append(40)
            puntuacion_P2.append(40)
            marcador()
        elif puntuacion_P1[-1] == 30:
            puntuacion_P1.append(40)
            puntuacion_P2.append(puntuacion_P2[-1])
            marcador()
        elif puntuacion_P1[-1] == 40 and puntuacion_P2[-1] == 40:
            puntuacion_P1.append("Ventaja P1")
            puntuacion_P2.append("")
            marcador()
        elif puntuacion_P2[-1] == "Ventaja P2":
            puntuacion_P2.remove("Ventaja P2")
            puntuacion_P1.remove("")
            marcador()
        elif puntuacion_P1[-1] == "Ventaja P1":
            puntuacion_P1.append("Victoria P1")
            puntuacion_P2.append("")
            marcador()
            break
        elif puntuacion_P1[-1] == 40:
            puntuacion_P1.append("Victoria P1")
            puntuacion_P2.append("")
            marcador()
            break
        else:
            print("se acabó")
        
    elif ganador_juego == "P2":
        if puntuacion_P2[-1] == 0:
            puntuacion_P2.append(15)
            puntuacion_P1.append(puntuacion_P1[-1])
            marcador()
        elif puntuacion_P2[-1] == 15:
            puntuacion_P2.append(30)
            puntuacion_P1.append(puntuacion_P1[-1])
            marcador()
        elif puntuacion_P2[-1] == 30 and puntuacion_P1[-1] == 40:
            puntuacion_P2.append(40)
            puntuacion_P1.append(40)
            marcador()
        elif puntuacion_P2[-1] == 30:
            puntuacion_P2.append(40)
            puntuacion_P1.append(puntuacion_P1[-1])
            marcador()
        elif puntuacion_P2[-1] == 40 and puntuacion_P1[-1] == 40:
            puntuacion_P2.append("Ventaja P2")
            puntuacion_P1.append("")
            marcador()
        elif puntuacion_P1[-1] == "Ventaja P1":
            puntuacion_P1.remove("Ventaja P1")
            puntuacion_P2.remove("")
            marcador()
        elif puntuacion_P2[-1] == "Ventaja P2":
            puntuacion_P2.append("Victoria P2")
            puntuacion_P1.append("")
            marcador()
            break
        elif puntuacion_P2[-1] == 40:
            puntuacion_P2.append("Victoria P2")
            puntuacion_P1.append("")
            marcador()
            break
        else:
            print("se acabó")
    else:
        print("Porfavor introduce P1 o P2")


def puntuacion_final():
    puntuacion_P1.pop(0)
    puntuacion_P2.pop(0)
    print("\nLa puntuacion final del partido es:")
    print(" P1 -- P2")
    
    for i in range(len(puntuacion_P1)):
        if puntuacion_P1[i] == 0:
            puntuacion_P1[i] = "love"
        if puntuacion_P2[i] == 0:
            puntuacion_P2[i] = "love"

        if puntuacion_P1[i] == 40 and puntuacion_P2[i] == 40:
            print("Deuce")
        elif puntuacion_P1[i] == "":
            print(puntuacion_P2[i])
        elif puntuacion_P2[i] == "":
            print(puntuacion_P1[i])      
        else:  
            print(puntuacion_P1[i], " -- ", puntuacion_P2[i])

puntuacion_final()