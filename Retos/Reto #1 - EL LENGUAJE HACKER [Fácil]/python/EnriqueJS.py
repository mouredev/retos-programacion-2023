diccionario_hacker = {
    'a': '4',
    'b': 'I3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_I',
    'k': '>|',
    'l': '1',
    'm': '[V]',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': 'j',
    'z': '2',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o',
    }

texto_traducido = ''
texto = input('Introduce un texto para transformarlo en lenguaje Hacker: ')
for i in texto.lower():
    if i in diccionario_hacker.keys():
        texto_traducido += diccionario_hacker[i]
    else:
        texto_traducido = texto_traducido + i
        
print(texto_traducido)
