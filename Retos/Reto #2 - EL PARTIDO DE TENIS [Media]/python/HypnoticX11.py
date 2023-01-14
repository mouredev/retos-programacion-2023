N1 = int(0)
N2 = int(0)
Deuce = True
Puntuaciones = ["Love",15,30,40,40]
PuntP1 = ["Love"]
PuntP2 = ["Love"]

while True:
    Punto = str(input("¿Quíen ha marcado Punto?: "))
    if Punto == "P1":
        if Puntuaciones[N1] == 40:
            if PuntP1[len(PuntP1)-1] == "Ventaja P1":
                PuntP1.append("Ha ganado el P1")
                PuntP2.append("Ha ganado el P1")
                break
            elif (PuntP2[len(PuntP2)-1] == "Ventaja P2"):
                PuntP1.append("Deuce")
                PuntP2.append("Deuce")
            else:
                PuntP1.append("Ventaja P1")
                PuntP2.append("Ventaja P1")
        else:
            N1 += 1
            PuntP1.append(Puntuaciones[N1])
            PuntP2.append(Puntuaciones[N2])
    elif Punto == "P2":
        if Puntuaciones[N2] == 40:
            if PuntP2[len(PuntP2)-1] == "Ventaja P2":
                PuntP1.append("Ha ganado el P2")
                PuntP2.append("Ha ganado el P2")
                break
            elif PuntP1[len(PuntP1)-1] == "Ventaja P1":
                PuntP1.append("Deuce")
                PuntP2.append("Deuce")
            else:
                PuntP1.append("Ventaja P2")
                PuntP2.append("Ventaja P2")
        else:
            N2 += 1
            PuntP1.append(Puntuaciones[N1])
            PuntP2.append(Puntuaciones[N2])
    else:
        print("No es un parámetro válido")

    if (Puntuaciones[N1] == Puntuaciones[N2] and Deuce == True and N1 >= 3):
        Deuce = False
        PuntP1.remove(PuntP1[len(PuntP1)-1])
        PuntP2.remove(PuntP1[len(PuntP1)-1])
        PuntP1.append("Deuce")
        PuntP2.append("Deuce")

for i in range(len(PuntP1)):
    if PuntP1[i] == "Deuce" or PuntP1[i] == "Ventaja P2" or PuntP1[i] == "Ventaja P1" or PuntP1[i] == "Ha ganado el P2" or PuntP1[i] == "Ha ganado el P1":
        print(PuntP1[i])
    else:
        print(PuntP1[i], " - ",PuntP2[i])