from math import sqrt


def primo (n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

while True:
    try:
        entrada = int(input("rango máximo de los números: "))
    except ValueError as e:
        print("ERROR: ", e)
    else:
        break

lista_primos = [i for i in range(2, entrada + 1) if primo(i)]
print(lista_primos)

resultado = ""
while True:
    try:
        n1 = lista_primos[0]
        n2 = lista_primos[1]
        if n2 - n1 == 2:
            resultado += f"({n1}, {n2})"
            resultado += ", "
        lista_primos.pop(0)
        lista_primos.pop(0)
    except:

        print("El resultado es:", resultado)
        break

