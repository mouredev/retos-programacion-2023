player1 = 0
player2 = 0

point = ["Love", "15", "30", "40"]


players = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2"]



for i in (players):
    
    if i == 'P1':
        player1 += 1  
    elif i == 'P2':
        player2 += 1
    else:
        print('Jugador ingresado incorrecto')

    if player1 > 3 or player2 > 3:
        if player1 == player2:
            print("Deuce")
        elif player1 - player2 == 1:
            print("Ventaja P1")
        elif player1 - player2 == 2:
            print("Gana P1")
        elif player1 - player2 == -1:
            print("Ventaja P2")
        elif player1 - player2 == -2:
            print("Gana P2")
    
    elif player1 == 3 and player2 == 3:
        print("Deuce")
    
    else:
        print(f"{point[player1]} - {point[player2]}")