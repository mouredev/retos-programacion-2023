aurebesh_to_spanish = {
    'aurek': 'a',
    'besh': 'b',
    'cresh': 'c',
    'cherek': 'ch',
    'dorn': 'd',
    'esk': 'e',
    'enth': 'ae',
    'onith': 'eo',
    'forn': 'f',
    'grek': 'g',
    'herf': 'h',
    'isk': 'i',
    'jenth': 'j',
    'krill': 'k',
    'krenth': 'kh',
    'leth': 'l',
    'mern': 'm',
    'nern': 'n',
    'nen': 'ng',
    'osk': 'o',
    'orenth': 'oo',
    'peth': 'p',
    'qek': 'q',
    'resh': 'r',
    'senth': 's',
    'shen': 'sh',
    'trill': 't',
    'thesh': 'th',
    'usk': 'u',
    'vev': 'v',
    'wesk': 'w',
    'xesh': 'x',
    'yirt': 'y',
    'zerek': 'z',
}

spanish_to_aurebesh = {value: key for key, value in aurebesh_to_spanish.items()}

def translate(text, direction):
    if direction == '1':
        mapping = spanish_to_aurebesh
    elif direction == '2':
        mapping = aurebesh_to_spanish
    else:
        print('Invalid option')
        return None
    
    translation = []
    for char in text.lower():
        if char == ' ':
            translation.append(' ')
        elif char in mapping:
            translation.append(mapping[char])
        else:
           print(f'Cannot translate character "{char}"')
           return None
    
    return ''.join(translation)


def main():
    while True:
        print('Que transformamos hoy? :D ')
        print('1 - Español a Aurebesh')
        print('2 - Aurebesh a Español')
        print('0 - Salir')
        direction = input('Ingresa tu eleccion: ')
        
        if direction == '0':
            break
        
        if direction not in ['1', '2']:
            print('Invalid option')
            continue
        
        text = input('Ingresa tu texto: ')
        translation = translate(text, direction)
        if translation:
            print('Translation:', translation)


if __name__ == '__main__':
    main()

