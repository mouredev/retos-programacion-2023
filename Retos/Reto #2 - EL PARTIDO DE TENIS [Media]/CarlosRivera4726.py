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
 */
 '''



#6 puntuaciones -> 0,1,2,3,4,5
PUNTUACIONES = ("Love", "15", "30", "30", "Deuce", "Ventaja")




def imprimirPuntuaciones(puntuaciones1, puntuaciones2):
    limite = 4
    if puntuaciones1 == limite and puntuaciones2 == limite:
        print("Deuce")

    elif puntuaciones1 >= limite or puntuaciones2 >= limite:
        puntos = puntuaciones1 - puntuaciones2
        if puntos == 0:
            print("Deuce")
        elif puntos == 1:
            print("Ventaja P1")
        elif puntos == -1:
            print("Ventaja P2")
        elif puntos >= 2:
            print("Ha ganado el P1")
            return
        else:
            print("Ha ganado el P2")
            return
            

    else:
        print(f"{PUNTUACIONES[puntuaciones1]} - {PUNTUACIONES[puntuaciones2]}")



puntuacionP1 = 0
puntuacionP2 = 0
def anotador(equipo):
    global puntuacionP1, puntuacionP2
    if(equipo == 'P1'):
        puntuacionP1 += 1
    elif equipo == 'P2':
        puntuacionP2 += 1

    imprimirPuntuaciones(puntuacionP1, puntuacionP2)
    

def main():
    lista_secuencia = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
    for secuencia in lista_secuencia:
        anotador(secuencia)


if __name__ == '__main__':
    main()
