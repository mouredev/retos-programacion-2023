"""
Enunciado

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


lst = [[], ['a', 'b', 'c'],['d','e','f'],['g','h','i'], ['j','k','l'], ['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

def input_chain(chain): # only return a list with the string split with '-'
    return chain.split('-')

def is_valid_block(chain): # Select a valid block with only one character in the string if there have two or more characters
    for block in chain:
        num = len(set(block))
        if num >= 2:
            print('Inserte una cadena valida')
            return False
        else:
            continue
    return True

def join_a_word(chain):
    lst_tup = []
    word = []
    if is_valid_block(chain):
        for ch in chain:
            if ch.isnumeric():
                tup = (int(ch[0])-1, len(ch)-1) # The tuple contains a number and stimes pulse the number.
                lst_tup.append(tup)
        for tup in lst_tup:
            if tup:
                k,j  = tup
                word.append(lst[k][j])
    word = ''.join(word)
    print(word) 
            
chain =  "6-666-88-777-33-3-33-888"
chain = input_chain(chain)
chain = join_a_word(chain)
