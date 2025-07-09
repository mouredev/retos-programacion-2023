import math

def even(num):
    if num % 2 == 0:
        even_flg = True
    else:
        even_flg = False
    return even_flg

def primo(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def fibo(num):
    exp1 = 5*(num**2)+4
    exp2 = 5*(num**2)-4
    raiz1 = int(math.sqrt(exp1))
    raiz2 = int(math.sqrt(exp2))

    if raiz1 * raiz1 == exp1 or raiz2 * raiz2 == exp2:
        return True
    return False

def main():
    num = int(input("Ingresa un numero entero"))

    if even(num):
        par_lg = "es par"
    else:
        par_lg = "no es par"

    if primo(num):
        primo_lg = "es primo"
    else:
        primo_lg = "no es primo"

    if fibo(num):
        fibo_lg = "es fibonacci"
    else:
        fibo_lg = "no es fibonacci"

    print(f"{num} {primo_lg}, {fibo_lg} y {par_lg}")

main()