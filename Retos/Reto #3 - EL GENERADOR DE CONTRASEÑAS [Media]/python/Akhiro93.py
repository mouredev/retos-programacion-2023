import random

try:
    tamaño_de_contraseña = int(input("tamaño de contraseña: ") - 1)
    if tamaño_de_contraseña > 15:
        tamaño_de_contraseña = 15
except:
    tamaño_de_contraseña = 8


def generador_de_contraseña(number):
    letras = "qwertyuiopasdfghjklñzxcvbnm"
    letras_mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    numeros = "1234567890"
    caracteres = "!#$%&/()=,.-_+*;:"
    contraseña = ""
    i = 0
    while i < number:
        q = random.randint(1, 4)
        if q == 1:
            n = random.randint(0, 26)
            contraseña += letras[n]
        if q == 2:
            n = random.randint(0, 9)
            contraseña += numeros[n]
        if q == 3:
            n = random.randint(0, 16)
            contraseña += caracteres[n]
        if q == 4:
            n = random.randint(0, 26)
            contraseña += letras_mayusculas[n]
        i += 1
    posicion_coma = random.randint(1, len(contraseña)-1)
    contraseña = contraseña[:posicion_coma] + "," + contraseña[posicion_coma:]
    return contraseña


print(generador_de_contraseña(tamaño_de_contraseña))
