

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


def get_result( game: list ) -> None:
    '''
    Parameter : game es una lista de ganador de cada set
    La función recorre cada item de la lista, con el cual se pasa a la función que calcula el score.
    '''
    score = [ 'love', 'love' ]
    for player in game:
        print(player)
        get_score2(player, score)
        print(score)

def get_score2(player:str , score: list)->None:
    '''
        Parameter : 
            player  : jugador ganador del set
            score   : resultado del score anterior. Es una lista con dos items, [0] para el jugador 1 y [1] para el jugador 2
        Función : Toma el score anterior del jugador y lo aumenta. Teniendo en consideración si el resultado es un empate, ventaja.
    '''
  
    if 'p1' == player:
        i = 0
        n = 1
    else:
        i = 1
        n = 0 
    
    if score[i] == 'love':
        score[i] = '15'
    elif score[i] == '15':
        score[i] = '30'
    elif score[i] == '30':
        score[i] = '40'
    elif score[i] == '40':
        score[i] = 'Ha ganado '+player
    elif score[i] == 'Deuce' or score[i] == '-':
        score[i] = 'Ventaja '+player
    elif 'Ventaja' in score[i]:
        score[i] = 'Ha ganador '+player
        
    
    if (score[i] == '40' and score[n] == '40' or 'Ventaja' in score[i]  and 'Ventaja' in score[n]):
        score[i] = 'Deuce'
        score[n] = 'Deuce'
    
    if ('Ventaja' in score[i]  and 'Deuce' in score[n] ):
        score[n] = '-'
        


if __name__ == "__main__":
    listado = ['p2', 'p2', 'p1', 'p1', 'p2', 'p1', 'p2', 'p1','p1','p1','p1','p1','p1']
    get_result(listado)