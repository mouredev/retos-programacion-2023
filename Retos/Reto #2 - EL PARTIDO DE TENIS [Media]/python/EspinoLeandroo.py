def convert_point(points):
    if points == 0:
        return "Love"
    elif points == 1:
        return "15"
    elif points == 2:
        return "30"
    elif points == 3:
        return "40"

p1 = 0
p2 = 0
while True:
    p = input()

    if p == "P1":
        p1 += 1
    elif p == "P2":
        p2 += 1
    else:
        print("invalid input")

    if p1 == 3 and p2 == 3:
        print("Deuce")
    elif p1 <= 3 and p2 <= 3:
        print(convert_point(p1) + " - " + convert_point(p2))
    else:
        if p1 - 1 == p2:
            print("Ventaja P1")
        elif p2 - 1 == p1:
            print("Ventaja P2")
        else:
            if p1 > p2:
                print("Ha ganado el P1")
                break
            elif p2 > p1:
                print("Ha ganado el P2");
                break
            else:
                print("Deuce");
            
        
    