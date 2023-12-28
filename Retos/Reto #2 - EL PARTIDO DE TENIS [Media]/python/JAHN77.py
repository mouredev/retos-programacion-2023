#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.  
c1=0
c2=0
while True:
    puntopara=input("Puntaje a favor de: ")
    puntos=["Love",15,30,40,60,""]


    
    if puntopara=="p1":
        c1+=1
    if puntopara=="p2":
        c2+=1

    if c1>=3 and c2>=3 and c1==c2:
        print("Deuce")

    elif (c1>=3 and c2>=3) and (c1==c2-1 or c2==c1-1):
        print(f"Ventaja {puntopara}")
    
    elif c1<=3 and c2<=3:
        if  puntopara=="p1" or puntopara=="p2" :
            print(f"{puntos[c1]}-{puntos[c2]}")

    if c1>=3 or c2>=3:
        if ((c1==4 and c2<=2) or (c2==4 and c1<=2)) or ((c1>=4 or c2>=4)  and (c1<c2-1 or c2<c1-1)):
            print(f"Ha ganado {puntopara}")
            break
        

    
        
    
        
    

    
    
    


    