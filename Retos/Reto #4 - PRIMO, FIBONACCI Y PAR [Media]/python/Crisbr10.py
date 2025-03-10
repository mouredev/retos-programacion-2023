'''*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 *'''
 
from math import sqrt

def es_fib(num:int):
    
    seq_fib = [0,1]
    i = 2
    
    while seq_fib[i-1] <= num:
        
        num_ant1 = seq_fib[i-2]
        num_ant2 = seq_fib[i-1]
        num_act = num_ant1 + num_ant2
        
        seq_fib.append(num_act)
        
        i+=1
    
    return True if num in seq_fib else False

def es_pri(num: int):
    
    raiz_num = int(sqrt(num) + 1)
    
    for i in range(2, raiz_num):
        
        if num % i == 0:
            return False
    return True

def es_par(num: int):
    return True if num % 2 == 0 else False

def check_num(num: int):
    
    num_fib = es_fib(num)
    num_pri = es_pri(num)
    num_par = es_par(num)
    
    response = f"{num} "
    
    if num_pri:
        response += "es primo"
    else:
        response += "no es primo"
        
    if num_fib:
        response += ", es fibonacci"
    else:
        response += ", no es fibonacci"
        
    if num_par:
        response += " y es par"
    else:
        response += " y es impar"

    return response

print(check_num(2))
print(check_num(7))