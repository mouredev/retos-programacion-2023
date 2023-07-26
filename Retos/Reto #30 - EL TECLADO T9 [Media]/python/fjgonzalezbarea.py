"""
 Los primeros dispositivos móviles tenían un teclado llamado T9
 con el que se podía escribir texto utilizando únicamente su
 teclado numérico (del 0 al 9).

 Crea una función que transforme las pulsaciones del T9 a su
 representación con letras.
 - Debes buscar cuál era su correspondencia original.
 - Cada bloque de pulsaciones va separado por un guión.
 - Si un bloque tiene más de un número, debe ser siempre el mismo.
 - Ejemplo:
     Entrada: 6-666-88-777-33-3-33-888
     Salida: MOUREDEV
"""

t9_keyboard = [' ', ',.?!', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


def validate_block_content(block: str) -> bool:
    characters_set = set(block)  # Remove duplicated. Therefore, there should be just 1 element
    all_numeric = all(character.isnumeric() for character in characters_set)  # Check all are numeric
    return len(characters_set) == 1 and all_numeric


def translate_block_to_letter(block: str) -> str:
    if not validate_block_content(block):
        raise ValueError(f"Wrong block. Each block should contain 1 single number that may be repeated 1 or more times. Received {block}")
    t9_number = int(block[0])
    letters_for_number = t9_keyboard[t9_number]

    # We need to be aware that the user may send more clicks than letters in the position. E.g. 22222 => 'B'
    number_of_clicks = len(block) % len(letters_for_number)
    return letters_for_number[number_of_clicks - 1]


def main(chain: str):
    translated_text = "".join([translate_block_to_letter(block) for block in chain.split("-")])
    print(f"Translated text: {translated_text}")


"""
Examples:
-   Input: 6-666-88-777-33-3-33-888
    Output: MOUREDEV

-   Input: 6666-666666-88888-7777777-33333-3333-33333-888888 --> More clicks than letters in the keyboard number
    Output: MOUREDEV
"""
if __name__ == '__main__':
    t9_input = input("Please, introduce a t9 valid chain: ")
    main(t9_input)
