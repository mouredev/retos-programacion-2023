
leet_dictionary = {
    'a': '4',
    'b': 'I3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': '[V]',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': '12',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': 'j',
    'z': '2',
    '0': 'o',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g'}


def translate_text(text):
    text_to_translate = ""
    for letter in text:
        letter_to_check = letter.lower()
        if letter_to_check in leet_dictionary:
            character = leet_dictionary[letter_to_check]
        else:
            character = letter

        text_to_translate += character

    return text_to_translate


print(translate_text(input('Type what you want to convert to leet ;) => ')))