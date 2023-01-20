#
#  Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  Podrás configurar generar contraseñas con los siguientes parámetros:
#  - Longitud: Entre 8 y 16.
#  - Con o sin letras mayúsculas.
#  - Con o sin números.
#  - Con o sin símbolos.
#  (Pudiendo combinar todos estos parámetros entre ellos)
#

import string
import random

while True:
    pwd_length = input("Enter the desired password length (8 to 16): ")
    if pwd_length not in ('8','9','10','11','12','13','14','15','16'):
        print("Not an appropriate choice.")
    else:
        break

pwd_length = int(pwd_length)

while True:
    upper_yn = input("Would you like the password to have uppercase letters? (Y/N): ").upper()
    if upper_yn not in ('Y', 'N'):
        print("Not an appropriate choice.")
    else:
        break

while True:
    number_yn = input("Would you like the password to have numbers? (Y/N): ").upper()
    if number_yn not in ('Y', 'N'):
        print("Not an appropriate choice.")
    else:
        break

while True:
    special_char_yn = input("Would you like the password to have special characters? (Y/N): ").upper()
    if special_char_yn not in ('Y', 'N'):
        print("Not an appropriate choice.")
    else:
        break

def randomPasswordGenerator(pwd_length, upper_yn, number_yn, special_char_yn):
    all_characters = string.ascii_lowercase
    
    if upper_yn == "Y":
        all_characters += string.ascii_uppercase
    if number_yn == "Y":
        all_characters += string.digits
    if special_char_yn == "Y":
        all_characters += string.punctuation

    password = "".join(random.sample(all_characters, pwd_length))
    return password

print(randomPasswordGenerator(pwd_length, upper_yn, number_yn, special_char_yn))