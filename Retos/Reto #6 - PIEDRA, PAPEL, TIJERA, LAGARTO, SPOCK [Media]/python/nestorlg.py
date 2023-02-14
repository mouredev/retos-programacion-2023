def quienGanaMas(partidas):
    win1 = 0
    win2 = 0
    for partida in partidas:
        if (partida[0] == "piedra"):
            if (partida[1] == "tijera" or partida[1] == "lagarto"):
                win1 += 1
            elif (partida[1] == "papel" or partida[1] == "spock"):
                win2 += 1
            else:
                if (partida[1] != "piedra"):
                    print("ERROR: no se reconoce la jugada", partida[1])
                    return
                
        elif (partida[0] == "papel"):
            if (partida[1] == "piedra" or partida[1] == "spock"):
                win1 += 1
            elif (partida[1] == "tijera" or partida[1] == "lagarto"):
                win2 += 1
            else:
                if (partida[1] != "papel"):
                    print("ERROR: no se reconoce la jugada", partida[1])
                    return
            
        elif (partida[0] == "tijera"):
            if (partida[1] == "papel" or partida[1] == "lagarto"):
                win1 += 1
            elif (partida[1] == "piedra" or partida[1] == "spock"):
                win2 += 1
            else:
                if (partida[1] != "tijera"):
                    print("ERROR: no se reconoce la jugada", partida[1])
                    return
            
        elif (partida[0] == "lagarto"):
            if (partida[1] == "papel" or partida[1] == "spock"):
                win1 += 1
            elif (partida[1] == "piedra" or partida[1] == "tijera"):
                win2 += 1
            else:
                if (partida[1] != "lagarto"):
                    print("ERROR: no se reconoce la jugada", partida[1])
                    return
            
        elif (partida[0] == "spock"):
            if (partida[1] == "piedra" or partida[1] == "tijera"):
                win1 += 1
            elif (partida[1] == "papel" or partida[1] == "lagarto"):
                win2 += 1
            else:
                if (partida[1] != "spock"):
                    print("ERROR: no se reconoce la jugada", partida[1])
                    return
            
        else:
            print("ERROR: no se reconoce la jugada", partida[0])
            return
        
            
    if (win1 > win2):
        print("Player 1")
    elif (win1 < win2):
        print("Player 2")
    else:
        print("Tie")

quienGanaMas([["piedra", "papel"], ["piedra", "tijera"], ["tijera", "papel"]])
quienGanaMas([["papel", "papel"], ["piedra", "lagarto"], ["tijera", "spock"], ["tijera", "tijera"]])
quienGanaMas([["papel", "tijera"], ["piedra", "piedra"], ["papel", "spock"], ["spock", "lagarto"], ["lagarto", "lagarto"]])
