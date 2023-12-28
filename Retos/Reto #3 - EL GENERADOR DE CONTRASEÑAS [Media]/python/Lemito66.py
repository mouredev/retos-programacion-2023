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
import string
def password_generator():
    list_of_words = []
    finally_password = ''
    for i in range(0, length_of_password()):
        choose_letter = random.choice(complete_list())
        list_of_words.append(choose_letter)
    finally_password += ''.join(list_of_words)
    return finally_password
    
def length_of_password():
    length_of_number = []
    for number in range(8,17):
        length_of_number.append(number)
    return random.choice(length_of_number)



def complete_list():
    lower_case=list(string.ascii_lowercase)
    upper_case=list(string.ascii_uppercase)
    numbers=list(string.digits)
    punctuation = list(string.punctuation)
    return upper_case + lower_case+ numbers + punctuation

print(password_generator())