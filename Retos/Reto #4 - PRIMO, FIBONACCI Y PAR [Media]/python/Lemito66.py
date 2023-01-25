""" 
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

"""


def is_even(number: int):
    if number % 2 == 0:
        return True
    else:
        return False


def is_fibonacci(number: int):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21
    list_of_number = [0, 1]
    for i in range(2, 2500):
        list_of_number.append(list_of_number[i-2]+list_of_number[i-1])
    if number in list_of_number:
        return True
    else:
        return False


def is_prime(number: int):
    count = 0
    if number > 0:
        for i in range(1, number+1):
            if number % i == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False
    else:
        return False


def isprime_isfibonnaci_is_even(number: int):
    result = ''
    if is_prime(number):
        result += 'es primo, '
    else:
        result += 'no es primo, '
    if is_fibonacci(number):
        result += 'fibonacci '
    else:
        result += 'no es fibonacci '
    if is_even(number):
        result += 'y es par'
    else:
        result += 'y es impar'
    return f'{number} {result}.'


print(isprime_isfibonnaci_is_even(2))
print(isprime_isfibonnaci_is_even(7))

