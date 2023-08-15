"""
Reto #30: El teclado T9

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


def teclado_t9(combinacion: str) -> str:
    t9 = {
        '0': ',.?!', '1': ' ',
        '2': 'ABC', '3': 'DEF', '4': 'GHI',
        '5': 'JKL', '6': 'MNO', '7': 'PQRS',
        '8': 'TUV', '9': 'WXYZ'
    }
    combinacion = combinacion.split('-')
    resultado = ''
    for bloque in combinacion:
        resultado += t9[bloque[0]][len(bloque) - 1]
    return resultado


if __name__ == "__main__":
    combinacion = input('Ingresa la combinación de pulsaciones del T9: ')
    print(teclado_t9(combinacion))
