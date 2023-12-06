# Reto #30: El teclado T9
#### Dificultad: Media | Publicación: 24/07/23 | Corrección: 31/07/23

## Enunciado


#
# Los primeros dispositivos móviles tenían un teclado llamado T9
# con el que se podía escribir texto utilizando únicamente su
# teclado numérico (del 0 al 9).
#
# Crea una función que transforme las pulsaciones del T9 a su
# representación con letras.
# - Debes buscar cuál era su correspondencia original.
# - Cada bloque de pulsaciones va separado por un guión.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
# - Ejemplo:
#     Entrada: 6-666-88-777-33-3-33-888
#     Salida: MOUREDEV
#

class T9Converter:
    def __init__(self):
        self.t9_mapping = {
            '0': ' ',
            '2': 'ABC',
            '3': 'DEF',
            '4': 'GHI',
            '5': 'JKL',
            '6': 'MNO',
            '7': 'PQRS',
            '8': 'TUV',
            '9': 'WXYZ'
        }

    def t9_to_letters(self, keypresses):
        result = []
        keypresses = keypresses.split('-')

        for block in keypresses:
            num = block[0]
            times = len(block)
            letter = self.t9_mapping[num][times - 1]
            result.append(letter)

        return ''.join(result)

if __name__ == "__main__":
    input_sequence1 = "6-666-88-777-33-3-33-888"
    input_sequence2 = "5-88-2-66-0-222-2-777-555-666-7777"
    t9_converter = T9Converter()
    output = t9_converter.t9_to_letters(input_sequence1)
    print(output)  # "MOUREDEV"
    output = t9_converter.t9_to_letters(input_sequence2)
    print(output)  # "JUAN CARLOS"