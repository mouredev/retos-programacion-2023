def tennisMatch():
    partido = input("Introduzca la secuencia del partido:\n")
    partido = list(partido.split(", "))

    Player1 = 0
    Player2 = 0
    for player in partido:
        if player == "P1":
            Player1 = count_points(Player1)
            get_score_board(Player1, Player2)
        else:
            Player2 = count_points(Player2)
            get_score_board(Player1, Player2)
        
def count_points(player):
    if player < 30:
        player += 15
    else:
        player += 10
    return player

def get_score_board(P1, P2):
    p1_value = P1
    p2_value = P2
    
    if((P1 - P2) == 20):
        return print("Ha ganado el P1")
    elif((P2 - P1) == 20):
        return print("Ha ganado el P2")
    elif(P1 >= 40 and (P1 - P2) >= 10):
        return print(p1_value, "-", p2_value, "Ventaja P1")
    elif(P2 >= 40 and (P2 - P1) >= 10):
        return print(p1_value, "-", p2_value, "Ventaja P2")
    elif(P1 == 0):
        p1_value = "Love"
    elif(P2 == 0):
        p2_value = "Love"
    elif(P1 == P2 and P1 >= 40 ):
        return print("Deuce")
    return print(p1_value, "-", p2_value)

tennisMatch()