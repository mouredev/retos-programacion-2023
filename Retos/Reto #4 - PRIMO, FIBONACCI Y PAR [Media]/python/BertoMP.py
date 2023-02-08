def es_primo(numero):
    if numero == 1 or numero == 0 or numero == 4:
        return False

    for n in range(2, int(numero/2)):
        if numero % n == 0:
            return False

    return True


def es_par(numero):
    if numero % 2 == 0:
        return True
    return False


def es_fibonacci(numero):
    fibo1 = 0
    fibo2 = 1

    while fibo1 + fibo2 <= numero:
        fibo_aux = fibo1
        fibo1 = fibo2
        fibo2 = fibo_aux + fibo1
        if numero == fibo2:
            return True
        return False


def inicio():
    num = int(input("Dime un número: "))

    str_es_primo = " es primo," if es_primo(num) else " no es primo,"
    str_es_fibo = " es fibonacci y" if es_fibonacci(num) else " no es fibonacci y"
    str_es_par = " es par." if es_par(num) else " es impar."

    print(f"El número {num}{str_es_primo}{str_es_fibo}{str_es_par}")


inicio()
