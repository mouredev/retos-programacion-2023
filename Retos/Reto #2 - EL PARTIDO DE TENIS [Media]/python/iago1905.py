partido = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P1","P2","P2","P2","P2"]
puntuaciones = ["Love",15, 30, 40, "Deuce", "Ventaja ", "Ha ganado el "] # 0, 1, 2, 3
p1 = 0
p2 = 0
    
    
for i in partido:
    if i == "P1":
        p1 += 1    
    else:
       p2 += 1

    # Deuce
    if p1 == 3 and p2 == 3:
        print(puntuaciones[4])
        continue

    # Ventajas
    if p1 > 3 and p1-p2 == 1:
        print(puntuaciones[5]+i)
        continue
    elif p2 > 3 and p2-p1 == 1:
        print(puntuaciones[5]+i)
        continue
    
    if p1 > 3 and p1 == p2:
        print(puntuaciones[4])
        continue

    # Victorias
    if p1 > 4 and p1 > p2:
        print(puntuaciones[6]+i)
        break

    if p2 > 4 and p1 < p2:
        print(puntuaciones[6]+i)
        break

    print(puntuaciones[p1], " - ", puntuaciones[p2])

    



    
