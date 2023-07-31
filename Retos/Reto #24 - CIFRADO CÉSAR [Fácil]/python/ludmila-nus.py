'''Crea un programa que realize el cifrado César de un texto y lo imprima.
También debe ser capaz de descifrarlo cuando así se lo indiquemos.'''

# importamos modulo para imprimir por pantalla en color
from termcolor import colored

# programa saluda al usuario
print('---Bienvenido al sistema de codificación ROT13---')
print('')
# parametros de traduccion - el programa traducira el texto segun cifrado cesar (ROT13)
# sustituyendo cada letra, por la letra que está 13 posiciones por delante en el alfabeto
rot13_min = 'abcdefghijklmnopqrstuvwxyz'
rot13_may = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# creamos un ciclo while para que el programa siga funcionando hasta que el usuario no quiera traducir nada mas
continuar = True
while continuar:
    # Le pedimos al usuario que seleccione una opcion
    accion = input('¿Que accion necesita realizar? \n\t1-Realizar un cifrado a ROT13 \n\t2-Desifrar un texto codificado en ROT13 \n\t3-salir \n\topcion: ')
    print('')
    # segun la opcion que eliga 1, 2, o 3
    if accion == '1' or accion == '2':     
        # pedimos por pantalla un texto
        texto = input('Ingrese un texto: ')
        # copiamos el texto ingresada para no modifical la original
        texto_rot13 = texto
        # creamos un bucle para que recorra el texto y reemplace las letras
        for letra in texto:
            # si la letra del texto que escribio esta en minuscula 
            if letra in rot13_min:
                posicion = rot13_min.find(letra) + 13
                # si la posicion en menor a la longitud del abecedario
                if posicion < 26:
                    # reemplazamos la letra de la texto por la letra segun su ubicacion ( 13 lugares mas adelante)
                    texto_rot13 = texto_rot13.replace(letra,rot13_min[posicion])
                # si la posicion supera la longitud del abecedario    
                else :
                    # le restamos a la posicion la longitud del abecedario para que de la posicion correcta
                    posicion = posicion - 26
                    texto_rot13 = texto_rot13.replace(letra,rot13_min[posicion]) 
            # si la letra del texto que escribio esta en mayuscula 
            elif letra in rot13_may:
                posicion = rot13_may.find(letra) + 13
                # si la posicion en menor a la longitud del abecedario
                if posicion < 26:
                    # reemplazamos la letra de la texto por la letra segun su ubicacion ( 13 lugares mas adelante)
                    texto_rot13 = texto_rot13.replace(letra,rot13_may[posicion])
                # si la posicion supera la longitud del abecedario    
                else :
                    # le restamos a la posicion la longitud del abecedario para que de la posicion correcta
                    posicion = posicion - 26
                    texto_rot13 = texto_rot13.replace(letra,rot13_may[posicion]) 
       
        if accion == '1': 
            # el programa muestra por pantalla el texto traducido
            print(colored(f'Traduccion de texto a cifrado ROT13: \n{texto_rot13}','magenta'))
            
        elif accion == '2':
            # el programa muestra por pantalla el texto traducido
            print(colored(f'Desifrado de texto codificado en ROT13: \n{texto_rot13}','green')) 
            
        # preguntamos si quiere volver al menu de inicio de lo contrario el sistema se cierra
        print('')
        volver = input('¿Quiere volver al menu de inicio? si/no: ') 
        print('')
        if volver == 'no':
            print('Gracias por utilizar el sistema de codificacion ROT13')
            continuar = False

    elif accion == '3':
        print('Gracias por utilizar el sistema de codificacion ROT13')
        continuar = False
    
    else :
        print('')
        print(colored('¡Opcion invalida! \n--- seleccione una opcion correcta ---','yellow'))
        print('')


