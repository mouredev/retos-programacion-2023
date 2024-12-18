# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def es_fibonacci(n):
    if n < 0:
        return False
    
    def es_cuadrado_perfecto(x):
        raiz = int(x**0.5)
        return x == raiz * raiz
    
    return es_cuadrado_perfecto(5 * n * n + 4) or es_cuadrado_perfecto(5 * n * n - 4)

def es_par(n):
    return n % 2 == 0


def analizar_numero(n):
    primo = "es primo" if es_primo(n) else "no es primo"
    fibonacci = "es fibonacci" if es_fibonacci(n) else "no es fibonacci"
    paridad = "es par" if es_par(n) else "es impar"
    
    print(f"{n} {primo}, {fibonacci} y {paridad}")

try:
    n = int(input("Introduce un número: "))
    analizar_numero(n)
except ValueError:
    print("Por favor, introduce un número válido.")

