#/*
# * Crea una función que reciba dos parámetros para crear una cuenta atrás.
# * - El primero, representa el número en el que comienza la cuenta.
# * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
# * - Sólo se aceptan números enteros positivos.
# * - El programa finaliza al llegar a cero.
# * - Debes imprimir cada número de la cuenta atrás.
# */

def reg(orig, secs):
    if check(orig,secs):
        print(orig)
        while orig > 0:
            print(orig - secs)
            orig -= secs
    else:
        print("solo números positivos please")

def check(uno, dos):
    if uno < 0 or dos < 0:
        return False
    else:
        return True

a = int(input("comenzamos en? "))
b = int(input("cada cuanto? "))

reg(a,b)