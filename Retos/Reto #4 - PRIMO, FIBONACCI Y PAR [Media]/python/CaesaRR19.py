def es_par(n: int) -> str:
    if n % 2 == 0:
        return "es par"
    return "es impar"


def es_fibo(n: int) -> str:
    a, b = 0, 1
    while n >= a:
        b, a = a + b, b
        if n == a:
            return "fibonnaci"
    return "no es fibonnaci"


def es_primo(n: int) -> str:
    for x in range(2, n - 1):
        if n % x == 0:
            return "no es primo"
    return "es primo"


def es_par_fibo_primo(n: int) -> str:
    par = es_par(n)
    fibo = es_fibo(n)
    primo = es_primo(n)
    return f"{n} {primo}, {fibo} y {par}"
