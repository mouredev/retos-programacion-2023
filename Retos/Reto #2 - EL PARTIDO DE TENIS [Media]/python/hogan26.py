diccionario = {
    0 : 'love',
    1 : '15',
    2 : '30',
    3 : '40'
}

def match(secuencia):
    p1,p2 = 0 , 0
    for player in secuencia:
        if player == 'P1': p1+= 1
        else: p2+= 1        

        if p1 == 3 and p2 == 3: print("Deuce")
        elif p1 == 4 and p2 == 3: print("Ventaja P1")
        elif p1 == 4 and p2 < 3: 
            print("Gana P1")
            quit()
        elif p1 == 3 and p2 == 4: print("Ventaja P2")            
        elif p1 < 3 and p2 == 4:
            print("Gana P2")
            quit()
        elif p1 == 4 and p2 == 4: 
            p1-=1
            p2-=1
            print("Deuce")
        elif p1 == 5:
            print("Gana P1")
            quit()
        elif p2 == 5:
            print("Gana P2")
            quit()
        else:
            print(diccionario[p1]+" - "+diccionario[p2])    

match(['P1','P1','P2','P2','P1','P2','P1','P2','P2','P2'])