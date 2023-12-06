
# Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  fibonacci y par.
#  Ejemplos:
#  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


def identify_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def identify_prime(number):
    divisibles = 0
    for i in range(1,number+1):
        if number % i == 0:
            divisibles += 1

    return divisibles == 2


def identify_perfect_square(number):
    odd = 1
    while number > 0:
        number -= odd
        odd += 2
    
    return number == 0


def identify_fibonacci(number):
    case_a = 5*(number**2)-4
    case_b = 5*(number**2)+4

    return (identify_perfect_square(case_a) or identify_perfect_square(case_b))


if __name__ == '__main__':
    number = int(input('Digite un número: '))
    number_result = str(number)
    if identify_prime(number):
        number_result += ' es primo,'
    else:
        number_result += ' no es primo,'
    if identify_fibonacci(number):
        number_result += ' es Fibonacci,'
    else:
        number_result += ' no es Fibonacci,'
    if identify_even(number):
        number_result += ' es par.'
    else:
        number_result += ' es impar.'

    print(number_result)