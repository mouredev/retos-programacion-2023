def transfor_laguage(text, idioma):

    language = {
            'a': 'aurek',   'b': 'besh',    'c': 'cresh',
            'd': 'dorn',    'e': 'esk',     'f': 'forn',
            'g': 'grek',    'h': 'herf',    'i': 'isk',
            'j': 'jenth',   'k': 'krill',  'l': 'leth',
            'm': 'mern',    'n': 'nern',    'o': 'osk',
            'p': 'peth',    'q': 'qek',     'r': 'resh',
            's': 'senth',   't': 'trill',   'u': 'usk',
            'v': 'vev',     'w': 'wesk',    'x': 'xesh',
            'y': 'yirt',    'z': 'zerek'
    }
    frase = ''
    if idioma == 'español':
        for p in range(len(text)):
            if text[p] in language:
                frase += f'{language[text[p]]} '
        print('Lenguaje Aurebesh: ',frase)
    
    else:
        list = text.split()
        for p in list:
            for key, value in language.items():
                if p == value:
                    frase += f'{key} '
        print('Lenguaje Español: ',frase)


selection_language = {
    1 : 'español',
    2 : 'aurebesh'
}

print('Bienvenido al traductor')
print('[1].- Presiona para Español - Aurebesh')
print('[2].- Presiona para Aurebesh - Español')
option = int(input('OPCIÓN: '))

if option in selection_language:
    text = str(input('Ingresa el texto: ')).lower()
    transfor_laguage(text, selection_language[option])

else:
    print('Error opción invalida')