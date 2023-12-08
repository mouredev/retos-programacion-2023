
def primo(n1):
    contador = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            contador += 1
    if contador == 2:
        return "es primo"
    else:
        return "no es primo"

def fibonacci(n3):
    fibo = [0]
    n1 = 0
    n2 = 1
    for i in range(n3):
        agrega = n1 + n2
        fibo.append(agrega)
        n1 = n2
        n2 = agrega
        if n2 > n3:
            break
    if n3 in fibo:
        return "es fibonacci"
    else:
        return "no es fibonacci"

def impar(n4):
    if n4 % 2 == 0:
        return "es par"
    else:
        return "no es par"

while True:
    try:
        ingreso = int(input("Ingrese el Número: "))
        break
    except ValueError:
        print("\n Sólo se admite un valor numérico, vuelva a intentarlo.\n")

print (f"{ingreso} {primo(ingreso)}, {fibonacci(ingreso)} y {impar(ingreso)}")