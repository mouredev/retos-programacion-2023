"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
import math as m

def is_even(number)->bool:
    return ((number%2)==0)

def is_prime(number)->bool:
    
    upperbound = m.sqrt(number) 
    i = 2 
    while ( number % i != 0 ) and (i <= upperbound):
        i=i+1
    
    return i>upperbound
        
    
def is_perfect_square(number)->bool:
    square = int(m.sqrt(number))
    return ((square*square) == number )


def is_fibonacci(number)->bool:
    return is_perfect_square(5*number*number+4) or is_perfect_square(5*number*number-4)


def is_prime_fib_even(number)->str:
    es_primo     = (' no', '')[is_prime(number)] + ' es primo, '
    es_fibonacci = (' no', '')[is_fibonacci(number)] + ' es fibonacci, '
    es_par       = (' es impar ', ' es par')[is_even(number)]
    
    return es_primo+es_fibonacci+es_par
    
num1 = 2
num2 = 7

print(num1 , is_prime_fib_even(num1))
print(num2 , is_prime_fib_even(num2))

# Más Tests :P - del 2 al 19
for i in range(1,20):
    print(i , is_prime_fib_even(i))
    