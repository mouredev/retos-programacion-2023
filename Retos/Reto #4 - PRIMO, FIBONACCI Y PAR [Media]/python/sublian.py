"""
Reto #4: PRIMO, FIBONACCI Y PAR
    Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
import math

def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt*sqrt==number

def check_prime_fibonacci_pair(number):
    
    result =f"{number}: "
    #primo
    if number > 1:
        for index in range(2,number):
            if number%index==0:
                result +="No es primo,"
                break
        else:
            result +="Es primo,"
    else:
        result +="No es primo,"
    
    #fibonacci
    result += " Es Fibonacci" if number>0 and(is_perfect_square(5*number*number+4) or is_perfect_square(5*number*number-4)) else " No es Fibonacci"

    #par
    result += ", es par!" if number %2 ==0 else ", es impar!"
    print(result)

if __name__ == '__main__':
    
    value= int(input("Ingrese valor a evaluar: "))
    check_prime_fibonacci_pair(value)