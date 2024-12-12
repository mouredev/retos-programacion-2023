# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */


def transformar_lenguaje_hacker(texto):
    if not texto == 'str':
        raise TypeError('El texto no puede contener números')
    else:
        leet_dict = {
            'a': '4', 'b': '13', 'c': '[', 'd': ')', 'e': '3',
            'f': '|=', 'g': '6', 'h': '#', 'i': '1', 'j': ',_|',
            'k': '>|', 'l': '1', 'm': '/\\/\\', 'n': '^/', 'o': '0',
            'p': '|*', 'q': '(_,)', 'r': 'I2', 's': '5', 't': '7',
            'u': '(_)', 'v': '\\/', 'w': '\\/\\/', 'x': '><', 'y': '`/',
            'z': '2', '1': 'L', '2': 'R', '3': 'E', '4': 'A', '5': 'S',
            '6': 'b', '7': 'T', '8': 'B', '9': 'g', '0': 'o'
        }

        texto_hacker = ''.join(leet_dict.get(char.lower(), char)  for char in texto)

        return texto_hacker
        
try:       
    texto_usuario = input('Escribe un texto: ')

    resultado = transformar_lenguaje_hacker(texto_usuario)

    print(f'Texto en lenguaje hacker: {resultado}')

except TypeError as e:
    print(e)
