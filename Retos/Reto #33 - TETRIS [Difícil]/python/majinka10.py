import random

def dibujaMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="")
        print()

pieza=[[[[0,0], [1, 0], [1, 1], [1, 2]],[False]],[[[0,1],[0,0],[1,0],[2,0]],[False]],[[[1,2],[0,2],[0,1],[0,0]],[False]],[[[2,0],[2,1],[1,1],[0,1]],[False]]] #Posicion incial de la pieza ubicada arriba a la izquierda

# 🔳
# 🔳🔳🔳

# 🔳🔳
# 🔳
# 🔳

# 🔳🔳🔳
#     🔳

#   🔳
#   🔳
# 🔳🔳

# pieza1=random.choice(pieza)

pieza1=[[[0,0], [1, 0], [1, 1], [1, 2]],[False]]

def llenarMatriz():
    matriz=[]
    for _ in range(10):
        a = ['🔲']*10
        matriz.append(a)
    return matriz 

def llenarTablero(pieza):
    tableroBlanco = llenarMatriz()
    for tuple in pieza[0]:
        tableroBlanco[tuple[0]][tuple[1]]='🔳'
    return tableroBlanco, pieza

def moverAbajo(pieza):
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

def moverDerecha(pieza):
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

def moverIzquierda(pieza):
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

def rotar(pieza):
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
            if pieza[1]==True:
                pieza[0][0][0]+=1
                pieza[0][0][1]+=1
                pieza[0][1][1]+=2
                pieza[0][2][0]-=1
                pieza[0][2][1]+=1
                pieza[0][3][0]-=2
            else:
                pieza[0][0][0]+=1
                pieza[0][0][1]+=1
                pieza[0][1][1]+=2
                pieza[0][2][0]-=1
                pieza[0][2][1]+=1
                pieza[0][3][0]-=2
                for tuple in pieza[0]:
                    tuple[1]-=1

        elif pieza[0][0][1]+1<9:
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

acciones=['exit','abajo','derecha','izquierda','rotar']
# especial1=[[1, 3], [0, 3], [0, 2], [0, 1]]

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
    elif accion=='a':
        pieza = moverAbajo(pieza1)
    elif accion=='d':
        pieza = moverDerecha(pieza1)
    elif accion=='i':
        pieza = moverIzquierda(pieza1)
    elif accion == 'r':
        pieza = rotar(pieza1)
    # pieza=moverAbajo(pieza) #Descomentar esta línea para que la pieza baje después de cada acción
    tetris()

tetris() 