def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a text using the Caesar cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The number of positions to shift the characters.

    Returns:
        str: The result of the encryption or decryption.
    """
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            code = ord(char)
            shifted_code = (code - ord("a") + shift) % 26 + ord("a")
            shifted_char = chr(shifted_code)
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char
    return result

def caesar_decipher(ciphertext, shift):
    """
    Decrypts a text encrypted with the Caesar cipher.

    Args:
        ciphertext (str): The text to be decrypted.
        shift (int): The number of positions the characters were shifted during encryption.

    Returns:
        str: The decrypted text.
    """
    return caesar_cipher(ciphertext, -shift)

def main():
    """
    Main function to get user input, perform encryption and decryption, and display results.
    """
    original_text = input("Enter the text to encrypt: ")
    shift_amount = int(input("Enter the shift amount (integer): "))

    encrypted_text = caesar_cipher(original_text, shift_amount)
    print("Encrypted text:", encrypted_text)

    decrypted_text = caesar_decipher(encrypted_text, shift_amount)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
