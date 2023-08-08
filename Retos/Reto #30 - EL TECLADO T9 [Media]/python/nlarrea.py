"""
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
"""


T9_KEYBOARD = {
    0: ' ',
    1: ',.?!',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}


def decodeT9Keyboard(text:str):
    chars = text.split('-')

    decodedText = ''
    for char in chars:
        times = len(char) - 1
        
        decodedText += T9_KEYBOARD[int(char[0])][times]

    return decodedText


print(decodeT9Keyboard('6-666-88-777-3-33-888'))                    # MOUREDEV
print(decodeT9Keyboard('444-0-2-6-0-66-555-2-777-777-33-2'))        # I AM NLARREA