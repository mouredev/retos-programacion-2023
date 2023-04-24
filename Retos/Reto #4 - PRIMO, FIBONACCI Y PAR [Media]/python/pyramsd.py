def es_fibinacci(n):
    a, b = 0, 1
    while b < n:
        varTemp = a
        a, b = b, varTemp + b
    return b == n

def es_ParImpar(n):
    if n % 2 == 0:
        return True
    return False

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def respuestaFinal():
    res_final = ""
    if es_primo(num):
        res_final += "es primo, "
    else:
        res_final += "no es primo, "
    if es_fibinacci(num):
        res_final += "fibonacci, "
    else:
        res_final += "no es fibonacci, "
    if es_ParImpar(num):
        res_final += "y es par."
    else:
        res_final += "y es impar."
    return res_final

num = int(input("Numero: "))

print(f"{num} {respuestaFinal()}")
