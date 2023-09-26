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

def es_primo(n:int):
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True
    else:
      return False
def primos_gemelos(n:int):
    primo_1 = 1
    gemelos = []
    for i in range(1, n):
        # si es primo lo comparo con le anterior, si la dif es 2 guardo el par
        if es_primo(i): 
            primo_2 = i
            if primo_2 - primo_1 == 2:
                par = (primo_1, primo_2)
                gemelos.append(par)
            else:
                    primo_1 = primo_2
    return gemelos


print(primos_gemelos(1000))
