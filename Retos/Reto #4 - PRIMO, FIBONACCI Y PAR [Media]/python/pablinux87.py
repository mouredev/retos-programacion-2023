'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 '''
import math
 
def primo(num:int)->str:
    for n in range(2, num):
        if num % n == 0:
            return ' no es primo,'
    return ' es primo,'

def par(num:int)->str:
    if num % 2 == 0:
        return ' es par,'
    return ' no es par,'

def fibonacci(num:int)->str:
    if num > 0 and (is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)):
        return ' fibonacci'
    return ' no es fibonacci'

def is_perfect_square(num:int)->bool:
    sqrt = int(math.sqrt(num))
    return sqrt * sqrt == num

def evaluate(num:int):
    finish=str(num) + primo(num)+ par(num) + fibonacci(num)
    return finish
    
if __name__=='__main__':
    print(evaluate(int(input('Ingrese el numero a evaluar -> '))))