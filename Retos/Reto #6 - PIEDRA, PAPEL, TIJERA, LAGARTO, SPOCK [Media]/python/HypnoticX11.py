partida = []
ronda = []
Nrondas = 0

def Resultado(partida):
    P1 = 0
    P2 = 0
    for i in range(0,len(partida)):
        if partida[i][0] == "πΏ":
            if partida[i][1] == "βοΈ" or partida[i][1] == "π¦":
                P1 += 1
            elif partida[i][0] == "πΏ" and partida[i][1] == "πΏ":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "π":
            if partida[i][1] == "πΏ" or partida[i][1] == "π":
                P1 += 1
            elif partida[i][0] == "π" and partida[i][1] == "π":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "βοΈ":
            if partida[i][1] == "π" or partida[i][1] == "π¦":
                P1 += 1
            elif partida[i][0] == "βοΈ" and partida[i][1] == "βοΈ":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "π¦":
            if partida[i][1] == "π" or partida[i][1] == "π":
                P1 += 1
            elif partida[i][0] == "π¦" and partida[i][1] == "π¦":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "π":
            if partida[i][1] == "πΏ" or partida[i][1] == "βοΈ":
                P1 += 1
            elif partida[i][0] == "π" and partida[i][1] == "π":
                P1 += 1
                P2 += 1
            else:
                P2 += 1

    if P1 == P2:
        return("Tie")
    elif P1 > P2:
        return("Player 1")
    else:
        return("Player 2")

Nrondas = int(input("NΓΊmero de rondas: "))
print("Juego πΏ (piedra), π (papel), βοΈ (tijera), π¦ (lagarto), π (spock) a ", Nrondas , "rondas.")

for i in range(1,(Nrondas+1)):
    print(" --------- ")
    print("| Ronda", i ,"|")
    print(" --------- ")
    ronda.append(input("Jugador 1: "))
    ronda.append(input("Jugador 2: "))
    partida.append(ronda)
    ronda = []

print(Resultado(partida))