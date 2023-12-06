'''
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
'''
P1 = 1
P2 = 2
def match_tennis(sets : list):
    puntaje = ["Love",15,30,40,"Deuce"]
    finished : bool = False
    countP1 : int = 0
    countP2 : int = 0 
    for set in sets:
        if set == P1: countP1 += 1
        elif set == P2: countP2 += 1 
        #5-3 = 2
        if(countP1 >= 3 and countP2 >= 3):#5 - 3 -> 60 - 40
            if(not finished and abs(countP1 - countP2) <= 1):
                if(countP1 - countP2 == 0):
                    print(f"{puntaje[4]}")
                if(countP2 > countP1):
                    print("Ventaja P2")
                elif(countP2 < countP1):
                    print("Ventaja P1")
            else:
                finished = True
                if countP1 == 5: print("Ha ganado P1") 
                else: print("Ha ganado P2")
        
        else:
            if(not finished):
                print(f"{puntaje[countP1]} - {puntaje[countP2]}")

match_tennis([P1, P1, P2, P2, P1, P2, P1, P1])
match_tennis([P2, P2, P1, P1, P2, P1, P2, P2])
match_tennis([P1, P2, P1, P1, P2, P2, P1, P2,P2,P2])