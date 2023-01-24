import random


def password_generator(length=8, capital=False, numbers=False, symbols=False):

    # Fuente: https://www.ascii-code.com

    characters = list(range(97, 123))

    if capital:
        characters += list(range(65, 91))

    if numbers:
        characters += list(range(48, 58))

    if symbols:
        characters += list(range(33, 48)) + \
            list(range(58, 65)) + list(range(91, 97))

    password = ""

    final_length = 8 if length < 8 else 16 if length > 16 else length

    while len(password) < final_length:
        password += chr(random.choice(characters))

    return password


print(password_generator())
print(password_generator(length=16))
print(password_generator(length=1))
print(password_generator(length=22))
print(password_generator(length=12, capital=True))
print(password_generator(length=12, capital=True, numbers=True))
print(password_generator(length=12, capital=True, numbers=True, symbols=True))
print(password_generator(length=12, capital=True, symbols=True))
