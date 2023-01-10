puntos = (
    'Love',
    '15',
    '30',
    '40',
    )

def juego(secuencia):
    jugador = {
        'P1': 0,
        'P2': 0
    }
    for punto in secuencia:
        jugador[punto] += 1
        if jugador['P1'] >= 3 and jugador['P2'] >= 3: 
            ventaja = jugador['P1'] - jugador['P2']
            if ventaja == 0:
                print('Deuce')
            elif abs(ventaja) == 1:
                print(f'Ventaja {"P1" if ventaja > 0 else "P2"}')
            else:
                print(f'Ha ganado el {"P1" if ventaja > 0 else "P2"}')
        else:
            print(f'{puntos[jugador["P1"]]} - {puntos[jugador["P2"]]}')
