'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''


def traduce(texto: str) -> str:
    '''Traduce el argumento "texto" desde Lenguaje Natural a Lenguaje Hack.'''
    MAPA_DE_CARACTERES = {
        'A': '4', 'B': 'l3', 'C': '[', 'D': ')', 'E': '3', 'F': '|=',
        'G': '&', 'H': '#', 'I': '1', 'J': ',_|', 'K': '>|', 'L': '1',
        'M': '/\\/\\', 'N': '^/', 'O': '0', 'P': '|*', 'Q': '(_,)',
        'R': 'l2', 'S': '5', 'T': '7', 'U': '(_)', 'V': '\\/',
        'W': '\\/\\', 'X': '><', 'Y': 'j', 'Z': '2',
        '1': 'L', '2': 'R', '3': 'E', '4': 'A', '5': 'S', '6': 'b',
        '7': 'T', '8': 'B', '9': 'g', '0': 'o',
    }
    texto_normalizado = texto.upper()
    texto_hack = texto_normalizado.translate(str.maketrans(MAPA_DE_CARACTERES))
    return texto_hack
