# /*
#  * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  *
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)
#  */

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

rango = int(input('Ingrese un número para el rango máximo: '))
primos = []
cadena = ''
x = 1
while x <= rango:
    if esPrimo(x):
        primos.append(x)
    x +=1

for i in range(len(primos)):
    if i > 1:
        if (primos[i] - primos[i-1] == 2):
            cadena = cadena + f' ({primos[i-1]} {primos[i]})'
if cadena == '':
    print('No hay primos gemelos')
else:
    print(cadena)