def Transformar(texto):

    texto_final = ''
    texto_lower = texto.lower()

    diccionario = {
        'a': '4',  'b': 'I3',
        'c': '[',  'd': ')',
        'e': '3',  'f': '|=',
        'g': '&',  'h': '#',
        'i': '1',  'j': ',_|',
        'k': '>|', 'l': '1',
        'm': '/\/\\', 'n': '^/',
        'o': '0',  'p': '|*',
        'q': '(_,)', 'r': 'I2',
        's': '5',  't': '7',
        'u': '(_)', 'v': '\/',
        'w': '\/\/', 'x': '><',
        'y': 'j',  'z': '2',
        '1': 'L',  '2': 'R',
        '3': 'E',  '4': 'A',
        '5': 'S',  '6': 'b',
        '7': 'T',  '8': 'B',
        '9': 'g',  '0': 'o',
        ' ': ' '
    }

    for letra in texto_lower:
        texto_final = texto_final + diccionario[letra]

    print(texto_final)


Transformar("Hola Mundo")