# Reto 4
 # Escribe un programa que, dado un número, compruebe y muestre si es primo,
 # fibonacci y par.
 # Ejemplos:
 # - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 # - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#
import math

def check_prime_fibonacci_even(number):
    result = f"{number} "
    # Primo
    if number > 1:
        for index in range (2,number):
            if  number % index == 0:
                result += "no es primo, "
                break
        else:
            result += "es primo, "
    else: 
        result += "no es primo, "

    # Fibonacci
    result += "es fibonacci " if number > 0 and is_perfect_square (( 5 * number * number + 4) or is_perfect_square  ( 5 * number * number - 4)) else "no es fibonacci " 
            
    # Par  
    result += "y es par" if number %2 == 0 else "y es impar"          
 
    print(result)

def is_perfect_square(number): # cuadrado perfecto
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

check_prime_fibonacci_even(2)
check_prime_fibonacci_even(7)
check_prime_fibonacci_even(0)