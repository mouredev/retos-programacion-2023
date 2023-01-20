# string --> lista que describe la informacion para mostrar
score = 'love, 15, 30, 40, Iguales, Ha Ganado el, Ventaja, Player 1, Player 2, SIMULACION DE SET DE TENNIS ,*'
score_list = list(score.split(','))

# Titulo
print(score_list[10].center(70,'*'))
print(score_list[9].center(70,'-'))
print(score_list[10].center(70,'*'))

# Input
play = list(input('\n* Bienvenido\n* Epscribe una secuencia de p1 p2 como quieras separadas por espacio\
                   \n* Solo se usaran las palabras p1 P1 p2 P2, las demas seran descartadas\n\n').lower().split(' '))

# filtro de texto: crea una nueva lista solo reconociendo p1 o p2
players = []
for item in range(len(play)):
    if play[item] == 'p1':
        players.append('p1')
    if play[item] == 'p2':
        players.append('p2')

# puntos iniciales p1, p2
score_p1 = 0
score_p2 = 0

print('\nEl Resultado de la simulacion es:\n')
print(f'{score_list[7].center(12)}{score_list[8]}')
# ciclo para recorrer la lista y mostrar los resultados segun la cantidad de puntos
for point in range(len(players)):
    # Sumar puntos segun la informacion p1 o p2
    if players[point] == 'p1':
        score_p1 += 1  
    if players[point] == 'p2':
        score_p2 += 1
    # mostrar el comportamiento de los primeros puntos love, 15, 30 y 40
    if score_p1 <= 3 and score_p2 <= 3:
        print(f'{score_list[score_p1].center(10)}     {score_list[score_p2]}')
    
    # si la puntuacion es 40 - 40 muestra Iguales
    if score_p1 == 3 and score_p2 == 3:
        print(f'{score_list[4].center(20)}\n')
    
    # si estan empatados 40-40 y alguno anota un punto se muestra: ventaja P1 o P2
    if score_p1 == 4 and score_p2 == 3:
        print(f'{score_list[6]}{score_list[7]}')
    elif score_p1 == 3 and score_p2 == 4:
        print(f'{score_list[6]}{score_list[8]}')

    # si despues de tener ventaja, el contrincante anota un punto volveran a estar 40 40
    if score_p1 == 4 and score_p2 == 4:
        print(f'{score_list[4]} de nuevo\n')
        score_p1 -= 1
        score_p2 -= 1

    # si se obtienen 4 puntos con una diferencia mayor o igual a 2 puntos
    # o el primero que obtenga 5 puntos --> hay un ganador y se termina el ciclo
    if score_p1 == 4 and score_p2 <3 or score_p1 == 5:
        print(f'{score_list[5]}{score_list[7]}\n')
        break
    elif score_p2 == 4 and score_p1 <3 or score_p2 == 5:
        print(f'{score_list[5]}{score_list[8]}\n')
        break