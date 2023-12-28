'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def esPrimo(n):
    if n<=1: return False
    r=True
    for j in range (2,n):
        if n%j==0:
            r=False
            break
    return r

        
def esFibonaci(n):
    f=1
    f1=1
    f2=0
    while f<n:
        f=f1+f2
        f2=f1
        f1=f
    return f==n


def esPar(n):
    return n%2==0


def reto4(n):
    p = f'{n} '
    if(esPrimo(n)):
        p+=f'es '
    else:
        p+=f'no es '
    p+='primo, '
    if(not(esFibonaci(n))):
        p+=f'no es '
    p+='Fibonacci y es '
    if(esPar(n)):
        p+=f'par.'
    else:
        p+=f'impar.'
    
    return p


if (__name__ == '__main__'):
    numero = str(input('Ingrese un Número: '))
    try:
        numero=int(numero)
        print (reto4(numero))
    except ValueError:
        print (f'el valor ingresado << {numero} >> no es un número valido...')