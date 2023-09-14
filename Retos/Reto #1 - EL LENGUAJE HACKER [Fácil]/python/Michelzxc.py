'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

import unittest


def main():
    print('###  Traductor Hack  ###')
    print('# Escribe exit() para  #')
    print('# terminar o <Ctrl-C>  #')
    print('########################')
    while True:
        entrada_usuario = input('< ')
        if entrada_usuario == 'exit()':
            break
        else:
            print(f'> {traduce(entrada_usuario)}\n')


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


class TestLenguajeHack(unittest.TestCase):
    def test_traduce(self):
        self.assertEqual(traduce('leet'), '1337')
        self.assertEqual(
            traduce('soy un texto para probar.'),
            '50j (_)^/ 73><70 |*4l24 |*l20l34l2.'
        )
        self.assertEqual(
            traduce('esto es un unittest de python. Se esta comprobando el funcionamiento.'),
            '3570 35 (_)^/ (_)^/177357 )3 |*j7#0^/. 53 3574 [0/\\/\\|*l20l34^/)0 31 |=(_)^/[10^/4/\\/\\13^/70.'
        )
        self.assertEqual(
            traduce('3 millones, 82, 0.5 y otros.'),
            'E /\\/\\1110^/35, BR, o.S j 07l205.'
        )


if __name__ == '__main__':
    # unittest.main()
    main()
