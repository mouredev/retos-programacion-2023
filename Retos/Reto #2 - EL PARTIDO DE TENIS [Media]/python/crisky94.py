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

def  mostrar_puntos(puntos_p1, puntos_p2):
    puntuaciones = ['Love', '15', '30', '40']

    if puntos_p1 >= 3 or puntos_p2 >= 3:
        if puntos_p1 == puntos_p2:
            return 'Deuce'
        
    if puntos_p1 > 3:
        print('Ventaja P1')
        return 'Ha ganado P1'
    elif puntos_p2 > 3:
        print('Ventaja P2')
        return 'Ha ganado P2'

    return f'{puntuaciones[puntos_p1]} - {puntuaciones[puntos_p2]}'

def jugar_tenis(secuencia):
    puntos_p1 = 0
    puntos_p2 = 0

    for punto in secuencia:
        if punto == "P1":
            puntos_p1 += 1
        elif punto == "P2":
            puntos_p2 += 1
        else :
            print('Error: entrada no valida')
            return
        
        resultado = mostrar_puntos(puntos_p1, puntos_p2)
        print(resultado)

        if 'Ha ganado' in resultado:
            break
        
secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
jugar_tenis(secuencia)