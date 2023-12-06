# Escribe un programa en python que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

import string, random

def set_numbers_characteres(expression_input_numbers_characters):
    while True:
        number_characters = input(expression_input_numbers_characters)
        try:
            number_characters = int(number_characters)
            if int(number_characters) and number_characters > 7 and number_characters < 17:
                print('>>> OK! \n')
                return number_characters
            else:
                print('>>> ERROR! Only accept numbers from 8 to 16.\n')
        except:
            print('>>> ERROR! Only accept numbers from 8 to 16.\n')

def check_yes_or_not(expression_input):
    while True: 
        value_input = input(expression_input).lower()

        if value_input != 'yes' and value_input != 'no':
            print('>>> ERROR! Only accept "yes" or "no".\n')
        
        else:
            print('>>> OK! \n')
            if value_input == 'yes':
                return True
            else:
                return False

def setup_password():
    print('\n>>> Choose the options:')
    print('>>> To exit press ctrl+c\n')

    num_characters = set_numbers_characteres('>>> 1 - Number of characters? (min 8 // max 16)\n')
    capital_letters = check_yes_or_not('>>> 2 - Include CAPITAL LETTERS? (yes/no)\n')
    numbers = check_yes_or_not('>>> 3 - Include NUMBERS? (yes/no)\n')
    symbols = check_yes_or_not('>>> 4 - Include SYMBOLS? (yes/no)\n')
    
    character_set = string.ascii_lowercase + 'ñ'

    if capital_letters:
        character_set = string.ascii_letters + 'Ññ'
    
    if numbers:
        character_set += string.digits

    if symbols:
        character_set += string.punctuation
    
    password = ''.join(random.choices(character_set, k=num_characters))

    return password

password = setup_password()

print(password)
print(len(password))