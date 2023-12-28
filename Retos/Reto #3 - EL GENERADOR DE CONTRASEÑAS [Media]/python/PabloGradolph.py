'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''

import string, random

def pasword_generator(length: int, uppercase: bool, numbers: bool, symbols: bool) -> str:

    # Definimos los números, letras y signos que podemos tener en la contraseña.
    if uppercase: letters = string.ascii_letters 
    else: letters = string.ascii_lowercase

    if numbers: letters += string.digits 
    if symbols: letters += string.punctuation
    
    # Generamos la contraseña
    pasword = ""
    for _ in range(0, length):
        pasword += random.choice(letters)

    return pasword

def main():

    # Pedimos las características de la contraseña con control de errores.
    length = int(input("Introduzca la longitud deseada de la contraseña: "))
    while length < 8 or length > 16:
        print("La longitud de la contraseña debe estar entre 8 y 16")
        length = int(input("Introduzca de nuevo la longitud de la contraseña: "))

    upper_letters = input("¿Puede tener letras mayúsculas? Y/N: ")
    while upper_letters != "Y" and upper_letters != "N":
        print("Por favor introduzca Y o N (Yes or No)")
        upper_letters = input("¿Puede tener letras mayúsculas? Y/N: ")
    if upper_letters == "Y": upper_letters = True
    else: upper_letters = False

    numbers = input("¿Puede tener números? Y/N: ")
    while numbers != "Y" and numbers != "N":
        print("Por favor introduzca Y o N (Yes or No)")
        numbers = input("¿Puede tener números? Y/N: ")
    if numbers == "Y": numbers = True
    else: numbers = False

    symbols = input("¿Puede tener símbolos? Y/N: ")
    while symbols != "Y" and symbols != "N":
        print("Por favor introduzca Y o N (Yes or No)")
        symbols = input("¿Puede tener símbolos? Y/N: ")
    if symbols == "Y": symbols = True
    else: symbols = False
    
    print(f"Su contraseña es: {pasword_generator(length, upper_letters, numbers, symbols)}")

if __name__ == "__main__":
    main()

