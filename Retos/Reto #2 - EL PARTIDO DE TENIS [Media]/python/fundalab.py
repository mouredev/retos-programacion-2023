
# reto de programación No. 2
# 12-ene-2023
# @fundalab by jesus becerra
# siguiendo retosdeprogramacion.com by mouredev
'''
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
'''
print ("Reto 2: EL PARTIDO DE TENIS")
marcador_p1=["love"]
marcador_p2=["love"]
puntos_p1=0
puntos_p2=0
deuce=False
advantage_p1 = False
advantage_p2 = False

print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}")

while True:
    punto = (input("Ingrese el jugador que ganó el punto: ")).upper()

    if (punto == "P1"):
        if deuce == True:
            advantage_p1 = True
            deuce = False
            print("P1 advantage")
            #marcador_p1.append("Advantage")
            #marcador_p2.append("")     
            #print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}") 
        elif deuce == False and advantage_p1 == True:
            print("Ganó P1")
            break

        if advantage_p2 == True:
         
            deuce=True
            advantage_p1=False
            advantage_p2=False 

        puntos_p1 = puntos_p1 + 1
        if puntos_p1 == 1:
            marcador_p1.append("15")
            print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}")
        if puntos_p1 == 2:
            marcador_p1.append("30")
            print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}") 
        if puntos_p1 == 3 and puntos_p2 <=2:
            marcador_p1.append("40")
            print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}")

    elif (punto == "P2"):

        if deuce == True:
            advantage_p2 = True
            deuce = False
            print("P2 advantage")
            #marcador_p2.append("Advantage")
            #marcador_p1.append("")     
            #print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}") 
        elif deuce == False and advantage_p2 == True:
            print("Ganó P2")
            break

        if advantage_p1 == True:
           
            deuce=True
            advantage_p1=False
            advantage_p2=False 

 



        puntos_p2 += 1
        if puntos_p2 == 1:
            marcador_p2.append("15")
            print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}")
        if puntos_p2 == 2:
            marcador_p2.append("30")
            print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}") 
        if puntos_p2 == 3 and puntos_p1  <= 2:
            marcador_p2.append("40")
            print(f"Player 1: {marcador_p1[-1]} \nPlayer 2: {marcador_p2[-1]}")
    else:
        print ("Error de entrada")

        
    if (puntos_p1 == puntos_p2) and (puntos_p1 >= 3 and puntos_p2 >=3):
        print("Deuce")
        deuce=True
        advantage_p1=False
        advantage_p2=False

    if puntos_p1 == 4 and puntos_p2 <=2:
        print("Gano p1")
        break     
    if puntos_p2 == 4 and puntos_p1 <=2:
        print("Gano p2")
        break  
