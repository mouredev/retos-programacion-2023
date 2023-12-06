'''
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''


def comprobar(n):
    solucion = str(n)+" "

    if(primo(n)):
        solucion += " es primo, "
    else:
        solucion += " no es primo, "
    
    
    if(fibo(n)):
        solucion += "fibonacci "
    else:
        solucion += "no es fibonacci "
    
    if n % 2 == 0:
        solucion += "y es par"
    else:
        solucion += "y es impar"

    print(solucion)


def primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True



def fibo(n):
    a = 0
    b = 1

    if n == a or n == b:
        return True
    
    while b < n:
        c = a + b
        if c == n:
            return True
        a = b
        b = c

    return False



comprobar(7)
comprobar(2)