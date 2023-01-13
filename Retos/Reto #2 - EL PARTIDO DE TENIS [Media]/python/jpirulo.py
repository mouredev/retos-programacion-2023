
def run():
    juegos = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
    p1=0
    p2=0
    ronda=0
    points = ['Love', '15', '30', '40']
    print("Bienvenidos al partido de Teniss Copa Pyton 2023")
    print("_________________________________________________")

    for i in juegos:
        ronda +=1
        if i == 'P1':
            p1 +=1
        elif i == 'P2':
            p2 +=1
        
        if p1 == 3 and  p2 == 3:
           print(f"{ronda}. Deuce!!!!")
        elif (p1 <3 or p2 <3):
            print(f"{ronda}. Player 1: {points[p1]} | Player 2: {points[p2]}")  

        if (p1 >= 4 or p2 >= 4) and abs(p1 - p2) >= 2:
            if p1> p2:
                print(f"{ronda}. Ha ganado el Player 1")
            else:
                print(f"{ronda}.Ha ganado el Player 2")
            return
        
        if (p1 >= 3 and p2 >= 3) and abs(p1 - p2) == 1:
            if p1> p2:
                print(f"{ronda}. Ventaja para Player 1")
            else:
                print(f"{ronda}. Ventaja para Player 2")
            continue





        








if __name__ == "__main__":
    run()
