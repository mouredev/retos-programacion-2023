from random import choice
from string import punctuation, ascii_lowercase, ascii_uppercase, digits


def random_password(length: int, upper: bool = False, digit: bool = False, symbol: bool = False):

    password = ""
    words = [ascii_lowercase]

    if length >= 8 and length <= 16:
        if upper:
            words.append(ascii_uppercase)
        if digit:
            words.append(digits)
        if symbol:
            words.append(punctuation)

        for i in range(length):
            word_list = choice(words)
            password += choice(word_list)

    else:
        return "La longitud debe tener entre 8 y 16 caracteres"

    return password



print(random_password(10, True, False, True))
print(random_password(1))
print(random_password(10, upper=True, symbol=True))
print(random_password(16, True, True, True))
print(random_password(16, True))
print(random_password(-16, True))