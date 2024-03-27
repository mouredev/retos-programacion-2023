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

def password_generate(long, upper, numbers, symbols):

    counter = 0
    password = ""
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowwer_chars = "abcdefghijklmnopqrstuvwxyz"
    numbers_chars = "0123456789"
    symbols_chars = "!%&/*+-@#$?¿"
    final_string = lowwer_chars

    if upper:
        final_string += upper_chars
    if numbers:
        final_string += numbers_chars
    if symbols:
        final_string += symbols_chars

    for char in final_string:
        if counter != long:
            random_char = random.choice(final_string)
            password += random_char
            counter += 1

    return password


how_long = input ("Introduce la lungitud de la contraseña (Entre 8 y 16): ")

try:
    long = int(how_long)

    if long < 17 and long > 7:

        is_upper = input("Mayúsculas Y(Si)/N(No): ").upper() == "Y" 
        is_numbers = input("Números Y(Si)/N(No): ").upper() == "Y" 
        is_symbols = input("Símbolos Y(Si)/N(No): ").upper() == "Y" 
        print("La contraseña es: ", password_generate(long, is_upper, is_numbers, is_symbols))

    else:
        print("La longitud debe ser de 8 a 16 caracteres.")

except:
    print("El valor", how_long, " no es válido.")