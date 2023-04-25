@@ -0,0 +1,71 @@
# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

"""Enunciado       
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

def partido(scores):
    score_p1=0
    score_p2=0
    points=["Love", "15", "30", "40"]
    print("<P1 - P2>")

    for score in scores:

        if score=="P1":
            score_p1+=1
        elif score=="P2":
            score_p2+=1
        else:
            print("Dato invalido, no se puede continuar")
            return()    

        if score_p1 == score_p2 and score_p1 > 0:
            print("Deuce")
        elif score_p1>3 or score_p2>3:

            if score_p1 == score_p2 - 2:
                print("Ganador P2 \n")
                return()

            elif score_p2 == score_p1 - 2:
                print("Ganador P1 \n")
                return()  

            elif score_p1 == score_p2 - 1:
                print("Ventaja P2") 
                continue               

            elif score_p2 == score_p1 - 1:
                print("Ventaja P1")                 
                continue                              

        else:                 
            print(f'{points[score_p1]} - {points[score_p2]}')

if __name__ == '__main__':

    print("Primer partido")
    partido(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1"])
    print("Segundo partido")
    partido(["P2", "P1", "P2", "P2", "P1", "P2"])
    print("Tercer partido")
    partido(["P1", "P2", "P2", "P2", "P1", "P1", "P2", "P1", "P1", "P2", "P1", "P2", "P2", "P2"])
