def tabla_multiplicar(numero):
    multiplicacion = []
    for i in range(1,11):
        multiplicacion.append(numero * i)
    return multiplicacion

def imprimir(multiplicacion, numero):
    for i in range(len(multiplicacion)):
        print(numero, "x", (i + 1) ,"=",multiplicacion[i])


numero = int(input("Ingresa un numero: "))
multiplicacion = tabla_multiplicar(numero)
imprimir(multiplicacion, numero)
