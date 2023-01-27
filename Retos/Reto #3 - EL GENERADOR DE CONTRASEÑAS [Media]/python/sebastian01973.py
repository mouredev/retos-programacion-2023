"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
import string

length = input("Longitud de la contraseña [8-16]:")
mayus = input("Incluir Mayusculas (S/N):")
numbers = input("Incluir Números (S/N):")
simbols = input("Incluir Simbolos (S/N):")

def validations(length,mayus,numbers,simbols):
    combinations = list(string.ascii_lowercase)
    if str(mayus).upper() == 'S':
        [combinations.append(str(c)) for c in list(string.ascii_uppercase)]
    if str(numbers).upper() == 'S':
        [combinations.append(str(c)) for c in list(string.digits)]
    if str(simbols).upper() == 'S':
        [combinations.append(str(c)) for c in list(string.punctuation)]
    return generate(combinations, length)


def generate(combinations, lenght):
    password = ""
    for i in range(0,int(length)):
        password += str(random.choice(combinations))
    return password
        
        
        
# Se genera la poassword
password = validations(length,mayus,numbers,simbols)

print("Su contraseña es la siguiente:")
print(password)





