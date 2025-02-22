import random

def password_generator(length = 8, capital = False, numbers = False, symbols = False):
    f_length = 0
    password = ''
    characters = list(range(97, 123))
    if capital:
        characters += list(range(65, 91))
    if numbers:
        characters += list(range(48, 58))
    if symbols:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))
    if length > 8 and length < 16:
        f_length = length
    elif length <= 8:
        f_length = 8
    else:
        f_length = 16
    for char in range(f_length):
        password += chr(random.choice(characters))
    return password

print(password_generator())