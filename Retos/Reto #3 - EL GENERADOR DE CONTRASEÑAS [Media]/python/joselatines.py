import random

""" /*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */ """

def create_password(length=8, uppers=False, numbers=False, symbols=False):
    password = ''
    current_length = 16 if length > 8 else 8

    characters_numbers = []

    # Alphabet
    for i in range(97, 123): 
        characters_numbers.append(i)

    if numbers:
      for i in range(48, 58): 
        characters_numbers.append(i)

    if symbols:
      # some symbols
      for i in range(33, 48):
        characters_numbers.append(i)

      # more symbols
      for i in range(58, 65):
        characters_numbers.append(i)

      # more symbols
      for i in range(91, 97):
        characters_numbers.append(i)

      # more symbols
      for i in range(123, 126):
        characters_numbers.append(i)

    random.shuffle(characters_numbers)

    for character in characters_numbers:
      if len(password) < current_length:
        password += str(chr(character))

    password = password.upper() if uppers else password

    return password


print('Your password is: ', create_password())
