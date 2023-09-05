import os

#Devuelve la pieza rotada
# pieza <[n,n]>: Pieza representada en un array bidimensional
def rotar(pieza):
    rotacion = []

    for i in range(len(pieza[0])):
        aux1 = []
        for j in range(len(pieza)-1,-1,-1): aux1.append(pieza[j][i])
        rotacion.append(aux1)
    return rotacion

#Dibuja el tablero con la pieza
# columnas <int>: Columnas del tablero
# filas <int>:    Filas del tablero
# pieza <[n,n]>:  Pieza representada en un array bidimensional
# xpos <int>:     Posicion de la pieza en el eje x (columnas)
# ypos <int>:     Posicion de la pieza en el eje y (filas)
def print_tablero(columnas, filas, pieza, xpos, ypos):
    for y in range(filas):
        for x in range(columnas):
            rposx = x-xpos
            rposy = y-ypos
            if (0<=rposy and rposy<len(pieza) and 0<=rposx and rposx<len(pieza[rposy]) and pieza[rposy][rposx] == 1): res = "🔳"
            else: res = "🔲"

            print(res,end = "")
        print()

#Comprueba si la posicion de la pieza en el tablero es valida
# columnas <int>: Columnas del tablero
# filas <int>:    Filas del tablero
# pieza <[n,n]>:  Pieza representada en un array bidimensional
# xpos <int>:     Posicion de la pieza en el eje x (columnas)
# ypos <int>:     Posicion de la pieza en el eje y (filas)
def posicion_valida(columnas, filas, pieza, xpos, ypos):
    ancho_pieza = len(pieza[0])
    altura_pieza = len(pieza)
    if( 0 <= xpos and xpos+ancho_pieza <= columnas and 0 <= ypos and ypos+altura_pieza <= filas ): return True
    else: return False


#Pieza
pieza = [[1,0,0],[1,1,1]]

#Posicion inicial
posx = 0
posy = 0

#Tablero por defecto
ncol = 10
nfilas = 10

#Main
os.system('clear')
print("Define el tamaño del tablero, minimo 3 columnas y 2 filas por ser el tamaño de la pieza inicial")

while True:
    ncol_input = input(" Columnas (10): ")
    if ncol_input=="": break
    elif ncol_input.isdigit() and int(ncol_input) >= 3:
        ncol = int(ncol_input)
        break

while True:
    nfilas_input = input(" Filas (10): ")
    if nfilas_input=="": break
    elif nfilas_input.isdigit() and int(nfilas_input) >= 2:
        nfilas = int(nfilas_input)
        break

while True:
    os.system('clear')
    print_tablero(ncol,nfilas,pieza,posx,posy)
    print()
    action = input("(q)salir (a)izquierda (s)abajo (d)derecha (r)rotar: ")
    if action == 'a': 
        if(posicion_valida(ncol,nfilas,pieza,posx-1,posy)): posx = posx -1
    elif action == 'd': 
        if(posicion_valida(ncol,nfilas,pieza,posx+1,posy)): posx = posx + 1
    elif action == 's': 
        if(posicion_valida(ncol,nfilas,pieza,posx,posy+1)): posy = posy + 1
    elif action == 'r': 
        if(posicion_valida(ncol,nfilas,rotar(pieza),posx,posy)): pieza = rotar(pieza)
    elif action =='q': break

