# ```
# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */
# ```

def is_prime(n):
    if n <= 1:
        return "no primo"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "no primo"
    return "primo"

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return "fibonacci" if a == n else "no fibonacci"

def is_even(n):
    return "par" if n % 2 == 0 else "impar"

if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    print(f"El numero {n} es {is_prime(n)}, {is_fibonacci(n)} y {is_even(n)}")