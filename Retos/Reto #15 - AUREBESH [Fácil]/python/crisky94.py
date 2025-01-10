
#  * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
#  * Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *  
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!
#  */

def transformarStarWars(texto):
    diccionario = {
        'a': 'aurek',
        'b': 'besh',
        'c': 'cresh',
        'd': 'dorn',
        'e': 'esh',
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
        't': 'thorn',
        'u': 'usk',
        'v': 'vev',
        'w': 'wesk',
        'x': 'xesh',
        'y': 'yirt',
        'z': 'zerek',
    }
    

    inverso_diccionario = {v: k for k, v in diccionario.items()}
    
    es_aurebesh = all(palabra in inverso_diccionario for palabra in texto.split())
    
    if es_aurebesh:
        palabras = texto.split()
        traducido = ''.join(inverso_diccionario[palabra] for palabra in palabras)
    else:
        traducido = ' '.join(diccionario[letra] if letra in diccionario else letra for letra in texto.lower())
    
    return traducido

print(transformarStarWars("hola"))      
print(transformarStarWars("herf osk leth aurek"))
