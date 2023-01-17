points = ("Love", 15, 30, 40, "Deuce", "Ventaja")
lista = ('P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1')

player1 = 0
player2 = 0

for elemento in lista:
    if elemento == 'P1':
        player1+=1
    elif elemento == 'P2':
        player2+=1

    if player1 >= 3 or player2 >=3:
        ventaja = player1 - player2
        if ventaja == 0:
            print('Duece')
            continue
        elif player1 > 3 or player2 > 3:
            if ventaja == 1:
                print('Ventaja P1')
                continue
            if ventaja == -1:
                print('Ventaja P2')
                continue
            if ventaja == 2:
                print('Ha ganado P1')
                continue
            if ventaja == -2:
                print('Ha ganado P2')
            
    
    print('{} - {}'.format(points[player1], points[player2])) 

    


            
            
            