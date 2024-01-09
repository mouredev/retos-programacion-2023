# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */


import random
import string

print("*"*40)
print("Bienvenido al generador de contraseñas")
print("*"*40)


def respuesta_valida_sn(pregunta):
    print("Por favor, responde con 's' para Sí y 'n' para No.")
    while True:
        respuesta = input(pregunta).lower()
        if respuesta =="s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("La respuesta debe ser 's' o 'n")

def generar_letra(tipo):
    letra_aleatoria = random.choice(tipo)
    lista_password.append(letra_aleatoria)


while True:
    print("Elige los siguientes parámetros")
    print("-"*40)
    longitud = input("¿Entre 8 y 16, qué longitud quieres que tenga la contraseña? Escribe un número del 8 al 16 \n")
    if longitud.isnumeric() == False:
        print("Debes introducir un número")
        continue
    elif int(longitud) not in range(8, 16):
        print("Debes introducir un número entre el 8 y el 16")
        continue

    mayus = respuesta_valida_sn("¿Quieres que tenga mayúsculas? ")
    numeros = respuesta_valida_sn("¿Quieres que tenga números? ")
    simbolos = respuesta_valida_sn("¿Quieres que tenga simbolos?")
    
    lista_password = []

    tipo_letras = string.ascii_letters if mayus else string.ascii_lowercase
    if numeros:
        tipo_letras += string.digits
    if simbolos:
        tipo_letras += string.punctuation

    for n in range(int(longitud)):
        generar_letra(tipo_letras)
    password = ''.join(lista_password)
    print("-"*40)
    print(f"Tu contraseña generada es: {password} ")
    print(f"longitud = {longitud} | mayus = {mayus} | numeros = {numeros} | simbolos = {simbolos}")
    print("-"*40)
    break
