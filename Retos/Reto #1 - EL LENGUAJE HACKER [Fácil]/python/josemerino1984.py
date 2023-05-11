"""*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */"""

alphabeto={

    'a': '@',
    'b': '8',
    'c': '(',
    'd': 'd',
    'e': '3',
    'f': 'ph',
    'g': '9',
    'h': '#',
    'i': '!',
    'j': 'j',
    'k': '|<',
    'l': '1',
    'm': '|\\/|',
    'n': '|\\|',
    'o': '0',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': '$',
    't': '7',
    'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><',
    'y': '`/',
    'z': '2'}

string= input("ingrese texto :")
string2=""
for i in string:
    if i in alphabeto:
        string2+=alphabeto[i]

    else:
        string2+=" "
        
print(string2)