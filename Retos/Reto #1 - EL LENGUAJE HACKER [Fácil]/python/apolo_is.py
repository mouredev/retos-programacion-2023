"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 """


trad_dict={
    'a':'4',
    'b':'l3',
    'c':'[',
    'd':')',
    'e':'3',
    'f':'|=',
    'g':'&',
    'h':'#',
    'i':'1',
    'j':',_|',
    'k':'>|',
    'l':'1',
    'm':'/\\/\\',
    'n':'^/',
    'o':'0',
    'p':'|*',
    'q':'(_,)',
    'r':'l2',
    's':'5',
    't':'7',
    'u':'(_)',
    'v':'\\/',
    'w':'\\/\\/',
    'x':'><',
    'y':'j',
    'z':'2',
    '1':'L',
    '2':'R',
    '3':'E',
    '4':'A',
    '5':'S',
    '6':'b',
    '7':'T',
    '8':'B',
    '9':'g',
    '0':'o'
}

def hacker_language(text:str):
    
    new_text = str()
    for letter in text:
        if letter.lower() in trad_dict.keys():
            new_text += trad_dict[letter.lower()]
        else:
            new_text += letter          #En caso que el dígito no se encuentre en la lista, lo devolveremos igual. Por ejemplo la 'ñ' y las vocales con tilde. 
        
    return new_text

n = 'Hola'
print(hacker_language(n))

if __name__ == '__main__':
    text = 'Hoy es 08 de Enero y estoy realizando el reto de programación propuesto por Moruredev. Buena suerte!'
    print(hacker_language(text))