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


def spanish_to_aurebesh(text: str) -> str:
    response = ''
    double_aurebesh = {
        'ch': 'cherek',
        'ae': 'enth',
        'eo': 'onith',
        'kh': 'krenth',
        'ng': 'nen',
        'oo': 'orenth',
        'sh': 'shen',
        'th': 'thesh',
    }
    dictionary_aurebesh = {
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
        'z': 'zerek',
    }

    position_of_word = 0
    text_to_lower = text.lower()
    while position_of_word < len(text_to_lower):
        # Verifica si los dos caracteres que empiezan en el índice actual están en el diccionario double_aurebesh
        if position_of_word < len(text_to_lower) - 1 and text_to_lower[position_of_word:position_of_word+2] in double_aurebesh:
            response += double_aurebesh[text_to_lower[position_of_word:position_of_word+2]]
            position_of_word += 2
        # Si no, verifica si el carácter actual está en el diccionario dictionary_aurebesh y agrega su valor a la respuesta
        elif text_to_lower[position_of_word] in dictionary_aurebesh:
            response += dictionary_aurebesh[text_to_lower[position_of_word]]
            position_of_word += 1
        # Si no, agrega el carácter original a la respuesta
        else:
            response += text_to_lower[position_of_word]
            position_of_word += 1

    return response


print(spanish_to_aurebesh("Lemito66"))
