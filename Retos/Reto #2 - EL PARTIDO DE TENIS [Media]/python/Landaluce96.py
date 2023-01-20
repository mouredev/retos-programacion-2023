"""
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
"""

def tennis():
    puntuacion = ('Love', '15', '30', '40', 'Deuce', 'Ventaja')
    dict = {'P1' : 'Love', 'P2' : 'Love'}
    fin = False

    print('Juego de tenis')
    print(dict['P1'] + ' - ' + dict['P2'])

    while not fin:
        correcto = False
        while not correcto:
            punto = input('¿Quién ha ganado el punto? (P1/P2) ').upper()
            if(punto == 'P1' or punto == 'P2'):
                correcto = True
        
        if punto == 'P1': otro = 'P2'
        else: otro = 'P1'

        if dict[punto] == 'Ventaja':
            print('Gana el juego ' + punto)
            break

        if dict[punto] == '40':
            print('Gana el juego ' + punto)
            break

        if dict['P1'] == 'Deuce' and dict['P2'] == 'Deuce':
            dict[punto] = puntuacion[puntuacion.index(dict[punto]) + 1]
        elif dict[punto] == 'Deuce':
            dict[otro] = puntuacion[puntuacion.index(dict[otro]) - 1]
        else :
            dict[punto] = puntuacion[puntuacion.index(dict[punto]) + 1]
        
        if dict['P1'] == '40' and dict['P2'] == '40':
            dict[punto] = puntuacion[puntuacion.index(dict[punto]) + 1]
            dict[otro] = puntuacion[puntuacion.index(dict[otro]) + 1]
            print('Deuce')
        elif dict[punto] == 'Ventaja':
            print('Ventaja ' + punto)
        elif dict['P1'] == 'Deuce' and dict['P2'] == 'Deuce':
            print('Deuce')
        else:
            print(dict['P1'] + ' - ' + dict['P2'])
      
tennis()