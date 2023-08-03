'''
    Traductor de castellano a aurebesh y viceversa.
    Autor (GitHub) : PhantomBCN
    Versión: 1.0
    Fecha: 12 de abril de 2023
'''
'''
    /*
    * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
    * Star Wars: el "Aurebesh".
    * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
    * - También tiene que ser capaz de traducir en sentido contrario.
    *  
    * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
    *
    * ¡Que la fuerza os acompañe!
    */
'''

# He preferido duplicar el diccionario por comodidad.
Aurebesh = {'a': 'aurek', 'b': 'besh', 'c': 'cresh', 'd': 'dorn', 'e': 'esk', 'f': 'forn', 'g': 'grek', 'h': 'herf',
            'i': 'isk', 'j': 'jenth', 'k': 'krill', 'l': 'leth', 'm': 'merm', 'n': 'nern', 'o': 'osk', 'p': 'peth',
            'q': 'qek',  'r': 'resh', 's': 'senth', 't': 'trill', 'u': 'usk', 'v': 'vev', 'w': 'wesk',
            'x': 'xesh', 'y': 'yirt', 'z': 'zerek'}

Castellano = {'aurek': 'a', 'besh': 'b',  'cresh': 'c', 'dorn': 'd',  'esk': 'e', 'forn': 'f', 'grek': 'g', 'herf': 'h',
              'isk': 'i',  'jenth': 'j',  'krill': 'k',  'leth': 'l',  'merm': 'm',  'nern': 'n',  'osk': 'o',  'peth': 'p',
              'qek': 'q',  'resh': 'r',  'senth': 's', 'trill': 't',  'usk': 'u', 'vev': 'v',  'wesk': 'w',
              'xesh': 'x', 'yirt': 'y', 'zerek': 'z'}

# Funcion que pasa de castellano a aurebesh
def castellano_aurebesh(texto_castellano):

    texto_aurebesh = ''

    for caracter in texto_castellano:
        if caracter == ' ':
            texto_aurebesh += ' '
        else:
            try:
                texto_aurebesh += Aurebesh[caracter.lower()]
            except KeyError:
                texto_aurebesh += '???'
    return (texto_aurebesh)

# Funcion que pasa de aurebesh a castellano
def aurebesh_castellano(texto_aurebesh):

    texto_castellano = ''
    token_aurebesh = ''

    for caracter in texto_aurebesh:
        if caracter == ' ':
            texto_castellano += ' '
        else:
            token_aurebesh +=caracter
            try:
                texto_castellano += Castellano[token_aurebesh.lower()]
                token_aurebesh=''
            except KeyError:
                if len(token_aurebesh)>5 :
                    texto_castellano += '?'
    if token_aurebesh != '':
        texto_castellano += '?'
    return (texto_castellano)

texto_castellano = input("Entra el texto a traducir al Aurebesh: ")
print(castellano_aurebesh(texto_castellano))
texto_aurebesh = input("Entra el texto a traducir al Castellano: ")
print(aurebesh_castellano(texto_aurebesh))
