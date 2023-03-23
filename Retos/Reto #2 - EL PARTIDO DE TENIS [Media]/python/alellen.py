'''
    Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
    El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
    gane cada punto del juego.

    - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
    - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
    15 - Love
    30 - Love
    30 - 15
    30 - 30
    40 - 30
    Deuce
    Ventaja P1
    Ha ganado el P1
    - Si quieres, puedes controlar errores en la entrada de datos.   
    - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''

points = ('P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1')
system_points = {0: 'Love', 1: '15', 2: '30', 3: '40'}
p1_points, p2_points = 0, 0

for point in points:
    if point == 'P1': p1_points += 1
    else: p2_points += 1

    if (p1_points + p2_points) <= 5:
        print(f'{system_points[p1_points]} - {system_points[p2_points]}')

    if p1_points == p2_points and (p1_points + p2_points) >= 6:
        print('Deuce')
    
    if (p1_points + p2_points) > 6 and (p1_points + p2_points) % 2 != 0:
        print(f'Ventaja {point}')

    if (p1_points + p2_points) >= 8 and (p1_points - p2_points) in (2, -2):
        print(f'Ha ganado el {point}')