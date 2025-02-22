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




def score(juegos):

    puntajes = ['love', '15' ,'30', '40']
    score_pl1 = 0
    score_pl2 = 0
    for player in juegos:
        if player == 'P1':
            score_pl1 += 1
        else:
            score_pl2 +=1
        if abs(score_pl1-score_pl2) == 2 and (score_pl1 >= 4 or score_pl2 >= 4):
            ganador = 'P1' if score_pl1 > score_pl2 else 'P2'
            print(f'El ganador es {ganador}')
            return
        elif score_pl1 >= 3 and score_pl2 >= 3:
            if score_pl1 == score_pl2:
                print(f'deuce')
            else:
                ventaja = 'P1' if score_pl1 > score_pl2 else 'P2'
                print(f'ventaja {ventaja}')
        else:
            print(f'{puntajes[score_pl1]}-{puntajes[score_pl2]}')


score(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])