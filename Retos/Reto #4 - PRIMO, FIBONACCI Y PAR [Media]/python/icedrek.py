"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
def is_prime(number):
    if number > 2 and number != 4:
        for i in range(2, int(number/2)):
            if number%i == 0:
                return False
        return True

    return False

def is_fibonacci(number):
    list = [0, 1]

    while True:
        n_fibo = list[-1] + list[-2]
        list.append(n_fibo)

        if n_fibo >= number:
            break

    return True if number in list else False

def is_even(number):
    return True if number%2 == 0 else False


number = int(input("Introduce un numero: "))

print(f"El numero {number}:")
print(" - Es primo")     if is_prime(number)     else print(" - No es primo")
print(" - Es Fibonacci") if is_fibonacci(number) else print(" - No es Fibonacci")
print(" - Es Par")       if is_even(number)      else print(" - Es Impar")
