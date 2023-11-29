''' * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"'''

def par(num):
    return num % 2 == 0

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibo(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def veri():
    try:
        num = int(input("Ingrese un número: "))
        if primo(num) and fibo(num) and par(num):
            print(f"{num} es primo, fibonacci y es par")
        elif primo(num) and fibo(num) and not par(num):
            print(f"{num} es primo, fibonacci y es impar")
        elif primo(num) and not fibo(num) and par(num):
            print(f"{num} es primo, no es fibonacci y es par")
        elif primo(num) and not fibo(num) and not par(num):
            print(f"{num} es primo, no es fibonacci y es impar")
        elif not primo(num) and fibo(num) and par(num):
            print(f"{num} no es primo, es fibonacci y es par")
        elif not primo(num) and fibo(num) and not par(num):
            print(f"{num} no es primo, es fibonacci y es impar")
        elif not primo(num) and not fibo(num) and par(num):
            print(f"{num} no es primo, no es fibonacci y es par")
        elif not primo(num) and not fibo(num) and not par(num):
            print(f"{num} no es primo, no es fibonacci y es impar")
    except ValueError:
        print("Por favor, ingrese un número válido.")


veri()
