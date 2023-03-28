#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#Ejemplos:
#- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


switches = {
    'primo': 0,
    'fibo': 0,
    'par': 0
}

n = int(input('Ingrese un número: '))
#n = 1

def primo(nu):
    if n == 2 or n == 3 or n == 5 or n == 1:
        switches['primo'] = 1
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        pass
    else:
        switches['primo'] = 1


def build(di, nu):
    output = []
    if di['primo'] == 0:
        output.append(f'{nu} no es primo,')
    else:
        output.append(f'{nu} es primo,')
    
    if di['fibo'] == 0:
        output.append(f'no es fibonacci,')
    else:
        output.append(f'fibonacci,')

    if di['par'] == 0:
        output.append(f'y es par')
    else:
        output.append(f'y es impar')

    switches['primo'] = 0 
    switches['par'] = 0 
    switches['fibo'] = 0 

    return output

def is_fibo(nu):
    output = [0, 1]
    start = 0
    increase = 1
    stop = nu+1
    while start < stop:
        increase += start
        output.append(increase)
        start = output[-2]

    if nu in output:
        switches['fibo'] = 1

if n % 2 == 0:
    pass
elif n % 2 != 0:
    switches['par'] = 1
elif n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    primo(n)

primo(n)
is_fibo(n)
print(' '.join(build(switches, n)))

# iteración automática
#while n <= 10:
#    if n % 2 == 0:
#        pass
#    elif n % 2 != 0:
#        switches['par'] = 1
#    elif n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
#        primo(n)
#    
#    primo(n)
#    is_fibo(n)
#    print(' '.join(build(switches, n)))
#
#    n+=1

