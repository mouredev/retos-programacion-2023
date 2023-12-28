# 
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
# 
import random

def passwordGenerator(lenght = 16, capital = True, numbers = True, symbols = True):
    #Create string
    password = ''
    #Check password input lenght
    if(lenght < 8):
        print('Minimum password lenght is 8 characters.')
        lenght = 8
    if(lenght > 16):
        print('Maximum password lenght is 16 characters.')
        lenght = 8
    #Element sin the password lists creation
    symbols_list = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '=', '!', '?', '^', '_', '~']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #Create list to contain needed list
    chars = []
    chars += alphabet
    #Add list to main list
    if(capital): chars += alphabet_caps
    if(numbers): chars += numbers_list
    if(symbols): chars += symbols_list
    #Generate password
    for index in range(0, lenght):
        password += random.choice(chars)
    return password

def main():
    print(passwordGenerator(10, False, False, False))
    print(passwordGenerator(16, False, False, True))
    print(passwordGenerator(16, False, True, True))
    print(passwordGenerator(16, True, True, True))

main()