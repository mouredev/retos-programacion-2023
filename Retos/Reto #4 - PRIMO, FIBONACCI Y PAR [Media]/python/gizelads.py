""" Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar" """

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def es_fibonacci(num):
    aux1 = 0
    aux2 = 1
    fibo = 0
    while fibo < num:
        fibo = aux1 + aux2
        aux1 = aux2
        aux2 = fibo

    if num == fibo:
        return True
    else:
        return False


def es_primo(num):
    cont = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
    
    if cont == 2:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un numero: "))
    respuesta = ""

    if es_primo(numero):
        respuesta = str(numero) + " es primo, "
    else:
        respuesta = str(numero) + " no es primo, "

    if es_fibonacci(numero):
        respuesta += "fibonacci y "
    else:
        respuesta += "no es fibonacci y "
    
    if es_par(numero):
        respuesta += "es par."
    else:
        respuesta += "es impar."
    
    print(respuesta)


if __name__ == "__main__":
    run()