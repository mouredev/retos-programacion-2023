partida = []
ronda = []
Nrondas = 0

def Resultado(partida):
    P1 = 0
    P2 = 0
    for i in range(0,len(partida)):
        if partida[i][0] == "🗿":
            if partida[i][1] == "✂️" or partida[i][1] == "🦎":
                P1 += 1
            elif partida[i][0] == "🗿" and partida[i][1] == "🗿":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "📄":
            if partida[i][1] == "🗿" or partida[i][1] == "🖖":
                P1 += 1
            elif partida[i][0] == "📄" and partida[i][1] == "📄":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "✂️":
            if partida[i][1] == "📄" or partida[i][1] == "🦎":
                P1 += 1
            elif partida[i][0] == "✂️" and partida[i][1] == "✂️":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "🦎":
            if partida[i][1] == "🖖" or partida[i][1] == "📄":
                P1 += 1
            elif partida[i][0] == "🦎" and partida[i][1] == "🦎":
                P1 += 1
                P2 += 1
            else:
                P2 += 1
        if partida[i][0] == "🖖":
            if partida[i][1] == "🗿" or partida[i][1] == "✂️":
                P1 += 1
            elif partida[i][0] == "🖖" and partida[i][1] == "🖖":
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

Nrondas = int(input("Número de rondas: "))
print("Juego 🗿 (piedra), 📄 (papel), ✂️ (tijera), 🦎 (lagarto), 🖖 (spock) a ", Nrondas , "rondas.")

for i in range(1,(Nrondas+1)):
    print(" --------- ")
    print("| Ronda", i ,"|")
    print(" --------- ")
    ronda.append(input("Jugador 1: "))
    ronda.append(input("Jugador 2: "))
    partida.append(ronda)
    ronda = []

print(Resultado(partida))