# Escribe un programa que, dado un número, compruebe y muestre si es primo,
# fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

def check_input(expression_input):
    while True:
        number_characters = input(expression_input)
        try:
            number_characters = int(number_characters)
            print('>>> OK! \n')
            return number_characters
        except:
            print('>>> ERROR! Only accept numbers.\n')

#def check_even(number):
#    return True if number % 2 == 0 else False

def check_prime(number):
    if number < 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def check_fibonacci(number): #Algoritmo de Fibonacci n = n-1 + n-2
    n1, n2 = 0, 1
    if number > 0:
        while number >= n1:
            num_fibo = n1 + n2
            if number == n1:
                return True
            else:
                n1 = n2
                n2 = num_fibo

    return False

### Comporbar si es fibonaccion usando Formula de Binet (cuadrado perfecto)
### Correccion MoureDev
import math

def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

def check_fibonacci_2 (number):
    if is_perfect_square((5 * number * number + 4)) or is_perfect_square(5 * number * number + 4):
        return True
    else:
        return False

def check_number():
    number = check_input('>>> Input your number.\n')
    
    #is_par = check_even(number)
    is_even = True if number % 2 == 0 else False
    print(f'>>> Is the number even?: {is_even}.')
    
    is_prime = check_prime(number)
    print(f'>>> Is the number prime?: {is_prime}.')

    is_fibo = check_fibonacci(number)
    print(f'>>> Is the number fibonacci?: {is_fibo}.')

    return 


check_number()