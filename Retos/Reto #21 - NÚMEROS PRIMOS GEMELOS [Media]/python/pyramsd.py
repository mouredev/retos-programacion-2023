def primos(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gemelos(r):
    diferencia = 2
    lista_rangos = []
    for i in range(2, r+1):
        if primos(i):
            if i - diferencia == 2:
                lista_rangos.append((diferencia, i))
            diferencia = i

    print(lista_rangos)

gemelos(14)
