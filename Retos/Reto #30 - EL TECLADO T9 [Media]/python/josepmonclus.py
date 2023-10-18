
'''
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
'''

keyboard = {
    '1': ',.?!',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}

def convert(input: str) -> str:
    text = ''
    split = input.split('-')
    for s in split:
        for i in range(0, len(s)):
            if s[0] != s[i] or s[0] not in keyboard or len(s) > len(keyboard[s[0]]):
                return '¡¡ERROR!!'
        
        text += keyboard[s[0]][len(s) - 1]
    
    return text

print(convert('6-666-88-777-33-3-33-888-1111'))
print(convert('222-666-6-666-0-33-7777-8-2-7777-111'))