import random
import string


def password_generator(n=8, upper=True, digits=True, punctuation=True) -> str:
    if (n < 8) or (n > 16):
        raise ValueError("Parameter n must be between 8 and 16")

    options = string.ascii_lowercase
    if upper:
        options = options + string.ascii_uppercase
    if digits:
        options = options + string.digits
    if punctuation:
        options = options + string.punctuation

    return "".join(random.choices(options, k=n))


print(password_generator())
print(password_generator(n=16))
print(password_generator(n=16, punctuation=False))
print(password_generator(n=16,  digits=False, punctuation=False))
print(password_generator(n=16, upper=False, digits=False, punctuation=False))
print(password_generator(n=17))
