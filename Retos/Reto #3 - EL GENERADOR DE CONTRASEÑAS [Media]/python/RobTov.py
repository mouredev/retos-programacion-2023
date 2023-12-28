from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


def password_generator(size: int, uppers: bool, dig: bool, punct: bool) -> str:
    val_list = ascii_lowercase
    if uppers:
        val_list += ascii_uppercase
    if dig:
        val_list += digits
    if punct:
        val_list += punctuation

    print(''.join(random.choice(val_list) for _ in range(size)))
    return ''.join(random.choice(val_list) for _ in range(size))


def start():
    password_generator(8, False, False, False)
    password_generator(9, False, False, True)
    password_generator(10, True, False, False)
    password_generator(11, False, True, False)
    password_generator(12, True, True, False)
    password_generator(13, False, True, True)
    password_generator(14, True, False, True)
    password_generator(15, True, True, True)


if __name__ == '__main__':
    start()
