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

alfabeto = {
    'a' : '4',
    'b' : 'I3',
    'c' : '[',
    'd' : ')',
    'e' : '3',
    'f' : '|=',
    'g' : '&',
    'h' : '#',
    'i' : '1',
    'j' : ',_|',
    'k' : '>|',
    'l' : '1',
    'm' : '/\/\\',
    'n' : '^/',
    'o' : '0',
    'p' : '|*',
    'y' : '(_,)',
    'r' : 'I2',
    's' : '5',
    't' : '7',
    'u' : '(_)',
    'v' : '\/',
    'w' : '\/\/',
    'x' : '><',
    'y' : 'j',
    'z' : '2',
}

def lenguaje_hacker(palabra):
    new_palabara = ''
    for letra in palabra:
        if letra in alfabeto:
            new_palabara += alfabeto[letra]
        else:
            new_palabara += letra
    return new_palabara

def main():
    palabra = 'Leet%'
    print(lenguaje_hacker(palabra.lower()))

if __name__ == "__main__":
    main()
