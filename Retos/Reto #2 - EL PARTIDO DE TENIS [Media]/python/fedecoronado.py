'''/*
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
 */'''
 
secuencia = ['P1', 'P1', 'P2', 'P3', 'P1', 'P1', 'P1', 'P1']
tantos ={0:"Love", 1: "15", 2:"30", 3:"40", 4:"Ventaja "}
# reseteo del game
score = [0,0]
fin = 0

for punto in secuencia:
    if punto == 'P1':
        score[0] += 1
    elif punto == 'P2':
        score[1] += 1
    else:
        print("Error en le ganador del punto")
    if score[0] < 5:
        puntos1 = tantos[score[0]]
    if score[1] < 5:
        puntos2 = tantos[score[1]]
    puntos = puntos1 + " - " + puntos2
    if score[0] > 3 or score[1] > 3:
        if score[0] == score[1]:
            puntos = 'Deuce'
        if score[0] > score[1]:
            puntos = 'Ventaja P1'
        if score[0] < score[1]:
            puntos = 'Ventaja P2'
    if score[0] >= 4 and score[0] - score[1] >= 2:
        puntos = 'Ha ganado el P1'
        fin = 1
    if score[1] >= 4 and score[1] - score[0] >= 2:
        puntos = 'Ha ganado el P2'
        fin = 1
    print(punto, score[0],score[1], puntos)
    if fin == 1:
        break
            

