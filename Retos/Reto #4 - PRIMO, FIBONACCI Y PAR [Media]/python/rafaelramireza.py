'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def esPrimo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def esFibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a+b
    return a == num

def esPar(num):
    return num%2 == 0

def main():
    num = int(input("Ingrese un número: "))
    if esPrimo(num):
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")
    if esFibonacci(num):
        print(f"{num} es fibonacci")
    else:
        print(f"{num} no es fibonacci")
    if esPar(num):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

if __name__ == "__main__":
    main()