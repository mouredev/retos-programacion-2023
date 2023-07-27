"""
/*
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
 */
"""

T9_TYPES = {
  '1': '.,?!',
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


def T9_keyboard(text: str) -> str:
  
  message = ''
  
  for numbers in text.split('-'):
    digit = numbers[0]
    message += T9_TYPES[digit][len(numbers)-1]
  
  return message

def T9_keyboard2(text: str) -> str:
  return ''.join(T9_TYPES[numbers[0]][len(numbers)-1] for numbers in text.split('-'))


if __name__ == '__main__':
  sol = T9_keyboard('6-666-88-777-33-3-33-888')
  answer = '👌' if sol == 'MOUREDEV' else '🤦‍♂️'
  print(f"{answer} {sol}")
  
  sol = T9_keyboard2('44-33-555-555-666-0-9-666-777-555-3')
  answer = '👌' if sol == 'HELLO WORLD' else '🤦‍♂️'
  print(f"{answer} {sol}")