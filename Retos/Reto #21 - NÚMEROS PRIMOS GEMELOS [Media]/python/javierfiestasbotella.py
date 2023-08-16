'''/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */'''
lista=[1,2,3,5,7,11]
rango=int(input('Introduzca el rango donde buscar: '))
for i in range(rango):
    solucion=[]
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i!=1:
        lista.append(i)
for numero in range(len(lista)-1):
    if lista[numero+1]-lista[numero]==2:
        solucion.append((lista[numero],lista[numero+1]))
for tupla in  solucion:
    print(tupla, end=', ')