# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */


PUNTUACIONES = ["Love", "15", "30",  "40"]


def jugar_juego():
    cuenta_p1 = 0
    cuenta_p2 = 0
    deuce = False
    seguir_jugando_juego = True

    while seguir_jugando_juego:
        print("¿Quién marcó?")
        tanto = input("pulsa 1 si marcó P1 y 2 si marcó P2: \n")
        if tanto not in ["1", "2"]:
            print("Entrada inválida. Por favor, introduce 1 o 2.")
            continue

        if (tanto == "1"):
            cuenta_p1 += 1
            print("Tanto para el jugador 1!")
        elif (tanto == "2"):
            cuenta_p2 += 1
            print("Tanto para el jugador 2!")


        if (cuenta_p1 < 4 and cuenta_p2 < 4):
            print("-"*40)
            print(f"Jugador 1 =  {PUNTUACIONES[cuenta_p1]} || Jugador 2 = {PUNTUACIONES[cuenta_p2]}")
            print("-"*40)

        if(cuenta_p1 >= 3 and cuenta_p2 >= 3 and cuenta_p1 == cuenta_p2 ):
            print("-"*40)
            print("Hay Deuce entre los jugadores")
            print("-"*40)
            deuce = True
        if (deuce and cuenta_p1 - 1 == cuenta_p2):
            print("-"*40)
            print("Hay ventaja para el jugador 1, siguen en Deuce")
            print("-"*40)
        elif (deuce and cuenta_p2 - 1 == cuenta_p1):
            print("-"*40)
            print("Hay ventaja para el jugador 2, siguen en Deuce")
            print("-"*40)

        elif (deuce and (cuenta_p1-1) > cuenta_p2):
            print("+"*40)
            print("Juego terminadoo! Gana el jugador 1!")
            print("+"*40)
            seguir_jugando_juego = False
        elif (deuce and (cuenta_p2-1) > cuenta_p1):
            print("+"*40)
            print("Juego terminadoo! Gana el jugador 2!")
            print("+"*40)
            seguir_jugando_juego = False


if __name__ == "__main__":
    print("+"*40)
    print("Bienvenidos al partido de tenis. ")
    print("+"*40)
    jugar_juego()
