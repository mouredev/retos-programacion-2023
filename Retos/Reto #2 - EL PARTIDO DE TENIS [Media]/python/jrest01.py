scores = {
        0 : 'Love',
        1 : '15',
        2 : '30',
        3 : '40',
    }

def tennis_game(points):
    
    player1 = 0
    player2 = 0
    resultado = ''

    for point in points:
        if point == 'P1':
            player1 += 1
        elif point == 'P2':
            player2 += 1
        if player1 < 4 and player2 < 4:
            resultado = scores[player1] +" - "+ scores[player2]
        elif player1 == player2:
            resultado = 'Deuce'

        elif player1 > player2:
            if (player1 - player2) == 1:
                resultado = 'Ventaja para 1'
            else:
                resultado = 'Gana 1'
                return
        else:
            if (player2 - player1) == 1:
                resultado = 'Ventaja para 2'
            else:
                resultado = 'Gana 2'
        print(resultado)

points = ["P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2", "P2", "P2",]
tennis_game(points)