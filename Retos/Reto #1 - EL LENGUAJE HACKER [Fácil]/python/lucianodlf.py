#!/usr/bin/env python
""" Resolver of weekly challenge 1 from https://github.com/lucianodlf/retos-programacion-2023 """

dictorionary_parse = {
    'A': '4',
    'B': 'IB',
    'C': '[',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '/\\/\\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '\\/',
    'W': '\\/\\/',
    'X': '><',
    'Y': 'j',
    'Z': '2',
    '0': 'o',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
}


def common_text_to_leet(text):
    """ Convert common text to leet dictionarie """
    result = ''
    for char in text:
        if char.isalnum() and char.upper() in dictorionary_parse:
            result += dictorionary_parse[char.upper()]
        else:
            result += char
    return result


def main():
    print(common_text_to_leet('hola Esto es 1 prueba 1234'))
    print(common_text_to_leet('Ésto es ótra prueba con pingüin´o'))


if __name__ == '__main__':
    main()
