#!/usr/bin/env python3

#secuencia = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
#secuencia = ['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P2']
#secuencia = ['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P1','P2','P1','P2','P2']

secuencia = []
puntuaciones = ['Love','15','30','40']
resultados = []
end_game = False

p1_historial = ['Love']
p2_historial = ['Love']

p1_points = 0
p2_points = 0

while end_game == False:
    play = input('Ingrese un P1 si es player 1 y un P2 si es un player 2: ')

    if play == 'P1':
        p1_points += 1
        if p1_points > 3:
            if p2_historial[-1] == '40' and p1_historial[-1] == '40':
                p1_historial.append('Deuce')
            if p1_historial[-1] == 'Ventaja P1' and abs(p1_points - p2_points) == 2:
                p1_historial.append('Ha Ganado P1')
                #resultados.append(p1_historial[-1])
                end_game = True
            elif p2_historial[-1] == 'Ventaja P2':
                p2_historial.append('Deuce')
                p1_historial.append('Deuce')
            elif p1_historial[-1] == 'Deuce':
                p1_historial.append('Ventaja P1')
        else:
            p1_historial.append(puntuaciones[p1_points])
    else: 
        p2_points += 1 

        if p2_points > 3:
            if p2_historial[-1] == '40' and p1_historial[-1] == '40':
                p2_historial.append('Deuce')
            if p2_historial[-1] == 'Ventaja P2' and abs(p1_points - p2_points) == 2:
                p2_historial.append('Ha Ganado P2')
                #resultados.append(p2_historial[-1])
                end_game = True
            elif p1_historial[-1] == 'Ventaja P1':
                p2_historial.append('Deuce')
                p1_historial.append('Deuce')
            elif p2_historial[-1] == 'Deuce':
                p2_historial.append('Ventaja P2')

        else:
            p2_historial.append(puntuaciones[p2_points])

    if p1_historial[-1] == '40' and p2_historial[-1] == '40' or p1_historial[-1] == 'Deuce' and p2_historial[-1] == 'Deuce':
        #print(f'Deuce')
        resultados.append('Deuce')
    elif p1_historial[-1] == 'Ventaja P1':
        #print(p1_historial[-1])
        resultados.append(p1_historial[-1])
    elif p1_historial[-1] == 'Ha Ganado P1':
        #print(p1_historial[-1])
        resultados.append(p1_historial[-1])
    elif p2_historial[-1] == 'Ventaja P2':
        #print(p2_historial[-1])
        resultados.append(p2_historial[-1])
    elif p2_historial[-1] == 'Ha Ganado P2':
        #print(p2_historial[-1])
        resultados.append(p2_historial[-1])
    else:
        #print(f'{p1_historial[-1]} - {p2_historial[-1]}')
        resultados.append(f'{p1_historial[-1]} - {p2_historial[-1]}')



for resultado in resultados:
    print(resultado)

    


