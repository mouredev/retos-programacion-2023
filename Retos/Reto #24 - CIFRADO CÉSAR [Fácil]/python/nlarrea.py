"""
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
"""

alphabet = [char for char in 'abcdefghijklmnñopqrstuvwxyz']

def cesar_cipher(text, number = 3, cipher = True):
    text_list = [char for char in text.lower()]
    
    def map_func(char):
        try:
            current_position = alphabet.index(char)

            if cipher:
                position = current_position + number

                if position >= len(alphabet):
                    position = abs(len(alphabet) - position)

                return alphabet[position]
            else:
                position = current_position - number

                if position < 0:
                    position = len(alphabet) + position

                return alphabet[position]
        except ValueError:
            return char
        
    ciphered_text = list(map((lambda x: map_func(x)), text_list))

    return ''.join(ciphered_text)


print(cesar_cipher('Hola mundo!'))                        # krñd oxpgr!
print(cesar_cipher('abcdefghijklmnñopqrstuvwxyz'))        # defghijklmnñopqrstuvwxyzabc
print(cesar_cipher('abcdefghijklmnñopqrstuvwxyz', 5))     # fghijklmnñopqrstuvwxyzabcde

print(cesar_cipher('krñd oxpgr!', 3, False))              # hola mundo!