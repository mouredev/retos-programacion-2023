"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def isPrime(number):
    if number == 1 or number <= 0: return False
    i = 2
    while i < number:
        if number % 2 == 0: return False
        i += 1
    return True

def isFibonacci(number):
    currentFib = 0
    nextFib = 1
    while currentFib <= number:
        if currentFib == number: return True       
        aux = currentFib + nextFib
        currentFib = nextFib
        nextFib = aux
    return False

def isEven(number):
    return number % 2 == 0

def checkNumber(number):
    answer = f"{number} es primo," if isPrime(number) else f"{number} no es primo,"
    answer += " es fibonacci" if isFibonacci(number) else " no es fibonacci"
    answer += " y es par" if isEven(number) else " y es impar"
    return answer

print(checkNumber(2))    # 2 es primo, es fibonacci y es par
print(checkNumber(7))    # 7 es primo, no es fibonacci y es impar
print(checkNumber(8))    # 8 no es primo, es fibonacci y es par