#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)


from random import choice


def generatePassword(uppercases, numbers, symbols, len):
    if (len >= 8 and len <= 16):
        password = ''
        characters = "abcdefghijklmnopqrstuvwxyz"
        characters += ("ABCDEFGHIJKLMNOPQRSTUVWXYZ" if uppercases else '') + \
            ('0123456789' if numbers else '') + \
            ("!@#$%&*()_+" if symbols else '')

    for i in range(len):
        password += (choice(characters))

    return password


# print(generatePassword(True, True, False, 10))
