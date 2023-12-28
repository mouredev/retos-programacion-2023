"""
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
"""

DICTIONARY_AUREBESH = {
    'a': 'aurek',
    'b': 'besh',
    'c': 'cresh',
    'd': 'dorn',
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
    'w': 'wesk',
    'x': 'xesh',
    'y': 'yirt',
    'z': 'zerek'
}

DOUBLE_AUREBESH = {
    'ch': 'cherek',
    'ae': 'enth',
    'eo': 'onith',
    'kh': 'krenth',
    'ng': 'nen',
    'oo': 'orenth',
    'sh': 'sen',
    'th': 'thesh'
}


def translateAurebesh(text):
    text = text.lower()
    result = ""

    idx = 0
    while (idx < len(text)):
        if idx != (len(text) - 1) and (text[idx] + text[idx + 1]) in DOUBLE_AUREBESH.keys():
            result += DOUBLE_AUREBESH[text[idx] + text[idx + 1]]
            idx += 1
        elif (text[idx]) in DICTIONARY_AUREBESH.keys():
            result += DICTIONARY_AUREBESH[text[idx]]
        else:
            result += text[idx]

        idx += 1

    return result


print(translateAurebesh('Hola mundo!'))

print(translateAurebesh('Larga vida y prosperidad.'))
