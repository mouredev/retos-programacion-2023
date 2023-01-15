def menu():
    print("Inserta el jugador que ha hecho punto: (P1 o P2)")
    player = input()
    return player

def checkPlayer(player):
    playerCorrect = 'false'

    while playerCorrect == 'false':
        if player == "P1":
            playerCorrect = 'true'
        elif player == "P2":
            playerCorrect = 'true'
        else:
            playerCorrect = 'false'
            print("Jugador incorrecto")
            player = menu()
    return player

def resultado(puntos):
    if puntos == 0:
        res = 0
    elif puntos == 1:
        res = 15
    elif puntos == 2:
        res = 30
    elif puntos == 3:
        res = 40
    else:
        res = 50

    return res
    


if __name__ == "__main__":
    puntosP1 = 0
    puntosP2 = 0

    playerCorrect = 'false'
    partidoTerminado = 'false'


    while partidoTerminado == 'false':
        player = menu()
        playerCorrect = checkPlayer(player)

        if playerCorrect == "P1":
            puntosP1 += 1            
        elif playerCorrect == "P2":
            puntosP2 += 1

        resP1 = resultado(puntosP1)
        resP2 = resultado(puntosP2)

        if puntosP1 <= 3 and puntosP2 <= 3:
            if puntosP1 == 3 and puntosP2 == 3:
                print("DEUCE")
            else:
                print(f"Resultado: {resP1}-{resP2}")
        else:
            if puntosP1 == 4 and puntosP2 <= 2:
                print("Gana P1")
                partidoTerminado = 'true'
            elif puntosP2 == 4 and puntosP1 <= 2:
                print("Gana P2")
                partidoTerminado = 'true'
            elif puntosP1 == puntosP2:
                print("DEUCE")
            elif puntosP1 == puntosP2 + 2:
                print("Gana P1")
                partidoTerminado = 'true'
            elif puntosP2 == puntosP1 + 2:
                print("Gana P2")
                partidoTerminado = 'true'
            elif puntosP1 < puntosP2:
                print("Ventaja P2")
            elif puntosP2 < puntosP1:
                print("Ventaja P1")
