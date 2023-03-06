# /*
# * Crea 3 funciones, cada una encargada de detectar si una cadena de
# * texto es un heterograma, un isograma o un pangrama.
# * - Debes buscar la definición de cada uno de estos términos.
# */

import re


# /**
# * Funcion de extension de un string que limpia los acentos de una cadena de texto y
# * los sustituye por su equivalente sin acento
# */
def clean_text(text):
    accents = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    reg_exp = re.compile('[áéíóúÁÉÍÓÚ]')
    return reg_exp.sub(lambda x: accents[x.group()], text)


# /**
# * Funcion que detecta si una palabra es un heterograma con una expresion regular
# * Un Heterograma es una palabra que no tiene letras repetidas
# */
def is_heterogram(text)->bool:
    text_lower = re.sub(r'[^a-z]', '', clean_text(text.lower()))
    reg_exp = re.compile(r'^(?!.*(.).*\1)[a-zA-Z]+$')
    return bool(reg_exp.match(text_lower))


# /**
# * Funcion que detecta si una palabra es un isograma.
# * Un isograma es una palabra en la que cada letra se repite exactamente el mismo numero de veces
# * Una palabra en la que cada letra se repite una sola vez es a su vez un heterograma.
# * Un palabra en la que cada letra se repite dos veces es un isograma de grado 2 y asi sucesivamente.
# */
def is_isogram(text):
    count_letters = {}
    text_lower = re.sub(r'[^a-z]', '', clean_text(text.lower()))
    for letter in text_lower:
        count_letters[letter] = text_lower.count(letter)
    return len(set(count_letters.values())) == 1


# /**
# * Funcion que detecta si una palabra es un pangrama
# * Un Pangrama es una frase que contiene todas las letras del alfabeto
# */
def is_pangram(text):
    text_lower = re.sub(r'[^a-z]', '', clean_text(text.lower()))
    reg_exp = re.compile(r'[a-z]')
    number_of_letters = len(reg_exp.findall('abcdefghijklmnopqrstuvwxyz'))
    letters = set(reg_exp.findall(text_lower))
    return len(letters) == number_of_letters


# /**
# * Funcione que comprueba si una palabra es un isograma, pangrama o heterograma
# */
def check_word(word):
    message = f'La frase {word} es: '
    conditions = []

    if is_isogram(word):
        conditions.append('isograma')

    if is_pangram(word):
        conditions.append('pangrama')

    if is_heterogram(word):
        conditions.append('heterograma')

    if not conditions:
        message += 'ni un isograma, ni un pangrama, ni un heterograma'
    else:
        message += ', '.join(conditions) + '.'

    print(message)


# /**
# * Función principal
# */
if __name__ == '__main__':
    check_word('Ecuador, cada quince de noviembre')
    check_word('esdrújula')
    check_word('aliento')
    check_word('mama')
    check_word("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja")
    check_word("Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!")
