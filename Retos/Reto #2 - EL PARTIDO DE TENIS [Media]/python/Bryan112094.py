# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.   
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

def tenis(secuencia):
    punto01 = 0
    punto02 = 0
    puntuaciones = ["Love", "15", "30", "40"]
    for x in secuencia:
        if x == 'P1':
            punto01 += 1
        elif x == 'P2':
            punto02 += 1
        else:
            print('Jugador ingresado incorrecto, intentelo denuevo')
            return()
        
        if punto01 > 3 or punto02 > 3:
            if punto01 == punto02:
                print("Deuce")
            elif punto01 - 2 == punto02:
                print('Ha ganado P1')
                return()
            elif punto01 - 1 == punto02:
                print('Ventaja P1')
            elif punto02 - 2 == punto01:
                print('Ha ganado P2')
                return()
            elif punto02 - 1 == punto01:
                print('Ventaja P2')
        elif punto01 == 3 and punto02 == 3 :
            print('Deuce')
        else:
            print(puntuaciones[punto01] + " - " + puntuaciones[punto02])

tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
