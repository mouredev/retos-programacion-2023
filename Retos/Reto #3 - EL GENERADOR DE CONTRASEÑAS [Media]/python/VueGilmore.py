'''
Reto #3: EL GENERADOR DE CONTRASEÑAS

Dificultad: MEDIA

Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
'''
import string, random

def generate_password(digits: int, letters: bool, numbers: bool, symbols: bool):
    options = list(string.ascii_lowercase)
    letters_options = list(string.ascii_uppercase)
    numbers_options = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    symbols_options = ('¿', '?', '¡', '!', ',', '.', ';', '*', '/', '-', '+', '(', ')', '[', ']', '{', '}')
    
    # Create the full options depending on the users choices
    if letters:
        options.extend(letters_options)
    if numbers:
        options.extend(numbers_options)
    if symbols:
        options.extend(symbols_options)

    # Generate the password
    password = ''
    for i in range(0, digits):
        randomInt = int(random.randint(0,len(options) - 1))
        randomDigit = options[randomInt]
        password = password + randomDigit

    return password


def start_program():
    digits = 0
    letters = False
    numbers = False
    symbols = False

    # Choose digits
    while digits < 8 or digits > 16:
        answer_digits = input('¿Cuántos dígitos debe tener la contraseña? (Número entre 8 y 16): ')

        try:
            digits = int(answer_digits)
        except:
            digits = 0

    # Choose uppercase
    answer_letters = input('¿Incluye letras mayúsculas? (s/n): ')
    if answer_letters == 's':
        letters = True
    elif not answer_letters == 'n':
        print('No se incluirán mayúsculas')
    

    # Choose numbers
    answer_numbers = input('¿Incluye números? (s/n): ')
    if answer_numbers == 's':
        numbers = True
    elif not answer_numbers == 'n':
        print('No se incluirán números')
    
    # Choose symbols
    answer_symbols = input('¿Incluye símbolos? (s/n): ')
    if answer_symbols == 's':
        symbols = True
    elif not answer_symbols == 'n':
        print('No se incluirán simbolos')

    generated_password = generate_password(digits, letters, numbers, symbols)
    print(generated_password)
    
start_program()