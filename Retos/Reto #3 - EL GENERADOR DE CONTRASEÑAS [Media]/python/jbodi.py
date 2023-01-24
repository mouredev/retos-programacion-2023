import string, random
# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado

"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""

def randomPasswordGenerator(longitud, parametros):
    password = ""

    for i in range (0, longitud + 1):
        lista_a_elegir = random.choice(parametros)
        password += random.choice(lista_a_elegir)

    print(password)

simbolos = string.punctuation
letras = string.ascii_lowercase
letras_con_mayus = string.ascii_letters
numeros = string.digits

con_simbolos = input("¿Quieres que tu contraseña contenga símbolos? [S/n]")
con_mayus = input("¿Quieres que tu contraseña contenga mayúsculas? [S/n]")
con_numeros = input("¿Quieres que tu contraseña contenga números? [S/n]")

longitud_pass = random.randint(8, 16)
parametros = []

if(con_simbolos.lower() == "s"):
    parametros.append(simbolos)
    print(parametros)

if(con_mayus.lower() == "s"):
    parametros.append(letras_con_mayus)
else:
    parametros.append(letras)

if(con_numeros.lower() == "s"):
    parametros.append(numeros)

print(parametros)
randomPasswordGenerator(longitud_pass, parametros)