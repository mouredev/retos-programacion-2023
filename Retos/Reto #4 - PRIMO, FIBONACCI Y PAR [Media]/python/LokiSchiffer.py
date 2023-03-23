'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 '''

import math

def is_prime(number: int) -> bool:
    # comprobar si el número es par y así descartarlos todos con excepción del 2
    if (number < 2 or (number % 2 == 0 and number != 2)):
        return False
  
    # Se revisa el modulo empezando en 3 y sin tener en cuenta los pares
    for i in range(3, number // 2, 2):
        if (number % i == 0):
            return False

    return True

def fibonnaci(number: int) -> bool:
    # Se utliza la identidad de Binet para figurar si es de la secuencia de fibonnaci
    binet = 5 * number * number + 4
    if (float.is_integer(math.sqrt(binet))):
        return True
    binet = 5 * number * number - 4
    if (float.is_integer(math.sqrt(binet))):
        return True
    return False

def check_number(number: int) -> str:
    # Crea el mensaje sobre las condiciones descritas
    message = "El número " + (str)(number)
    message += "" if is_prime(number) else " no"
    message += " es primo,"
    message += "" if fibonnaci(number) else " no"
    message += " es fibonnaci y"
    message += " es impar" if number % 2 != 0 else " es par"
    return message
  
print(check_number(37))
print(check_number(73))
print(check_number(5))
print(check_number(2))
print(check_number(8))
print(check_number(46))
print(check_number(13))