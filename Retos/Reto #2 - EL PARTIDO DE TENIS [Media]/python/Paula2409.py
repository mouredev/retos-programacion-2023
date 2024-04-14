"""
## Enunciado
```
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
```
"""

def tennis_game(secuence: list):
    """ Simulates a tennis game based on a sequence of points played by two players.
    
    Args:
        secuence (list): a list of points
    
    Returns:
        None
    """

    score_P1 = 'Love'
    score_P2 = 'Love'
    deuce = ''
    ad_in = ''
    win = ''
    
    for point in secuence:
        if point == 'P1':
            if score_P1 == 'Love':
                score_P1 = 15
            elif score_P1 == 15:
                score_P1 = 30
            elif score_P1 == 30:
                if score_P2 == 40:
                    deuce = 'Deuce'
                score_P1 = 40
            elif score_P1 == 40:
                if score_P2 < 40 or ad_in == 'Ventaja P1':
                    win = 'Ha ganado el P1'
                elif score_P2 == 40:
                    ad_in = 'Ventaja P1'
                    
        if point == 'P2':
            if score_P2 == 'Love':
                score_P2 = 15
            elif score_P2 == 15:
                score_P2 = 30
            elif score_P2 == 30:
                if score_P1 == 40:
                    deuce = 'Deuce'
                score_P2 = 40
            elif score_P2 == 40:
                if score_P1 < 40 or ad_in == 'Ventaja P2':
                    win = 'Ha ganado el P2'
                elif score_P1 == 40:
                    ad_in = 'Ventaja P2'

        if deuce:
            print(deuce)
            deuce = ''
        elif win:
            print(win)
            break
        elif ad_in:
            print(ad_in)
        else:
            print(f'{score_P1} - {score_P2}')        
            
tennis_game(['P1','P1','P2','P2','P1','P2','P1','P1'])
