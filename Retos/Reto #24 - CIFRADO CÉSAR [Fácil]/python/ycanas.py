def cipher(text, decrypt, n):
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    output   = ""

    for letter in text:
        is_upper = letter.isupper()
        letter   = letter.lower()

        if letter in alphabet:
            index = (alphabet.index(letter) + ( - n if decrypt else n)) % len(alphabet)
            output = output + (alphabet[index].upper() if is_upper else alphabet[index])
        
        else:
            output = output + letter
    
    return output


text = "Yair Cañas"

cipher_text = cipher(text, False, 2)
decrypt_text = cipher(cipher_text, True, 2)

print(cipher_text + '\n' + decrypt_text)
