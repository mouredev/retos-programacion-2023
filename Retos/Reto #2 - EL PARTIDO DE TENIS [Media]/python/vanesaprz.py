# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

## Enunciado

"""
/*
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
 */
"""

#La idea es que mi programa va a ir solicitando quien gana los puntos uno a uno, hasta que uno de los jugadores gane. 

def gana_punto (): #Solicita el jugador que ha ganado el punto al usuario. 
    
    while True: #se comprueba que el input es válido, comparándolo con P1 y P2. 
        puntuador = input ("Qué jugador ha ganado el punto? (P1/P2): ")
        if puntuador == "P1" or puntuador =="P2": 
            break
        else: #Si no es válido, se introduce un mensaje de error y se vuelve a preguntar. 
            print("No has indicado el jugador correctamente. ")
    return puntuador

    
def actualizar_puntos (puntuador, p_j1, p_j2): 
    #comprueba quien ha ganado punto y actualiza las puntuaciones
    if puntuador == "P1":
        p_j1 += 1
    else:
        p_j2 +=1

    return p_j1, p_j2

def in_duece (p_j1, p_j2): #comprueba si hemos llegado a un punto en el que ha habido deuce al menos una vez. A partir de aquí será siempre deuce o ventaja
    if p_j1 >=3 and p_j2 >=3:
        return True
    else: 
        return False

def imprimir_marcador (p_j1, p_j2):
    #funcion encargada de imprimir el marcador. Recibe la puntuación de ambos jugadores. 
    duece = in_duece(p_j1, p_j2)
    if not duece:
        #si no hay deuce o ventaja, simplemente muestra el marcador normal  según los posibles ["Love", "15", "30", "40"]
        print (f"{posibles[p_j1]} - {posibles[p_j2]}")

    #Si ya ha habido deuce, compara las puntuaciones:   
    elif p_j1 == p_j2:
        print("Deuce")
    elif p_j1 > p_j2:
        print("Ventajan P1")
    else:
        print ("Ventaja_P2")


def comprueba_ganador(p_j1, p_j2): #Comprueba si se dan las condiciones para que alguno de los jugadores haya ganado. Recibe ambas puntuaciones.

    #en caso de ganador, imprime quien ha ganado y devuelve True
    if (p_j2 - p_j1 >= 2 ) and p_j2 >3: 
        print("Ha ganado el P2")
        return True
    
    elif (p_j1 - p_j2 >= 2 ) and p_j1 >3:
        print("Ha ganado el P1")
        return True
    
    #si nadie ha ganado, devuelve falso.
    else:
        return False



#posibles puntuaciones antes de deuce
posibles= ["Love", "15", "30", "40"]

#desarrollo del juego:

puntos_j1 = 0
puntos_j2 = 0        

hay_ganador = False

while not hay_ganador:
    puntuador = gana_punto() #tenemos el jugador que gana el punto P1 o P2
    puntos_j1, puntos_j2 = actualizar_puntos(puntuador, puntos_j1, puntos_j2) #se suma el punto al jugador que corresponda
    hay_ganador = comprueba_ganador(puntos_j1, puntos_j2) 
    #si esta función devuelve True, se nos indica que hay un ganador y por lo tanto, saldríamos del loop y se acaba el partido.
    
    if not hay_ganador: #si no hay ganador, imprimimos marcador y seguimos en loop. 
        imprimir_marcador(puntos_j1, puntos_j2)
    



    


 







    