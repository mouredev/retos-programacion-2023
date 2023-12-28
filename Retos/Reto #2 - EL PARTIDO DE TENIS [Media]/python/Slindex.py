validacion = False

while not validacion:
    secuencia = input('Por favor ingrese la secuencia del juego: ')
    secuencia = secuencia.split(sep=',')

    print(secuencia)

    for i,jugador in enumerate(secuencia):
        secuencia[i] = jugador.strip()

    for jugador in secuencia:
        if jugador != 'P1' and jugador != 'P2':
            print('Por favor ingrese "P1" o "P2" como su secuencia, separada por comas')
            validacion = False
            break
        else:
            validacion = True

puntos_p1 = 0
puntos_p2 = 0
deuce_flag = False

marcador = {0: 'Love',
            1: '15',
            2: '30',
            3: '40',}

def deuce():
    if puntos_p1 == puntos_p2 and (puntos_p1 >= 3 or puntos_p2 >= 3):
        deuce = True
    else:
        deuce = False
    return deuce

def ventaja():
    if abs(puntos_p1 - puntos_p2) == 1:
        ventaja = True
    else:
        ventaja = False
    return ventaja

def ganador():
    if (puntos_p1 >= 4 or puntos_p2 >= 4) and abs(puntos_p1 - puntos_p2) >= 2:
        ganador = True
    else:
        ganador = False
    return ganador

for jugador in secuencia:

    if jugador == 'P1':
        puntos_p1 += 1
    elif jugador == 'P2':
        puntos_p2 += 1
    
    if deuce():
        deuce_flag = True
        print('Deuce')
    elif ventaja() and deuce_flag:
        print(f'Ventaja {jugador}')
    elif ganador():
        print(f'Ha ganado el {jugador}')
        break
    else:
        print(f'{marcador[puntos_p1]} - {marcador[puntos_p2]}')