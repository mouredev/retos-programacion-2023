
numero = 13


def is_fibo(number):
    x = 0
    y = 1
    z = 0
    lista = []
    resultado = ""
    for i in range(0,number+1):
        z = x + y
        x = y
        y = z
        lista.append(z)

    if number in lista:
        resultado += "es fibonacci"
        return resultado
    else:
        resultado += "no es fibonacci"

    return resultado


def is_pair(number):
    resultado = ""
    if number % 2 == 0:
        resultado += "es par"
        return resultado
    else:
        resultado += "es impar"
    
    return resultado



def is_prime(number):
    resultado = ""
    c = 0
    for i in range(2,number):
        if number % i == 0:
            c += 1
    if c > 0:
        resultado += 'no es primo'
        return resultado
    else: 
        resultado += 'es primo'
    
    return resultado

print(f"{numero}, {is_prime(numero)}, {is_fibo(numero)} y {is_pair(numero)} ")
