# -*- coding: utf-8 -*-

# Reto #4: PRIMO, FIBONACCI Y PAR
#
#  Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  fibonacci y par.
#  Ejemplos:
#  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  

message_helper = {
    True: "is",
    False: "isn't"
}

def fibonacci(number: int):
    '''
    Fibonacci using loop while
    '''
    serie = []
    stop = False
    while number >= 0:
        x = serie[-2] if len(serie) > 1 else 0
        y = serie[-1] if len(serie) > 1 else 1 * len(serie)
        z = x + y
        serie.append(z)
        if z > number:
            break
    return serie

def is_prime(number: int) -> bool:
    '''
    Define if a number is prime
    '''
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_even(number: int) -> bool:
    '''
    Define if a number is even
    '''
    if number % 2 == 0:
        return True
    return False

def is_fibinacci(number: int, x: int = 0, y: int = 1) -> bool:
    '''
    Fibonacci using recursion
    '''
    z = x + y
    if number == z:
        return True
    elif number > z:
        return is_fibinacci(number=number, x=y, y=(x + y))
    else:
        return False

def number_analize() ->str:
    result = f""
    source = input("Enter a number:\n")
    try:
        number = int(source)
        result = f"{number} {message_helper[is_prime(number=number)]} prime, {message_helper[is_fibinacci(number=number)]} fibonacci and {message_helper[is_even(number=number)]} even."
    except ValueError as e:
        result = f"Value error. {source} {message_helper[False]} integer.\nDescription: {e}"
    finally:
        print(result)

if __name__ == '__main__':
    number_analize()
