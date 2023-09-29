import string

def caesar_cipher(text: str, decrypt = False, shift = 3):

    alphabet = list(string.ascii_lowercase)
    alphabet.insert(alphabet.index("n") + 1, "ñ")

    caesar_text = ""

    for value in text.lower():
        if value in alphabet:
            index = (alphabet.index(value) + (-shift if decrypt else shift)) % len(alphabet)
            caesar_text += alphabet[index]
        else:
            caesar_text += value

    print(caesar_text)

caesar_cipher("Mi nombre es MoureDev.")
caesar_cipher("ol proeuh hv orxuhghy.", True)
caesar_cipher("Mi nombre es MoureDev.", shift=5)
caesar_cipher("qn rtqgwj jx qtzwjija.", True, 5)