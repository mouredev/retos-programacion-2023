
def valinput(mensaje): ##### validacion de datos de ingreso
    while True:
        try:
            print(f"{mensaje}")    
            valor=int(input(">>"))
            return valor
        except ValueError:
            print("cometio un error, debe ingresar un numero entero ")


def game(movidas):       ##validacion de juego
    reglas={1:[2,4],  #piedra
            2:[3,4],  #tijera
            3:[1,5],  #papel
            4:[3,5],  #lagarto
            5:[1,2]   #spock
    }
    player1=0
    player2=0

    for i in range(len(movidas)):
        if movidas[i][0]==movidas[i][1]:
            pass
        else:
            if movidas[i][1] in reglas[movidas[i][0]]:
               player1+=1
            else:
               player2+=1
            
    print("\n")
    if player1==player2:
        print("tie")
    elif player1>player2:
        print("ganador jugador 1")
    else:
        print("ganador jugador 2")

def resultados(movidas):
    print(  f"__________Movimientos______________")

    for i in range(len(movidas)):
        print(f"| jugador 1  {valores[movidas[i][0]]}   jugador2    {valores[movidas[i][1]] }    ")
        print(f"|_________________________________")




#print(list(valores.keys())[list(valores.values()).index("🪨")])
valores={1:"🪨",2:"✂️",3:"📰",4:"🦎",5:"🧑‍🚀"}

i=0
movidas=list()
print(valores)
mensaje="defina numero de partidas"
partidas=valinput(mensaje)

while i<partidas:
    try:
        i+=1
        mensaje="Jugador 1 haga su movimiento "
        play1=valinput(mensaje)
        mensaje="Jugador 2 haga su movimiento "
        play2=valinput(mensaje)


        tupla=(play1,play2)
        movidas.append(tupla)
    except ValueError:
        print("cometio un error, debe ingresar un numero entero ")



resultados(movidas)
game(movidas)


