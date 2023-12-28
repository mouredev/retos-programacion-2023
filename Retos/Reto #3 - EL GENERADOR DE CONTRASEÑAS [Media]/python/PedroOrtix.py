import numpy as np

ABECEDARIO =  "abcdefghijklmnopqrstuvwxyz"
ABECEDARIO_MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMEROS = "0123456789"
SIMBOLOS = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def generacion_contra(longitud: int, mayuscula: bool, numeros: bool, simbolos: bool) -> str:
    conjunto = ABECEDARIO
    if mayuscula:
        conjunto = conjunto + ABECEDARIO_MAYUSCULAS
    if numeros:
        conjunto = conjunto + NUMEROS
    if simbolos:
        conjunto = conjunto + SIMBOLOS
    contra = ""
    for _ in range(longitud):
        contra = contra + np.random.choice(list(conjunto))  
    return contra


def main():
    longitud = int(input("Introduce la longitud de la contraseña (8/16): "))
    assert longitud == 8 or longitud == 16, "Solo se aceptan 8 o 16"

    pre_mayus = str(input("Mayusculas y/n: "))
    assert pre_mayus == 'y' or pre_mayus == 'n', "Solo se aceptan y/n"
    mayuscula = False
    if pre_mayus == "y":
        mayuscula = True

    pre_num = str(input("Numeros y/n: "))
    assert pre_num == 'y' or pre_num == 'n', "Solo se aceptan y/n"
    numeros = False
    if pre_num == "y":
        numeros = True

    pre_simb = str(input("Simbolos y/n: "))
    assert pre_simb == 'y' or pre_simb == 'n', "Solo se aceptan y/n"
    simbolos = False
    if pre_simb == "y":
        simbolos = True

    print("Tu contraseña es: ")
    print(generacion_contra(longitud, mayuscula, numeros, simbolos))

if __name__ == '__main__':
    main()

