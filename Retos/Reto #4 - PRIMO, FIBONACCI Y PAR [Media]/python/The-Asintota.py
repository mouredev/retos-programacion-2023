'Reto #4: PRIMO, FIBONACCI Y PAR'
'''
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.

Ejemplos:
*Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
*Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

def check(num):
    
    if num < 0 or type(num) == type(1.0):
        return 'El numero debe ser un entenero positovo.'

    resultado = ''

    #numero par o impar
    if num % 2 == 0:
        resultado += 'El nunero {} es par, '.format(num)

    else:
        resultado += 'El numero {} es impar, '.format(num)

    #numero de fibbonaci
    pos_0 = 0
    pos_1 = 1
    fibbo = False

    while pos_0 <= num:
        if pos_0 == num:
            fibbo = True

        suma = pos_0 + pos_1
        pos_0 = pos_1
        pos_1 = suma

    if fibbo == True:
        resultado += 'pertenece a la sucesion de fibbonaci y '

    else:
        resultado += 'no pertenece a la sucesion de fibbonaci y '

    #numero primo
    primo = True

    if num == 2:
        resultado += 'es primo.'

    elif num == 1:
        resultado += 'no es primo.'

    else:
        for n in range(2, num):
            if num % n == 0:
                primo = False

        if primo == True:
            resultado += 'es primo.'

        else:
            resultado += 'no es primo.'

    return resultado