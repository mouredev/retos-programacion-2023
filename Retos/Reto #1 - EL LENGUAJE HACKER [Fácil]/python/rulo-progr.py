def lenguajeHacker(text):
    leet_table = {
        'A': '4',
        'B': 'I3',
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
        'M': '/\/\ ',
        'N': '^/',
        'O': '0',
        'P': '|*',
        'R': 'I2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': '\/',
        'W': '\/\/',
        'X': '><',
        'J': 'j',
        'Z': '2',
    }

    leet_text = ''

    for char in text:
        if char in leet_table:
            leet_text += leet_table[char]
        else:
            leet_text += char

    return leet_text

input_text = input("Introduce un texto para traducir:  ")
leet_text = lenguajeHacker(input_text.upper())
print(leet_text)  