"""""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def es_primo(numero):
    for n in range(2,numero):
        if((numero % n) == 0):
            return 'No es primo'


    return 'Es Primo'

def es_fibonnacci(numero):
    a = 0
    b = 1

    while a < numero + 1:
        if a == numero: return 'Es fibonnacci'
        a,b = b,a+b

    return 'No es fibonnacci'


def verificar(numero):
    es_par = 'No es par'
    if (numero % 2) == 0: 
        es_par = 'Es par'

    return f'[{numero}] -{es_primo(numero)}- -{es_fibonnacci(numero)}- -{es_par}-'


if __name__ == '__main__':
    numero = input('Escribe un numero a verificar:\n')
    print('\n',verificar(int(numero)))