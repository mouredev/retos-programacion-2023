from termcolor import colored


class CesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha() or char.isdigit() or char.isspace() or char in [".", ",", "!", "?"]:
                if char.isalpha():
                    encrypted_char = chr((ord(char.upper()) - 65 + self.shift) % 26 + 65)
                    encrypted_text += encrypted_char if char.isupper() else encrypted_char.lower()
                else:
                    encrypted_text += char
            else:
                raise ValueError("Invalid input. Only alphanumeric characters, spaces, and punctuation marks are allowed.")
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha() or char.isdigit() or char.isspace() or char in [".", ",", "!", "?"]:
                if char.isalpha():
                    decrypted_char = chr((ord(char.upper()) - 65 - self.shift) % 26 + 65)
                    decrypted_text += decrypted_char if char.isupper() else decrypted_char.lower()
                else:
                    decrypted_text += char
            else:
                raise ValueError("Invalid input. Only alphanumeric characters, spaces, and punctuation marks are allowed.")
        return decrypted_text


def colored_input(prompt, color):
    return input(colored(prompt, color))


def cipher_decorator(func):
    def wrapper():
        try:
            text = colored_input("Enter the text: ", "blue")
            shift = int(colored_input("Enter the shift value: ", "magenta"))
            cipher = CesarCipher(shift)
            result = func(cipher, text)
            print(colored("Result: ", "green") + colored(result, "yellow"))
        except ValueError as e:
            print(colored(str(e), "red"))
        except UnicodeDecodeError:
            print(colored("Unable to decrypt the text. Please ensure that only alphanumeric characters, spaces, and punctuation marks are used.", "red"))

    return wrapper


@cipher_decorator
def encrypt_text(cipher, text):
    return cipher.encrypt(text)


@cipher_decorator
def decrypt_text(cipher, text):
    return cipher.decrypt(text)


if __name__ == "__main__":
    try:
        choice = colored_input("Choose an option (1: Encrypt, 2: Decrypt): ", "cyan")
        if choice == "1":
            encrypt_text()
        elif choice == "2":
            decrypt_text()
        else:
            print(colored("Invalid choice!", "red"))
    except KeyboardInterrupt:
        print(colored("\nProgram terminated by user.", "yellow"))
