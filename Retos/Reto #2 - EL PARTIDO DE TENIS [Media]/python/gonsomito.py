# * 
# * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# *   15 - Love
# *   30 - Love
# *   30 - 15
# *   30 - 30
# *   40 - 30
# *   Deuce
# *   Ventaja P1
# *   Ha ganado el P1
# * - Si quieres, puedes controlar errores en la entrada de datos.   
# * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
# */
#---------------------------FUNCIONES---------------------------
def tanteo(punto_en_juego):                                     #ESTA FUNCION VA A COMPROBAR EL MARCADOR. RECIBE una LISTA CON EL MARCADOR 
    puntuaciones = {0: "Love",1: "15",2:"30",3:"40",4:"DEUCE", 5:"Ventaja"}  #USA UN DICCIONARIO DE RESULTADOS POSIBLES
    if punto_en_juego[0] == 3 and punto_en_juego[1] == 3:       #COMPROBAMOS DEUCE
        print(puntuaciones[4])                                  #Si es DUCE me salgo
        return (0,0)
    elif punto_en_juego[0] >= 3 and punto_en_juego[1] >= 3:     #CUANDO ESTAMOS EN DEUCE COMPROBAMOS PARA QUIEN ES LA Ventaja
        if punto_en_juego[0]>punto_en_juego[1]:
            print(puntuaciones[5]+" P1")                         #Ventaja para P1
            return (1,0)                                         #y devuelvo una bandera average para P1
        elif punto_en_juego[0]<punto_en_juego[1]:
            print(puntuaciones[5]+" P2")                         #Ventaja para P2
            return (0,1)                                         #y devuelvo una bandera average para P2
    elif punto_en_juego[0] < 5 and punto_en_juego[1] < 5:
        print(puntuaciones[punto_en_juego[0]] + " - " + puntuaciones[punto_en_juego[1]]) 
        return (0,0)                                             #cualquier otro resultado que no implique DEUCE o VENTAJA
#----------------------------EMPIEZA EL PARTIDO-----------------
print("Partido de Tenis entre P1 vs P2")
marcador = [0, 0]                                                #marcador a cero en una lista de 2 elementos
average  = [0, 0] 
matchball = [0, 0]
average  = tanteo(marcador)                                      #inicio el partido y pone el average a 0 por si hace falta. funciona como una bandera
while marcador[0] <=4 and marcador[1] <=4:
    if (marcador[0] == 3 and marcador[1] <3) :                   #comprobamos si es bola de partido MATCHBALL
        #print("\nMATCHBALL P1")
        matchball = [1, 0]
    elif (marcador[0] <3 and marcador[1] == 3):
        #print("\nMATCHBALL P2")
        matchball = (0, 1)
    else: 
        matchball = (0, 0)
    print("Punto para: ")                                        #Pedimos un ganador del punto
    punto_para = input()                                         #esperamos un valor P1 o P2 
    if average == (0,0):                                         #si no hay VENTAJA se suma el punto
        if punto_para == 'p1' or punto_para == 'P1':             #PUNTO NORMAL para P1
            marcador[0] = marcador[0] + 1 + matchball[0]
            average = tanteo(marcador) 
        elif punto_para == 'p2' or punto_para == 'P2':           #PUNTO NORMAL para P2
            marcador[1] = marcador[1] + 1 + matchball[1]
            average =  tanteo(marcador)
        else:                                                    #MAL SAQUE, VUELVE A INTRODUCIR QUIEN SE LLEVA EL PUNTO
            print ("\n\nOUT!! (vuelve a sacar)")                     
    elif average == (1,0) :                                      #si hay VENTAJA P1 se suma el punto
        if punto_para == 'p1' or punto_para == 'P1':
            marcador[0] = marcador[0] + 2 
            average =  tanteo(marcador)
        elif punto_para == 'p2' or punto_para == 'P2':           #si rompe la ventaja p2, se resta el punto
            marcador[0] = marcador[0] - 1
            average =  tanteo(marcador)
        else:
            print ("\n\nOUT!! (vuelve a sacar)")                 #MAL SAQUE, VUELVE A INTRODUCIR QUIEN SE LLEVA EL PUNTO
    elif average == (0,1) : 
        #print("Juguemos el desempate")                          #si hay VENTAJA P2 se suma el punto
        if punto_para == 'p2' or punto_para == 'P2':
            marcador[1] = marcador[1] + 2 
            average =  tanteo(marcador)
        elif punto_para == 'p1' or punto_para == 'P1':           #si rompe la ventaja p1, se resta el punto
            marcador[1] = marcador[1] - 1
            average =  tanteo(marcador)
        else:
            print ("\n\nOUT!! (vuelve a sacar)")                #MAL SAQUE, VUELVE A INTRODUCIR QUIEN SE LLEVA EL PUNTO
    #print (marcador, average, matchball)
#------------------------VENCEDORES del PARTIDO
if marcador[0] >= 5 :
    print("\n\nVENCEDOR P1")
else:
    print("\n\nVENCEDOR P2")
#no es un código bonito, ni refinado, ni ordenado... pero funciona. 
#No está mal para empezar a quitar el óxido de los ruedines.
