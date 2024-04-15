"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""

def is_prime(number: int) -> str:
    """
    This function check if a given number is prime.

    Args:
        number (int): any number

    Returns:
        str: returns if is the number is prime or not.
    """
    try:
        if number > 1:
            for digit in range(2,number):
                if number % digit == 0:
                    return f'The number {number} is not prime'
        return f'The number {number} is prime'
    except ValueError:
        print('El valor debe ser un numero entero')

def is_even(number: int) -> str:
    """
    This code evaluate if a given number is even or odd.

    Args:
        number (int): any number

    Returns:
        str: if the number is even or odd
    """
    if number % 2 == 0:
        return 'is even'
    return 'is odd'

def fibonacci(number: int) -> str:
    """
    This function checks if a given number is part of the fibonacci sequence.

    Args:
        number (int): any number

    Returns:
        str: returns if the given number is in the fibonacci sequence.
    """
    first = 0
    second = 1
    third = 0
    
    while third < number:
        third = first + second
        first = second
        second = third
    if third == number:
        return 'is fibonacci'
    return 'is not fibonacci'

number = 2
print(f'{is_prime(2)}, {fibonacci(2)} and {is_even(2)}')    
number = 7
print(f'{is_prime(7)}, {fibonacci(7)} and {is_even(7)}')    

def check_number():
    number = int(input('Ingrese un numero: '))
    print(f'{is_prime(number)}, {fibonacci(number)} and {is_even(number)}')    
check_number()