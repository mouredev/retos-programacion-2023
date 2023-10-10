""" 
* Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 """ 
 
def tabla_multiplicar(numero):
    if(type(numero) == int or type(numero) == float):
        for index in range(1, 11):
            multiplicacion = index*numero
            print(f'{numero} X {index} = {multiplicacion}')

tabla_multiplicar(10)
tabla_multiplicar(10.0)
tabla_multiplicar(-10)