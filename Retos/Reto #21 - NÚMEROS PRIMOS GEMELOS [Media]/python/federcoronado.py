'''
* Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
'''

rango = 1000

primo_1 = 1
gemelos = []
for i in range(1, rango):
    #determino si es primo
    primo = True
    for j in range(2,i):
        if i%j == 0:
            primo = False
    # si es primo lo comparo con le anterior, si la dif es 2 guardo el par
    if primo: 
        primo_2 = i
        if primo_2 - primo_1 == 2:
            par = (primo_1, primo_2)
            gemelos.append(par)
        else:
                primo_1 = primo_2
print(gemelos)
