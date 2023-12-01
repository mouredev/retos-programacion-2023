'''
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
'''

def PedirNumero():
    while True:
        ingresado=input("Ingrese un numero: ")
        try:
            numero=int(ingresado)
            if numero<10 and numero>0:
                return numero
            else:
                print("Ingrese un numero del 1 al 10")
        except ValueError:
            print("Ingrese un numero correcto")

def TablaMultiplicar(numero):
    print(f"TABLA DEL {numero} ")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

TablaMultiplicar(PedirNumero())