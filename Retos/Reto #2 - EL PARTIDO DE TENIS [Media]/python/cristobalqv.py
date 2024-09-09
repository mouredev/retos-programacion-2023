def tenis():
    marcador_p1 = ['0', '15', '30', '40', 'V']
    marcador_p2 = ['0', '15', '30', '40', 'V']
    marcador_index1 = 0
    marcador_index2 = 0
    lista_puntos = []

    print(f'Marcador inicial: {marcador_p1[marcador_index1]} - {marcador_p2[marcador_index2]}')

    while True:
        if marcador_p1[marcador_index1] == '40' and marcador_p2[marcador_index2] == '40':
            print('Nos vamos a deuce')
            while True:
                ganador = input('Selecciona ganador del punto: P1 o P2: ').upper()
                if ganador == 'P1' and marcador_p1[marcador_index1] == 'V' and marcador_p2[marcador_index2] == '40':
                    print('Ha ganado el jugador P1!')
                    lista_puntos.append(ganador)
                    return 
                elif ganador == 'P2' and marcador_p1[marcador_index1 == '40'] and marcador_p2[marcador_index2] == 'V':
                    print('Ha ganado el jugador P2!')
                    lista_puntos.append(ganador)
                    return 
                elif ganador == 'P1' and marcador_p2[marcador_index2] == '40':
                    print('Ventaja para el jugador P1')
                    marcador_index1 += 1
                    lista_puntos.append(ganador)
                    while True:
                        ganador = input('Selecciona ganador del punto: P1 o P2: ').upper()
                        if ganador == 'P1':
                            print('Ha ganador el jugador P1')
                            lista_puntos.append(ganador)
                            return 
                        elif ganador == 'P2':
                            print('Gana el punto el jugador P2. Deuce')
                            lista_puntos.append(ganador)
                            marcador_index1 -= 1
                            break
                        else:
                            print('Digite un ganador válido P1 o P2')
                                    
                elif ganador == 'P2' and marcador_p1[marcador_index1] == '40':
                    print('Ventaja para el jugador P2')
                    marcador_index2 += 1
                    lista_puntos.append(ganador)
                    while True:
                        ganador = input('Selecciona ganador del punto: P1 o P2: ').upper()
                        if ganador == 'P2':
                            print('Ha ganado el jugador P2!')
                            lista_puntos.append(ganador)
                            return 
                        elif ganador == 'P1':
                            print('Gana el punto el jugador P1. Deuce')
                            lista_puntos.append(ganador)
                            marcador_index2 -= 1
                            break              
                else:
                    print('Digite un ganador válido P1 o P2')
     
        ganador = input('Selecciona ganador del punto: P1 o P2: ').upper()

        if ganador == 'P1':
            if marcador_index1 < len(marcador_p1) - 2:
                marcador_index1 += 1
                yield f'Marcador: {marcador_p1[marcador_index1]} - {marcador_p2[marcador_index2]}'
                lista_puntos.append(ganador)
            else: 
                print('El ganador es P1!')
                lista_puntos.append(ganador)
                return 

        elif ganador == 'P2':
            if marcador_index2 < len(marcador_p2) - 2:
                marcador_index2 += 1
                yield f'Marcador: {marcador_p1[marcador_index1]} - {marcador_p2[marcador_index2]}'
                lista_puntos.append(ganador)
            else:
                print('El ganador es P2!')
                lista_puntos.append(ganador)
                return f'Marcador final = {marcador_p1[marcador_index1]} - {marcador_p2[marcador_index2]}'
                
        else:
            print('vuelve a ingresar un ganador')
    

juego = tenis()

for marcador in juego:
    print(marcador)