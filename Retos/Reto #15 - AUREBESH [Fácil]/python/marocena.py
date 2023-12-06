spa_aur_dict = {
                'a': 'aurek',
                'b': 'besh',
                'c': 'cresh',
                'd': 'dorn',
                'w': 'wesk', # Si se coloca después de 'e' puede dar lugar a errores en la traduccion aure > spa
                'e': 'esk',
                'f': 'forn',
                'g': 'grek',
                'h': 'herf',
                'i': 'isk',
                'j': 'jenth',
                'k': 'krill',
                'l': 'leth',
                'm': 'mern',
                'n': 'nern',
                'o': 'osk',
                'p': 'peth',
                'q': 'qek',
                'r': 'resh',
                's': 'senth',
                't': 'trill',
                'u': 'usk',
                'v': 'vev',
                'x': 'xesh',
                'y': 'yirt',
                'z': 'zerek',
                'ch': 'cherek',
                'ae': 'enth',
                'eo': 'onith',
                'kh': 'krenth',
                'ng': 'nen',
                'oo': 'orenth',
                'sh': 'shen',
                'th': 'thesh',
                }

def spanish_to_aurebesh(text, reverse = False):
    if reverse == True:
        for key, value in spa_aur_dict.items():
            text = text.replace(value, key)
        
        return text
    else:
        resul = ''
        i = 0
        while i < text.__len__():
            char = ''
            char_seq = ''

            char = text[i].lower()
            if (i + 1) < text.__len__():
                char_seq = (text[i] + text[i+1]).lower()

            if char_seq in spa_aur_dict:
                resul += spa_aur_dict[char_seq]
                i += 1
            else:
                if (not char.isspace()) and (char in spa_aur_dict):
                    resul += spa_aur_dict[char]
                elif char.isspace():
                    resul += ' '
                else:
                    resul += char
            
            i += 1
        
        return resul

text = 'Hola, Mundo!'
print(spanish_to_aurebesh(text))

text = 'herfosklethaurek, mernusknerndornosk!'
print(spanish_to_aurebesh(text, reverse=True))