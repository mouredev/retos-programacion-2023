#  Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  gane cada punto del juego.
#  
#  - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#    15 - Love
#    30 - Love
#    30 - 15
#    30 - 30
#    40 - 30
#    Deuce
#    Ventaja P1
#    Ha ganado el P1
#  - Si quieres, puedes controlar errores en la entrada de datos.   
#  - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

player1=["love"]
player2=["love"]
deuce=False
ventajaP1=False
ventajaP2=False

secuencia=["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

for score in secuencia:
    if deuce == True:
        if score == "P1":
            if ventajaP1 == True:
                print("Ha ganado el P1")
                break
            elif ventajaP2 == True:
                print("Deuce")
                ventajaP2=False
            else:
                print("Ventaja P1")
                ventajaP1 = True
        elif score == "P2":
            if ventajaP2 == True:
                print("Ha ganado el P2")
                break
            elif ventajaP1 == True:
                print("Deuce")
                ventajaP1=False
            else:
                print("Ventaja P2")
                ventajaP2 = True
    elif score == "P1":
        if player1[-1] == "40" and player2[-1] != "40":
            print("Ha ganado el P1")
            break
        elif player1[-1] == "love":
            player1.append("15")
        elif player1[-1] == "15":
            player1.append("30")
        elif player1[-1] == "30":
            player1.append("40")
        
    elif score == "P2":
        if player2[-1] == "40" and player1[-1] != "40":
            print("Ha ganado el P2")
            break
        elif player2[-1] == "love":
            player2.append("15")
        elif player2[-1] == "15":
            player2.append("30")
        elif player2[-1] == "30":
            player2.append("40")

    else:
        print("Syntax error.")

    if player1[-1] == "40" and player2[-1] == "40" and ventajaP1 == False and ventajaP2 == False:
        deuce=True
        print("Deuce")
    elif deuce == False:
        print(f"{player1[-1]} - {player2[-1]}")  S