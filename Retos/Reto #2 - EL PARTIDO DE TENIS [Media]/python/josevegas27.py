'''
    RETO #2: EL PARTIDO DE TENIS
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

# Entrada lista

def partido_tenis(lista:  list):
    n,m = (0,0)

    for i in lista:
        if i not in ['P1','P2']: 
        	print ('Error en la entrada de datos')
        	return True

    puntos = ['Love','15','30','40','Ventaja','Ha ganado']

    cont_p1 = puntos[n]
    cont_p2 = puntos[m]
    for win in lista:

        if win == 'P1':
            n += 1
            cont_p1 = puntos[n]

        if win == 'P2':
            m += 1
            cont_p2 = puntos[m]


        if n == 4 and m == 4:
        	print('Empate')
        	print('\nFin del Juego')
        	return True

       	elif n == 5 or ( n == 4 and m < 3):
       		print('Ha ganado P1')
        	print('\nFin del Juego')
        	return True

       	elif m == 5 or ( m == 4 and n < 3):
       		print('Ha ganado P2')
        	print('\nFin del Juego')
        	return True

        elif n == 4 and m == 3:
        	print('Ventaja P1')

        elif n == 3 and m == 4:
        	print('Ventaja P2')

        elif n == 3 and m == 3:
        	print('Deuce')

        elif n <= 3 and m <= 3:
        	print(f'{cont_p1}-{cont_p2}')


puntos = input('Introduzca los puntos: ')
puntos_lsta = []
while True:
    puntos_lsta.append(puntos)
    if partido_tenis(puntos_lsta):
    	break
    puntos = input('\nSiguiente punto: ')
    if puntos not in ['P1','P2']: break
