"""
## Enunciado

```
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
```
"""

def is_even(number):
    if number % 2 == 0:
        return 'es par'
    else:
        return 'es impar'
    
def is_prime(number):
    if number < 2:
        return True
    
    prime = 0
    
    for digit in range(2,number):
        if number % digit == 0:
            prime += 1
            
    if prime:
        return 'no es primo'
    else:
        return 'es primo'

def fibonacci(number):
    first = 0
    second = 1
    fibo = []
    
    for digit in range(number):
        third = first + second
        fibo.append(third)
        first,second = second,third
    
    if number in fibo:
        return 'fibonacci'
    else:
        return 'no es fibonacci'
    
def check_number():
    number = int(input('Ingrese un numero para chequear si es primo, es fibonacci y si es par o impar: '))
    
    print(f"{number} {is_prime(number)}, {fibonacci(number)} y {is_even(number)}")
    
check_number()