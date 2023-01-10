"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""


def translate(character: str, translations: list[tuple[str, str]]) -> str:
    if len(translations) == 0:
        return character

    if translations[0][0] == character:
        return translations[0][1]

    return translate(character, translations[1:])


def run(text: str, translations: list[tuple[str, str]]) -> str:
    if len(text) == 0:
        return ''

    return f'{translate(text[0].lower(), translations)}{run(text[1:], translations)}'


if __name__ == '__main__':
    data = input('Introduce un texto: ')
    keys = {
        'a': '4', 'b': 'I3', 'c': '[', 'd': '|)', 'e': '3', 'f': '|=',
        'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '1', 'm': '/\\/\\',
        'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)', 'r': 'I2', 's': '5', 't': '7',
        'u': '(_)', 'v': '\\/', 'w': 'VV', 'x': '><', 'y': 'Ч', 'z': '2'
    }
    print(run(data, [(k, v) for k, v in keys.items()]))
