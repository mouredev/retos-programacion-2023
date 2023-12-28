import random

def generador(longitud, may, num, sim):
    letras = "abcdefghijklmnopqrstuvwxyz"
    numeros = "1234567890"
    simbolos = "ºª!·$%&/()=?¿¡'[]{}#~@¬/*+;:,.<>"
    contrasena = ""

    if may == "s":
        letras += letras.upper()
    if num == "s":
        letras += numeros
    if sim == "s":
        letras += simbolos

    i = 0        
    while i < longitud:
        contrasena += letras[random.randint(0, len(letras)-1)]
        i += 1
    return contrasena

def main():
    longitud = None
    while longitud not in range(8,17):
        longitud = int(input("Selecciona la longitud de la contraseña (8 a 16): "))

    mayusculas = None
    while mayusculas not in ["s","n"]:
        mayusculas = input("¿La contraseña debe contener mayúsculas? (s/n): ")

    numeros = None
    while numeros not in ["s","n"]:
        numeros = input("¿La contraseña debe contener números? (s/n): ")

    simbolos = None
    while simbolos not in ["s","n"]:
        simbolos = input("¿La contraseña debe contener símbolos? (s/n): ")
        
    print("Tu contraseña es: " + generador(longitud, mayusculas, numeros, simbolos))

main()