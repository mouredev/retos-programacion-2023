'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''

import random

# Getting all the cahracters for use
character_set = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbols = ["|", "!", "\"", "#", "$", "%", "&", "/", "(", ")", "=", "?", "'", "\\", "+", "-", "*", "{", "}", "[", "]", ";", ":", "_", "^"]

# Function to determine the size of the password, keeping the restrictions in check
def check_lenght(password_length: int):
    if (password_length < 8):
        return 8
    elif (password_length > 16):
        return 16
    return password_length

# Asking the user for the selected information
pass_length = int(input("Ingresar la longuitud: "))
has_mayus = input("Tiene mayusculas?(y/n) ")
has_numbers = input("Tiene números?(y/n) ")
has_simbols = input("tiene símbolos?(y/n) ")
# Cheking the different flags for character use
if has_mayus == "y":
    character_set += mayus
if has_numbers == "y":
    character_set += numbers
if has_simbols == "y":
    character_set += simbols
pass_lenght = check_lenght(pass_length);
password = ""
for i in range(pass_lenght):
    # Looping through to obtain the password
    password += random.choice(character_set)
print(password)