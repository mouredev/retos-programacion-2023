import sys

sec = input("Ingrese secuencia en formato lista: ")

sec1 = sec.replace("[", "")
sec2 = sec1.replace("]", "")
secuencia = sec2.split(", ")

#Catching errors
def catchE():
    if len(secuencia) < 4: return True
    elif secuencia.count("P1")+2 == secuencia.count("P2"): return False
    elif secuencia.count("P2")+2 == secuencia.count("P1"): return False
    return True
if catchE() == True:
    print("Secuencia de puntos invalida")
    sys.exit()

P1_points = 0 
P2_points = 0
points = {0: "Love", 1: 15, 2: 30, 3: 40}

for value in secuencia:     
    if value == "P1":
        P1_points += 1
        if P1_points <= 3 and P2_points <3:
            print(points[P1_points],"-",points[P2_points])
        elif P1_points >=3 and P1_points == P2_points:
            print("Deuce")
        elif P1_points > 3 and P2_points == P1_points - 1:
            print("Ventaja P1")
        elif P1_points > 3 and P2_points < P1_points - 1:
            print("Ha ganado el P1")
    if value == "P2":
        P2_points += 1
        if P2_points <= 3 and P1_points <3:
            print(points[P1_points],"-",points[P2_points])
        elif P2_points >=3 and P1_points == P2_points:
            print("Deuce")
        elif P2_points > 3 and P1_points == P2_points - 1:
            print("Ventaja P2")
        elif P2_points > 3 and P1_points < P2_points - 1:
            print("Ha ganado el P2")
