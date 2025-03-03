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

def tenis_game(secuence:list):
    
    #Creamos un set con la lista recibida para verificar que sus dos valores son P1 o P2
    if set(secuence) != {"P1","P2"}:
        print("Secuencia de jugadores incorrecta")
        
    points_p1 = 0
    points_p2 = 0

    
    for player in secuence:
        
        if player == "P1":
            if points_p1 < 30:
                points_p1 += 15  
            else: points_p1 += 10
            
            if points_p1 - points_p2 == 10 and points_p1 > 40:
                print("Ventaja P1")
                continue
            if points_p1 - points_p2 == 20:
                print("Ha ganado el P1")
                break
        else:
            if points_p2 < 30:
                points_p2 += 15
            else: 
                points_p2 += 10

            if points_p2 - points_p1 == 10 and points_p2 > 40:
                print("Ventaja P2")
                continue
            if points_p2 - points_p1 == 20:
                print("Ha ganado el P2")
                break
        
        if points_p1 == points_p2 and points_p1 > 40 and points_p2 > 40:
            print('Deuce')
        else:
            if points_p1 == 0:
                real_point_p1 = "Love"
            else:
                real_point_p1 = points_p1
            if points_p2 == 0:
                real_point_p2 = "Love"
            else:
                real_point_p2 = points_p2
            print(f'{real_point_p1} - {real_point_p2}')
    
        pass

tenis_game(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])