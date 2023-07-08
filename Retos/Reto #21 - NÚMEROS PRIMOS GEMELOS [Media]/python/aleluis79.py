# Crea un programa que encuentre y muestre todos los pares de números primos
# gemelos en un rango concreto.
# El programa recibirá el rango máximo como número entero positivo.

# - Un par de números primos se considera gemelo si la diferencia entre
#   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
# - Ejemplo: Rango 14
#   (3, 5), (5, 7), (11, 13)

def es_primo(numero: int):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def primos_gemelos(rango: int):
    primo_anterior = 2
    rangos = []
    for i in range(2, rango+1):
        if es_primo(i):
            if (i - primo_anterior == 2):
                rangos.append((primo_anterior, i))
            primo_anterior = i

    for i, rango in enumerate(rangos):
        print(str(rango) + ", " if i < len(rangos)-1 else str(rango), end="")
    
    print()

primos_gemelos(7)
primos_gemelos(14)
primos_gemelos(100)
