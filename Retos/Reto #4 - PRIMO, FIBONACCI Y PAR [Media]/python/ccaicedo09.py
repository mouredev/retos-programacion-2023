"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""


def is_prime(num: int):

    if num <= 1:
        return False

    for i in range(2,num):
        if num%i == 0:
            return False
        
    return True


def is_fibonacci(num: int):
    numOne = 1
    numTwo = 1
    while numTwo < num:
        [numOne, numTwo] = [numTwo, numOne + numTwo]

    return numTwo == num or num == 1


def is_even(num: int):
    
    if num%2 == 0:
        return True
    else:
        return False


def main(num):

    result = f"El número {num}"
    result += f" es primo," if is_prime(num) else " no es primo,"
    result += f" fibonacci " if is_fibonacci(num) else " no es fibonacci "
    result += f"y es par" if is_even(num) else "y es impar"

    return result


print(main(2))
print(main(7))
