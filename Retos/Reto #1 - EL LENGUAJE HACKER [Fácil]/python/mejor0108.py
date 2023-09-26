
#/*
#```
# * Escribe un programa que reciba un texto y transforme lenguaje natural a
# * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# *  se caracteriza por sustituir caracteres alfanuméricos.
# * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# *   con el alfabeto y los números en "leet".
# *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
# */
#```

diccionario = {
    'a' : '4',      'b' : '13',     'c' : '[',      'd' : ')',      'e' : '3',
    'f' : '|=',     'g' : '&',      'h' : '#',      'i' : '1',      'j' : ',_|',
    'k' : '>|',     'l' : '1',      'm' : '/\\/\\', 'n' : '^/',    'o' : '0',
    'p' : '|*',     'q' : '(_,)',   'r' : '|2',     's' : '5',      't' : '7',
    'u' : '(_)',    'v' : '\\/',    'w' : '\\/\\/', 'x' : '><',     'y' : 'j',
    'z' : '2',
    '1' : 'L',      '2' : 'R',      '3' : 'E',      '4' : 'A',      '5' : 'S',
    '6' : 'b',      '7' : 'T',      '8' : 'B',      '9' : 'g',      '0' : 'o'
    
               }


        
        
def conversion_hacker(texto: str) -> str:
    try: 
        return diccionario[texto.lower()]
    except KeyError:
        return texto
        
if __name__ == '__main__':
    texto = '''Required. A sequence, collection or an iterator object. 
        You can send as many iterables as you like, 
        just make sure the function has one parameter for each iterable.'''
    x = "".join(list(map(conversion_hacker,texto)))
    print(x)