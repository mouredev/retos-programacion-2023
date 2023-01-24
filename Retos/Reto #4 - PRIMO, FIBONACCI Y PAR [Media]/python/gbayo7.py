# 
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
# 

from math import sqrt


def es_fibonacci(n):
    '''Compruea si n esta en la secuencia de Fibonacci. Devuelve True si lo está, en caso contrario devuelve False.'''    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

def es_primo(n):
    '''Comprueba si un nuero es primo. Devuelve True si lo es, en caso contrario devuelve False.'''
    if (n < 2):
        return False
    
    for x in range(2, n):
        if(n%x==0):
            return False
    return True

def es_par(n):
    '''Comprueba si un nuero es par. Devuelve True si lo es, en caso contrario devuelve False.'''
    if(n%2==0):
        return True
    return False

def check_number(n):
    output = f'{n} '
    if(es_primo(n)):
        output += 'es primo, '
    else:
        output += 'no es primo, '
    if(es_fibonacci(n)):
        output += 'es fibonacci y '
    else:
        output += 'no es fibonacci y '
    if(es_par(n)):
        output += 'es par.'
    else:
        output += 'es impar'
    print(output)
    
def main():
    check_number(3)
    check_number(8)
    check_number(13)
    check_number(34)
    check_number(37)
    check_number(25)
    check_number(377)
    check_number(378)
main()

