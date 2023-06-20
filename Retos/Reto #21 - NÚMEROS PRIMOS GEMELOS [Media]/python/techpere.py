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


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_pares_gemelos(rango):
    pares_gemelos = []
    for num in range(2, rango):
        if es_primo(num) and es_primo(num + 2):
            pares_gemelos.append((num, num + 2))
    return pares_gemelos

rango_maximo = int(input("Ingrese el rango máximo: "))
pares_gemelos = encontrar_pares_gemelos(rango_maximo)

print("Pares de números primos gemelos:")
for par in pares_gemelos:
    print(par)
