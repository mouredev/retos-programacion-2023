import random

def imprimir(p1,p2):
    flag = True;

    if p1 == 0 and p2 ==0:
        print("Love - Love")
    elif p1 == 0 and p2 != 0:
        print(f"Love - {p2}")
    elif p1 != 0 and p2 == 0:
        print(f"{p1} - Love")
    elif p1 == 40 and p2 == 40:
        print('Deuce')
    elif p1 == 50 and p2 == 40:
        print('Ventaja P1')
    elif p2 == 50 and p1 == 40:
        print('Ventaja P2')
    elif p2 == 60 and p1 == 40:
        print('Ha ganado el P1')
        flag = False
    elif p1 == 60 and p2 == 40:
        print('Ha ganado el P2')
        flag = False
    elif p2 == 50 and p1 < 40:
        print('Ha ganado el P2')
        flag =  False
    elif p1 == 50 and p2 < 40:
        print('Ha ganado el P1')
        flag = False
    else:
        print(f"{p1} - {p2}")

    return flag


def tennis():
    player_1 = 0
    player_2 = 0

    while(player_1 <70 and player_2 <70):
        players = [player_1,player_2]

        flag = imprimir(player_1,player_2)

        if(not flag):
            break

        point = random.choice(players)

        if(point == player_1):
            if player_1 >=30:
                player_1 +=10
            else:
                player_1 += 15
        else:
            if player_2 >=30:
                player_2 +=10
            else:
                player_2 += 15
        
        if(player_1 == 50 and player_2 ==50):
            player_1, player_2 = 40,40

tennis()


