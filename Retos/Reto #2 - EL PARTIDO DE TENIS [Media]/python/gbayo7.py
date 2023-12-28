# 
# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
# 
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.   
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
# 
from enum import Enum
class player(Enum):
    P1 = 1,
    P2 = 2

def tennisGame(plays:list):
    output = ''
    #Players points buffer
    last_P1 = 0 
    last_P2 = 0
    #Flag to indicate i there is a winner
    finished = False
    win_msg= 'Ha ganado '

    #iterate trough the points
    for index, winner in enumerate(plays):
        #Chek winner of the play
        if(winner == player.P1):
            if(last_P1 == 0):
                last_P1 = 15
            elif(last_P1 == 15):
                last_P1 = 30
            elif(last_P1 == 30):
                last_P1 = 40
            elif(last_P1 == 40):
                if(last_P2 != 40 and last_P2 != 50): #50 represents advantage
                    finished = True
                    win_msg += 'P1'
                elif(last_P2 == 50): #If the other playeras advantage both counters are reset to 40
                    last_P1 = 40
                    last_P2 = 40
                elif(last_P2 == 40): #If the other player is 40 winner gets advantage
                    last_P1 = 50
            elif(last_P1 == 50): #If there is a win with an advantage the player takes the win
                finished = True
                win_msg += 'P1'
        elif(winner == player.P2):
            if(last_P2 == 0):
                last_P2 = 15
            elif(last_P2 == 15):
                last_P2 = 30
            elif(last_P2 == 30):
                last_P2 = 40
            elif(last_P2 == 40):
                if(last_P1 != 40 and last_P1 != 50):
                    finished = True
                    win_msg += 'P2'
                elif(last_P1 == 50):
                    last_P1 = 40
                    last_P2 = 40
                elif(last_P1 == 40):
                    last_P2 = 50
                elif(last_P2 == 50):
                    finished = True
                    win_msg += 'P2'
        #Check if there is a winner
        if(finished): 
            output += win_msg
            break
        #Change points by representative expressis
        if(last_P1 == 0): p_p1 = 'Love'
        elif(last_P1 == 50): p_p1 = 'Ad P1'
        else: p_p1 = str(last_P1)

        if(last_P2 == 0): p_p2 = 'Love'
        elif(last_P2 == 50): p_p2 = 'Ad P1'
        else: p_p2 = str(last_P2)

        #Check if it's a draw, an advantage or a normal point 
        if(p_p1 == p_p2):
            output += 'Deuce\n'
        elif('Ad' in p_p1):
            output += p_p1 +'\n'
        elif('Ad' in p_p2):
            output += p_p2 + '\n'
        else:
            output += f'{p_p1} - {p_p2}\n'
    #Print the result
    print(output)

def main():
    secuence = [player.P1, player.P1, player.P2, player.P2, player.P1, player.P2, player.P1, player.P1]
    tennisGame(secuence)

main()