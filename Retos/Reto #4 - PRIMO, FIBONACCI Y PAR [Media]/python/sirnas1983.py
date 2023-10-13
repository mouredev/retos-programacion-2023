import math

def secuencia_fibo(n) -> list:
    def recursiva(n):
        if n<=1:
            return n
        else:
            return recursiva(n-2) + recursiva(n-1)
    resp = []
    i = 0
    while (fibo := recursiva(i)) <= n:
        resp.append(fibo)
        i += 1
    return resp

def es_fibonacci(n):
    if n in secuencia_fibo(n):
        return True
    return False

def es_primo(n):
    for i in range(2,math.ceil((n**.5)) + 1):
        if n < 2:
            primo = False
            break
        elif n == 2:
            primo =True
            break
        elif n%i == 0:
            primo = False
            break
        elif i == math.ceil((n**.5)):
            primo = True
    return primo

def es_par(n):
    if n%2 == 0:
        return True
    return False

def primo_fibo_paridad(n):
    primo = es_primo(n)
    fibo = es_fibonacci(n)
    par = es_par(n)
    resp = f'{n} {"es" if primo else "no es"} primo{", fibonacci" if fibo else ""} y {"es par" if par else "es impar"}.'
    return resp

j = 610
print(primo_fibo_paridad(j))
