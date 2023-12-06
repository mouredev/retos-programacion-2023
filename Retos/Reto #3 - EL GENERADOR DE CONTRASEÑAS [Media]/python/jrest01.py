import string
import random

# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

LOWER = list(string.ascii_lowercase)
UPPER = list(string.ascii_uppercase)
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SIMBOLS = ['*', '/', '-', '+', ':', ';', ',', '.']
CHARS = list(LOWER + UPPER + NUMBERS + SIMBOLS)

def password_generator():
    password = ''
    length = random.randint(8, 17)
    for i in range(length):
        char = CHARS[random.randint(0,len(CHARS)-1)]
        password += char
    return password


if __name__ == '__main__':
    print('Su contraseña es: '+password_generator())