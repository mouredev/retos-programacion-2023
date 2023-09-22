import random

def dibujaMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="")
        print()

pieza=[[[[0,0], [1, 0], [1, 1], [1, 2]],[False]],[[[0,1],[0,0],[1,0],[2,0]],[False]],[[[1,2],[0,2],[0,1],[0,0]],[False]],[[[2,0],[2,1],[1,1],[0,1]],[False]]] #Posicion incial de cada una de las formas, ubicada arriba a la izquierda. El booleando que acompaña cada pieza es para el caso especial en el que la forma 2 esté pegada a la izquierda. Ya que sin este no puedo saber cuando se movió a la derecha en el movimiento anterior para que en ese caso no vuelva a la izquierda.

# 🔳
# 🔳🔳🔳 Forma 1

# 🔳🔳
# 🔳    Forma 2
# 🔳

# 🔳🔳🔳 Forma 3
#     🔳

#   🔳
#   🔳 Forma 4
# 🔳🔳

pieza1=random.choice(pieza) #Escojo una forma al azar de la pieza

def llenarMatriz(): #LLeno una matriz de 10*10, en este caso es el tablero
    matriz=[]
    for _ in range(10):
        a = ['🔲']*10
        matriz.append(a)
    return matriz 

def llenarTablero(pieza): #Funcion que llena el tablero, lo primero que hace es hacer un tablero en blanco y luego llena con la posición actual de la pieza
    tableroBlanco = llenarMatriz()
    for tuple in pieza[0]:
        tableroBlanco[tuple[0]][tuple[1]]='🔳'
    return tableroBlanco, pieza

def moverAbajo(pieza): #Funcion que me ayuda a mover la pieza hacia abajo, siempre y cuando no se salga de la matriz
    for tuple in pieza[0]:
        if tuple[0]<9:
            sepuede=True
        else:
            sepuede=False
            break
    if sepuede:
        for tuple in pieza[0]:
            tuple[0]+=1
    return pieza

def moverDerecha(pieza): #Funcion que me ayuda a mover la pieza hacia la derecha, siempre y cuando no se salga de la matriz
    for tuple in pieza[0]:
        if tuple[1]<9:
            sepuede=True
        else:
            sepuede=False
            break
    if sepuede:
        for tuple in pieza[0]:
            tuple[1]+=1
    pieza[1]=True
    return pieza

def moverIzquierda(pieza): #Funcion que me ayuda a mover la pieza hacia la izquierda, siempre y cuando no se salga de la matriz
    for tuple in pieza[0]:
        if tuple[1]>0:
            sepuede=True
        else:
            sepuede=False
            break
    if sepuede:
        for tuple in pieza[0]:
            tuple[1]-=1
    return pieza

def rotar(pieza): #Funcion para rotar la pieza, basicamente funciona sumando lo que le falta a la pieza actualmente, en cada posicion, para ser la pieza que sigue en la rotación.
    if (pieza[0][0][0]-pieza[0][3][0])==-1: #Entra acá si está en la primera forma
        if pieza[0][0][1]==0 or pieza[0][3][1]==9 or pieza[0][3][1]==8: #Entra acá si está pegada a la izquierda o derecha
            pieza[0][0][1]+=1
            pieza[0][1][0]-=1
            pieza[0][2][1]-=1
            pieza[0][3][0]+=1
            pieza[0][3][1]-=2
            for tuple in pieza[0]:
                tuple[1]+=1
        else:
            pieza[0][0][1]+=1
            pieza[0][1][0]-=1
            pieza[0][2][1]-=1
            pieza[0][3][0]+=1
            pieza[0][3][1]-=2
        
    elif (pieza[0][0][0]-pieza[0][3][0])==-2: #Entra acá si está en la segunda forma

        if pieza[0][0][1]==2:
            if pieza[1]==True: #Entra aca si la pieza anteriormente se movio hacía la derecha
                pieza[0][0][0]+=1
                pieza[0][0][1]+=1
                pieza[0][1][1]+=2
                pieza[0][2][0]-=1
                pieza[0][2][1]+=1
                pieza[0][3][0]-=2
                pieza[1]=False #Lo establece en falso para que no vuelva a entrar
            else: #Sino se ha movido a la derecha entra aca
                pieza[0][0][0]+=1
                pieza[0][0][1]+=1
                pieza[0][1][1]+=2
                pieza[0][2][0]-=1
                pieza[0][2][1]+=1
                pieza[0][3][0]-=2
                for tuple in pieza[0]:
                    tuple[1]-=1

        elif pieza[0][0][1]+1<9: #Entra acá si no está pegada a la izquierda ni a la derecha
            pieza[0][0][0]+=1
            pieza[0][0][1]+=1
            pieza[0][1][1]+=2
            pieza[0][2][0]-=1
            pieza[0][2][1]+=1
            pieza[0][3][0]-=2

        else: #Entra acá si la pieza está pegada a la derecha
            for tuple in pieza[0]:
                tuple[1]-=1
            pieza[0][0][0]+=1
            pieza[0][0][1]+=1
            pieza[0][1][1]+=2
            pieza[0][2][0]-=1
            pieza[0][2][1]+=1
            pieza[0][3][0]-=2

    elif (pieza[0][0][0]-pieza[0][3][0])==1: #Entra acá si está en la tercera forma
            pieza[0][0][0]+=1
            pieza[0][0][1]-=2
            pieza[0][1][0]+=2
            pieza[0][1][1]-=1
            pieza[0][2][0]+=1
            pieza[0][3][1]+=1

    else:   #Entra acá si está en la cuarta forma
        if pieza[0][3][1]+1<10:
            pieza[0][0][0]-=2
            pieza[0][1][0]-=1
            pieza[0][1][1]-=1
            pieza[0][3][0]+=1
            pieza[0][3][1]+=1
        else: #Entra acá si la pieza está pegada a la derecha
            pieza[0][0][0]-=2
            pieza[0][1][0]-=1
            pieza[0][1][1]-=1
            pieza[0][3][0]+=1
            pieza[0][3][1]+=1
            for tuple in pieza[0]:
                tuple[1]-=1

    return pieza

acciones=['exit','abajo','derecha','izquierda','rotar'] #Acciones que se pueden realizar, esto me sirve para el while que está en tetris

def tetris():    
    newTablero, pieza=llenarTablero(pieza1)
    dibujaMatriz(newTablero)
    for tuple in pieza[0]:
        if tuple[0]==len(newTablero[0])-1:
            return print('Juego finalizado')
    accion=input('Ingresa la acción a realizar (abajo, derecha, izquierda o rotar) o exit para terminar el juego\n')
    while accion not in acciones:
        accion=input('Ingresa la acción a realizar (abajo, derecha, izquierda o rotar) o exit para terminar el juego\n')
    if accion == 'exit':
        return print('Juego finalizado')
    elif accion=='abajo':
        pieza = moverAbajo(pieza1)
    elif accion=='derecha':
        pieza = moverDerecha(pieza1)
    elif accion=='izquierda':
        pieza = moverIzquierda(pieza1)
    elif accion == 'rotar':
        pieza = rotar(pieza1)
    # pieza=moverAbajo(pieza) #Descomentar esta línea para que la pieza baje después de cada acción
    tetris()

tetris() 