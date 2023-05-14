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

partida_tennis(('P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'))