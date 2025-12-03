p1=0
p2=0
puntaje={0:"Love",1:15,2:30,3:40}
while True:
    try:
        tiro =input("Ingrese turno: ")
        if tiro.upper() == "P1":
            p1 += 1
        elif tiro.upper() == "P2":
            p2 += 1
        if p1 >= 4 and p1 - p2 >=2:
            print("Ha ganado el P1")
            break
        elif p2 >= 4 and p2 - p1 >=2:
            print("Ha ganado el P2")
            break
        elif (p1 >= 3 and p2 >= 3) and p1 == p2:
            print("Deuce")
        elif p1 >= 3 and p2 >=3 and p1 - p2 == 1:
            print("Ventaja P1 ")
        elif p1 >= 3 and p2 >=3 and p2 - p1 == 1:
            print("Ventaja P2")
        else:
            print(f"{puntaje[p1]} - {puntaje[p2]}")
    except ValueError:
        print("entrada inválida")
        pass    