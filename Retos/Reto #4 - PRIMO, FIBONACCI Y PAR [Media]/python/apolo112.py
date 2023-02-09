"""
```
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
```
"""

def is_par (num):
    if type(num) != int:
        raise Exception("The number is not a integer")

    if num % 2 == 0 and num != 1:
        return True
    else:
        return False


def is_fibonacci (num):
    if type(num) != int:
        raise Exception("The number is not a integer")
    n =[0, 1]
    while(True):

        if n[-1] == num or num == 0:
            return True
        elif n[-1] > num:
            return False
        n.append(n[-2]+n[-1])

def is_primo(num):

    if num == 1:
        return True
    for i in range (2, int(num/2) +1):
        if num % i == 0: return False

    return True
        

def comprovar(num):
    if type(num) != int:
        raise Exception("The number is not a integer")

    if is_primo(num):
        primo= 'es primo'
    else:
        primo="no es primo"
    
    if is_fibonacci(num):
        fibo = "es fibonacci"
    else:
        fibo = "no es fibonacci"
    
    if is_par(num):
        par = "es par"
    else:
         par = "no es par"

    print(f"El {num} {primo}, {fibo} y {par} ")




num_1= 21
comprovar(num_1)
num_2= 28657
comprovar(num_2)
num_3= 144
comprovar(num_3)
"""
num_4= 2971215073
comprovar(num_4)
"""
num_5=6
comprovar(num_5)