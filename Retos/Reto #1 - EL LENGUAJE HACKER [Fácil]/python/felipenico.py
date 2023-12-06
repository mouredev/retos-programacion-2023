'''/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */'''
class Encrypt:
    alphabet = {
        'A':'4',
        'B':'I3',
        'C':'[',
        'D':')',
        'E':'3',
        'F':'|=',
        'G':'&',
        'H':'#',
        'I':'1',
        'J':',_|',
        'K':'>|',
        'L':'1',
        'M':'JVI',
        'N':'Λ/',
        'O':'0',
        'P':'|°',
        'Q':'(_,)',
        'R':'I2',
        'S':'5',
        'T':'7',
        'U':'(_)',
        'V':'\/',
        'W':'\/\/',
        'X':'><',
        'Y':'j',
        'Z':'2',
        '0':'o',
        '1':'L',
        '2':'R',
        '3':'E',
        '4':'A',
        '5':'S',
        '6':'b',
        '7':'T',
        '8':'B',
        '9':'g',

    }
    def lorem_ipsum():
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        #return "hola Mundo"
    def hackear():
        c = ""
        for n in Encrypt.lorem_ipsum().upper():
            if(n.isalnum()): #n in Encrypt.alphabet.keys()
                c += Encrypt.alphabet[n]
            else:
                c += n
        return c
print(Encrypt.hackear())

