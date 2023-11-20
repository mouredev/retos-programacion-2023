# Reto #4: PRIMO, FIBONACCI Y PAR

# 
# 
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
# 


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_fibonacci(numero):
    # Un número es un cuadrado perfecto en la secuencia de Fibonacci si y solo si es mayor a 0 y (5 * n^2 + 4) o (5 * n^2 - 4) es un cuadrado perfecto    
    return numero > 0 and (((5 * numero**2 + 4)**0.5 % 1 == 0) or ((5 * numero**2 - 4)**0.5 % 1 == 0))

def es_par(numero):
    return numero % 2 == 0

def main():
    numero = int(input("Ingrese un número: "))

    if es_primo(numero):
        primo = "es primo"
    else:
        primo = "no es primo"

    if es_fibonacci(numero):
        fibonacci = "es fibonacci"
    else:
        fibonacci = "no es fibonacci"

    if es_par(numero):
        par = "par"
    else:
        par = "impar"

    resultado = f"{numero} {primo}, {fibonacci} y es {par}"
    print(resultado)

if __name__ == "__main__":
    main()
