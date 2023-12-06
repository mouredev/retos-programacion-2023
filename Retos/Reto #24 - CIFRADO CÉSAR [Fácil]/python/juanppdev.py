from __future__ import print_function
# The Caesar Cipher Algorithm

def main():
    message = input("Introducir Mensaje: ")
    key     = int(input("Key [1-26]: "))
    mode    = input("Cifrar o Descifrar [c/d]: ")

    if mode.lower().startswith('c'):
        mode = "cifrar"
    elif mode.lower().startswith('d'):
        mode = "descifrar"

    translated = encdec(message, key, mode)
    if mode ==   "cifrar":
        print(("Mensaje Cifrado:", translated))
    elif mode == "descifrar":
        print(("Mensaje Descifrado:", translated))
        
def encdec(message, key, mode):
    message    = message.upper()
    translated = ""
    LETTERS    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
    input()