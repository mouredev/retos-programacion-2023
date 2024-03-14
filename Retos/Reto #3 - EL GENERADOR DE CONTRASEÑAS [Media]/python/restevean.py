import random
import string


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    allowed_chars = string.ascii_lowercase
    if use_uppercase:
        allowed_chars += string.ascii_uppercase
    if use_numbers:
        allowed_chars += string.digits
    if use_symbols:
        allowed_chars += string.punctuation
    if length < 8 or length > 16:
        # raise ValueError("La longitud debe estar entre 8 y 16")
        length = 8

    return ''.join(random.choice(allowed_chars) for _ in range(length))


def generate_password_2(length=8, use_uppercase=True, use_numbers=True, use_symbols=True):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if use_uppercase else ""
    numbers = "0123456789" if use_numbers else ""
    symbols = "!@#$%^&*()" if use_symbols else ""

    allowed_chars = lowercase_letters + uppercase_letters + numbers + symbols
    if length < 8 or length > 16:
        # raise ValueError("La longitud debe estar entre 8 y 16")
        length = 8

    return ''.join(random.choice(allowed_chars) for _ in range(length))


def main():
    password = generate_password(16, False, False, False)
    print(password)
    password = generate_password(16, False, False, True)
    print(password)
    password = generate_password(16, False, True, True)
    print(password)
    password = generate_password(16, True, True, True)
    print(password)
    password = generate_password_2(16, False, False, False)
    print(password)
    password = generate_password_2(16, False, False, True)
    print(password)
    password = generate_password_2(16, False, True, True)
    print(password)
    password = generate_password_2(16, True, True, True)
    print(password)


if __name__ == '__main__':
    main()
