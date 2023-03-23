
def score(P1,P2):
    puntuacion1=0
    puntuacion2=0

    if P1==0:
        puntuacion1="Love"
    elif P1==1:
        puntuacion1=15
    elif P1==2:
        puntuacion1=30
    elif P1==3:
        puntuacion1=40
    
    if P2==0:
        puntuacion2="Love"
    elif P2==1:
        puntuacion2=15
    elif P2==2:
        puntuacion2=30
    elif P2==3:
        puntuacion2=40

    if P1>=3 and P2>=3:     
        if P1 == P2:
            print("Deuce")
        elif P1-P2 >=2:
            print("Ha ganado el P1")
        elif P2-P1 >=2:
            print("Ha ganado el P2")
        elif P1>P2:
            print("Ventaja P1")
        elif P2>P1:
            print("Ventaja P2")
    else:
        print(f"{puntuacion1} - {puntuacion2}")
    

if __name__=="__main__":
    P1=0
    P2=0
    secuencia=[]
    #____________________________ para pedir al usuario los datos
    for i in range (8):
        A=input(f"Escribe el puntaje {i+1}: \n")
        secuencia.append(A.upper())
    #____________________________

    #secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]   
    print("Los Resultados fueron:")
    print("\n")
    for each in secuencia:
        if each == "P1":
            P1+=1
        if each=="P2":
            P2+=1
        
        score(P1,P2)

    
