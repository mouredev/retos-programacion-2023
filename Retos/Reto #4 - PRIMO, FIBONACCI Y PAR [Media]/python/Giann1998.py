"""
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 """
def par(numero):
    if numero%2==0:
        return 'par'
    else:
        return 'impar'
def fibonacci(numero):
    a=0
    b=1
    sucesion=[a,b]
    c=0
    while c<numero:
        c=b+a
        sucesion.append(c)
        a=b
        b=c
    if numero in sucesion:
        return 'fibonacci'
    else:
        return 'no es fibonacci'
def primo(numero):
    cont=2
    if numero==2:
        return 'primo'

    while cont<numero:
        if numero%cont!=0:
            if cont==numero-1:
                return 'primo'
            else:
                cont+=1
        elif numero%cont==0:
            return 'no es primo'

def reto_4(number):
    return f'{number} es {primo(number)}, {fibonacci(number)} y es {par(number)}'


print(reto_4(2))
print(reto_4(7))
