#Partido de tenis #1 ##################################################################################
def fase_juegos(puntos):
    contador = 0
    ganador = False
    P1 = 0
    P2 = 0
    for x in puntos:
        if fase_regular(P1,P2) == True:
            if x.upper() == 'P1':
                P1 = puntuacion_basica(P1)
            elif x.upper() == 'P2':
                P2 = puntuacion_basica(P2)
            imprimir_fase(P1, P2)
            if P1 > 40 and P2 < 40:
                ganador = 'P1'
                break
            elif P2 > 40 and P1 < 40:
                ganador = 'P2'
                break
        elif fase_regular(P1,P2) == False:
            ganador = puntuacion_advance(puntos[contador:])
        contador +=1
        if ganador != False:
            break
    return ganador
def fase_regular(P1,P2):
    if P1 == P2 == 40:
        return False
    else:
        return True

def puntuacion_basica(variable):
    if (0 <= variable < 30):
        variable += 15
    elif (30 <= variable <= 40):
        variable += 10
    return variable
def puntuacion_advance(puntos):
    diccionario = {0:'Deuce',1:'Advance P1',2:'Winner P1',-1:'Advance P2',-2:'Winner P2'}
    i = 0
    for x in puntos:
        if i != 2 or i != -2:
            if (x == 'P1'):
                i += 1
            else:
                i -= 1
        else:
           return desenpate(i)
        print(diccionario[i])
    return desenpate(i)
def desenpate(i):
    if i == 2:
        return 'P1'
    else:
        return 'P2'
    return False

def imprimir_fase(P1,P2):
    diccionario = {0:'Love',15:'15',30:'30',40:'40'}
    print(f'{diccionario[P1]} - {diccionario[P2]}')

#Partido de tenis #2###################################################################################
def partida_tennis(partido):
    ganador = False
    diccionario = {0: 'Love',1: '15',2: '30',3:'40',4:'Winner'}
    P1 = 0
    P2 = 0
    contador = 0
    for x in partido:
        if fase_regular(P1,P2) == True:
            if x == 'P1':
                P1 = puntuacion_basica(P1)
            elif x == 'P2':
                P2 = puntuacion_basica(P2)
            print(f'{diccionario[P1]} - {diccionario[P2]}')
            if P1 == 4 or P2 == 4:
                break
        else:
            puntuacion_advance(partido[contador:])
            break
        contador += 1
def fase_regular(P1, P2):
    if P1 == P2 == 3:
        return False
    else:
        return True

def puntuacion_basica(variable):
    if (0 <= variable < 3):
        variable += 1
    return variable

def puntuacion_advance(partido):
    P1 = 0
    P2 = 0
    diccionario = {0: 'Deuce', 1: 'Advance', 2: 'Winner'}
    for x in partido:
        if x == 'P1':
            if (P2 == 0):
                P1 += 1
            else:
                P2 -= 1
        elif x == 'P2':
            if P1 == 0:
                P2 += 1
            else:
                P1 -= 1
        if P1 > P2:
            print(diccionario[P1] +':P1')
            if P1 == 2:
                break
        elif P1 == P2:
            print(diccionario[P1])
        else:
            print(diccionario[P2])
            if P2 == 2:
                break
