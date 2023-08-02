
'''
 Crea una función que reciba dos parámetros para crear una cuenta atrás.
 - El primero, representa el número en el que comienza la cuenta.
 - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 - Sólo se aceptan números enteros positivos.
 - El programa finaliza al llegar a cero.
 - Debes imprimir cada número de la cuenta atrás.
'''

import time

def cuenta_atras(inicio: int, segundos: int):
    for s in range(inicio, 0, -1):
        print(s)
        time.sleep(segundos)
    print('¡Cuenta atrás terminada!')


cuenta_atras(10, 1)
cuenta_atras(5, 3)