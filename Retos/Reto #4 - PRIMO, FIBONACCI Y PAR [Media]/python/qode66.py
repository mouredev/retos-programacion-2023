
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


def es_par(p): #determina si el número es par
    if p%2 == 0:
        prop1 = " es par,"
    else:
        prop1 = " es impar,"
    return prop1

def es_fibo(n): #determina si pertenece a la serie fibonacci
    a, b = 0, 1
    while a < n:
        if a == n:
            prop2 = " pertenece a fibonacci,"
        else:
            prop2 = " no pertenece a fibonacci,"
        a, b = b, a+b
    return prop2

def es_primo(u): #determina si el número es primo
    for i in range(2, u):
        if u%i == 0:
            prop3 = " no es primo,"
            break
        else:
            prop3 = " es primo,"
    return prop3

x = "s"
while x == "s" or x == "S":
    n = int(input("Introduce un número entero mayor que 1: "))
    s = "El número " + str(n) + "," + es_par(n) + es_fibo(n) + es_primo(n)
    print(s)
    x = input("¿Otro cálculo? s/n: ")