import random

uppercase_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_list = "abcdefghijklmnopqrstuvwxyz"
numbers_list = "0123456789"
special_characters_list = "!@#$%^&*()?"

yes_choices = ['SI', 'S', 'YES', 'Y']
no_choices = ['NO', 'N']

# === Funcion que genera la contraseña con los parametros indicados ===
def generate_password(size, valid_size, capital, lower, number):

    if valid_size:
        if not (size >= 8 and size <= 16):
            print("La longitud no cumple el parámetro de longitud recomendada.")
            return ""

    password = ""
    character_list = ""

    character_list += special_characters_list
    character_list += uppercase_list if capital else ""
    character_list += lowercase_list if lower else ""
    character_list += numbers_list if number else ""

    for i in range(length):
        random_character = random.choice(character_list)
        password += random_character
    return password

# Valida respuestas Si/No
def get_yes_or_no(question):
    while True:
        answer = input(question)

        if answer.upper() in yes_choices:
            return True
        elif answer.upper() in no_choices:
            return False
        else:
            print("Debes escribir Si o No.")
            continue

# Valida longitud
def get_number(question):
    while True:
        try:
            length = int(input(question))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if length < 0:
            print("Debes escribir un número positivo.")
            continue
        else:
            return length

# === Ingreso de datos ===
length = get_number("Ingrese la longitud de la contraseña: ")
valid_length = get_yes_or_no("Validar la longitud Si/No: ")
include_capitals = get_yes_or_no("Incluir mayúsculas Si/No: ")
include_lowercase = get_yes_or_no("Incluir minúsculas Si/No: ")
include_numbers = get_yes_or_no("Incluir números Si/No: ")

# Genera la contaseña
generated_password = generate_password(int(length),
                                       valid_length,
                                       include_capitals,
                                       include_lowercase,
                                       include_numbers)

print("La contraseña generada es:", generated_password)
