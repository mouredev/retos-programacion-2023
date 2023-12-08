# Created by luiveldel

#  Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  gane cada punto del juego.
#  
#  - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#     15 - Love
#     30 - Love
#     30 - 15
#     30 - 30
#     40 - 30
#     Deuce
#     Ventaja P1
#     Ha ganado el P1
#   - Si quieres, puedes controlar errores en la entrada de datos.   
#   - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   


from enum import Enum

class Player(Enum):
    P1 = 1
    P2 = 2

def game_results(player_win: list):
    game = ['0', '15', '30', '40']
    score_p1 = 0
    score_p2 = 0
    game_finished = False

    for player in player_win:
        if player == Player.P1:
            score_p1 += 1
        else:
            score_p2 += 1
        
        if score_p1 >= 4 or score_p2 >= 4:
            if abs(score_p1 - score_p2) >= 2:
                game_finished = True
            elif score_p1 == score_p2:
                print("Deuce")
            elif score_p1 > score_p2:
                print("Advantage P1")
            else:
                print("Advantage P2")
        else:
            print(f'{game[score_p1]} - {game[score_p2]}')
    
    if score_p1 > score_p2:
        print("Ha ganado el P1")
    else:
        print("Ha ganado el P2")

game_results([Player.P1, Player.P1, Player.P2, Player.P1, Player.P2, Player.P2, Player.P2, Player.P1, Player.P1])