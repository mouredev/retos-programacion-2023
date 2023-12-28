#Reto #3: EL GENERADOR DE CONTRASEÑAS

"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
from random import choice, shuffle

lower_case_letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capitalize_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbols_list = ["!","#","$","%","&"]


def generate_password(lenght: int, mayus: str, number: str, simbol: str) -> str:
    characters = lower_case_letters_list
    password = []

    if mayus == "y":
        password.append(choice(capitalize_letters_list))
        characters += capitalize_letters_list
    if number == "y":
        password.append(choice(numbers_list))
        characters += numbers_list
    if simbol == "y":
        password.append(choice(simbols_list))
        characters += simbols_list
   
    shuffle(characters)
   
    while len(password) < lenght:
        password.append(choice(characters))

    return ''.join(password)

if __name__ == "__main__":
    lenght = 0
    mayus = ""
    numbers = ""
    simbols = ""
    while lenght < 8 or lenght > 16:
        lenght = int(input("Ingrese la cantidad de caracteres entre 8 y 16: "))
    while mayus.lower() not in ("y","n"):
        mayus = input("Incluir letras mayusculas (y/n):").lower()
    while numbers.lower() not in ("y","n"):
        numbers = input("Incluir numeros (y/n): ").lower()
    while simbols.lower() not in ("y","n"):
        simbols = input("Incluir simbolos (y/n):").lower()
    print(generate_password(lenght, mayus, numbers, simbols))
