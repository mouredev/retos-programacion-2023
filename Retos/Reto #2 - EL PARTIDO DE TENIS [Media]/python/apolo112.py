"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
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

def tennis_match(seq):
    """
    Se introduce una secuencia del partido a la función y esta imprimirá los resultados. 
    """

    points = ['Lovre','15', '30', '40']
    p ={'P1':[points[0],0], 'P2':[points[0],0]}
    
    for ball in seq:
        if p[ball][0] != points[3]:
            p[ball][1] += 1
            p[ball][0] = points[p[ball][1]]
            if p['P1'][0] == points[3] and p['P2'][0] == points[3]:
                print('Deuce')

            else: print(p['P1'][0] + ' - ' + p['P2'][0])

        else:
            p[ball][1] +=1

            if p['P1'][1] == p['P2'][1]:
                print('Deuce')
            elif p['P1'][1] > p['P2'][1]:
                if p['P1'][1] - p['P2'][1] == 1:
                    print('Ventaja P1')
                else: print( 'Ha ganado P1')
            elif p['P2'][1] > p['P1'][1]:
                if p['P2'][1] - p['P1'][1] == 1:
                    print('Ventaja P2')
                else: print( 'Ha ganado P2')




seq = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
tennis_match(seq)
print('')

seq_1 = ['P1','P2','P2','P1','P2', 'P2']
tennis_match(seq_1)
print('')
seq_2 = ['P1','P2','P2','P1','P2', 'P1','P2','P1','P2']
tennis_match(seq_2)
print('')
seq_1 = ['P1','P2','P2','P1','P2', 'P1','P2','P1','P1','P1']
tennis_match(seq_1)