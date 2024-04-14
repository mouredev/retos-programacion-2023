''' * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"'''

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

def es_par(numero):
    return numero % 2 == 0

def main():
    numero = int(input("Ingrese un número: "))

    if es_primo(numero):
        primo_str = "es primo"
    else:
        primo_str = "no es primo"

    if es_fibonacci(numero):
        fibonacci_str = "es fibonacci"
    else:
        fibonacci_str = "no es fibonacci"

    if es_par(numero):
        par_str = "es par"
    else:
        par_str = "es impar"

    resultado = f"{numero} {primo_str}, {fibonacci_str} y {par_str}"
    print(resultado)
    main()

if __name__ == "__main__":
    main()
