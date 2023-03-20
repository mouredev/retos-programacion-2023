"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

P1=0
P2=0
t=0

p=""
p=input()

while (t==0):

    if (p=="P1" and P1==0 and P2==0):
       P1=15
       print(P1," - Love")
    elif (p== "P1" and P1==15 and P2==0):
       P1=30
       print(P1," - Love")
    elif (p=="P1" and P1==30 and P2==0):
        P1=40
        print(P1," - Love")
    elif (p== "P1" and P1==40 and P2==0):
        print("Ha ganado el P1")
        t=1
    elif (p== "P1" and P1==15 and P2==15):
        P1 =30
        print(P1," - ",P2)
    elif (p=="P1" and P1==30 and P2==15):
        P1=40
        print(P1," - ",P2)
    elif (p== "P1" and P1==40 and P2==15):
        print("Ha ganado el P1")
        t=1
    elif (p== "P1" and P1==15 and P2==30):
        P1=30
        print(P1 , " - " , P2)
    elif (p=="P1" and P1==30 and P2==30):
        P1=40
        print( P1 , " - " , P2) 
    elif (p== "P1" and P1==40 and P2==30):
        print("Ha ganado el P1")
        t=1
    elif (p== "P1" and P1==15 and P2==40):
        P1=30
        print(P1 , " - " , P2) 
    elif (p=="P1" and P1==30 and P2==40):
        P1=40
        print("Deuce") 
    elif (p== "P1" and P1==40 and P2==40):
        P1=55
        print("Ventaja para P1") 
    elif (p=="P1" and P1==55):
        print("Ha ganado P1") 
        t=1
    elif (p=="P2" and P1==0 and P2==0):
        P2=15
        print("Love - " , P2) 
    elif (p=="P2" and P1==0 and P2==15):
        P2=30
        print("Love - " , P2) 
    elif (p=="P2" and P1==0 and P2==30):
        P2=40
        print("Love - " , P2) 
    elif (p=="P2" and P1==0 and P2==40):
        print("Ha ganado P2") 
        t=1
    elif (p=="P2" and P1==15 and P2==0):
        P2=15
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==15 and P2==15):
        P2=30
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==15 and P2==30):
        P2=40
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==15 and P2==40):
        print("Ha ganado P2") 
        t=1
    elif (p=="P2" and P1==30 and P2==0):
        P2=15
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==30 and P2==15):
        P2=30
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==30 and P2==30):
        P2=40
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==30 and P2==40):
        print("Ha ganado P2") 
        t=1
    elif (p=="P2" and P1==40 and P2==0):
        P2=15
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==40 and P2==15):
        P2=30
        print(P1 , " - " , P2) 
    elif (p=="P2" and P1==40 and P2==30):
        P2=40
        print("Deuce") 
    elif (p=="P2" and P1==40 and P2==40):
        P2=55
        print(" Ventaja para P2")   
    elif(p=="P2" and P2==55):
        print("Ha ganado P2") 
        t=1
    
    p=input()
       
    
  