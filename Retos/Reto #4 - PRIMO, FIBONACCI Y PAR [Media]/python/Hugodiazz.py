# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"



def esPar(numero):
    if numero % 2 == 0:
        return 'es par'
    else: 
        return 'es impar'

def esPrimo(numero):
    if numero <= 1:
        return 'no es primo'
    elif numero <= 3:
        return 'es primo'
    elif numero % 2 == 0 or numero % 3 == 0:
        return 'no es primo'
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return 'no es primo'
        i += 6
    return 'es primo'

def enFibo(numero):
    a, b, i = 0, 1, 0
    while i <= numero:
        c = a + b
        a = b
        b = c

        if a == numero:
            return 'es fibonacci'
            break
        elif a > numero:
            return 'no es fiboncacci'
            break
        
        i += 1
    return ''

def evaluarNumero(numero):
    par = esPar(numero)
    fibo = enFibo(numero)
    primo = esPrimo(numero)
    
    print(str(numero), primo, fibo + ' y ', par)


print(evaluarNumero(2))
print(evaluarNumero(7))