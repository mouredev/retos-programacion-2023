
import random
from typing import Text

ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
        'x', 'y', 'z', '!','"', '#', '$', '%', '&', "'", '(', 
        ')', '*', '+' , '-', '.', '/', ':', ';', '<', '=', '>', 
        '?', '@', ',', "]", '^', '_', "{", "|", "}", "~", ")" ]


def choice_between_values(list):
    return random.choice(list)

def build_list_choice(capital_letters: bool, numbers:bool, symbols:bool):
    types_caracter = ['letter']
    if capital_letters:
        types_caracter.append('capital')
    if numbers:
         types_caracter.append('number')
    if symbols:
         types_caracter.append('symbol')
    return types_caracter
    


def build_password(longitud: int, capital_letters: bool, numbers:bool, symbols:bool) -> Text:
    list_letter = ''
    list_choice = build_list_choice(capital_letters, numbers, symbols)
    if longitud > 7 and longitud < 17:

        for i in range(longitud):
            choice_caracter = choice_between_values(list_choice)
            if choice_caracter == 'letter':
                list_letter += random.choice(ABC[:25])
            
            if choice_caracter == 'number':
                list_letter += str(random.choice(list(range(0,10))))

            if choice_caracter == 'symbol':
                list_letter += random.choice(ABC[25:55])

            if choice_caracter == 'capital':
                list_letter += random.choice(ABC[:25]).upper()
        
        return list_letter
    else: 
        return 'La longitud debe ser entre 8 y 16 caracteres'


password = build_password(8, True, True, True)

print(f'La nueva contraseña es: {password}')
