# Reto 03: El generador de contraseñas
# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
import random, string

def create_password(passwordlength, withuppercase, withnumbers, withsymbols):
    password = ""
    length = 8 if passwordlength < 8 else 16 if passwordlength > 16 else passwordlength

    characters = string.ascii_lowercase
    for i in range(length):
        if withuppercase:
            characters = string.ascii_letters
        if withnumbers:
            characters += string.digits
        if withsymbols:
            characters += string.punctuation

        password += random.choice(characters)
    return password

print(create_password(4, True, True, True))
print(create_password(8, True, False, True))
print(create_password(16, True, True, False))
print(create_password(25, False, True, True))
print(create_password(25, False, False, False))




