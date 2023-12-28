def juego(secuencia):
    puntos = ('Love', '15', '30', '40')
    jugador_1 = jugador_2 = 0
    for punto in secuencia:
        if punto == 'P1':
            jugador_1 += 1
        else:
            jugador_2 += 1
        if jugador_1 >= 3 or jugador_2 >= 3:
            ventaja = jugador_1 - jugador_2
            if ventaja == 0:
                print('Deuce')
                continue
            elif jugador_1 > 3 or jugador_2 > 3:
                P1_o_P2 = f'{"P1" if ventaja > 0 else "P2"}'
                if abs(ventaja) == 1:
                    print(f'Ventaja {P1_o_P2}')
                    continue
                else:
                    print(f'Ha ganado el {P1_o_P2}')
                    break
        print(f'{puntos[jugador_1]} - {puntos[jugador_2]}')
