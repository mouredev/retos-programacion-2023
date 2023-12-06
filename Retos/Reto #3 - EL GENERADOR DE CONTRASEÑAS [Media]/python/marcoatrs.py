import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_password(
    length: int,
    lc: bool = True,
    uc: bool = True,
    nums: bool = True,
    special: bool = True,
) -> str:
    if not 16 >= length >= 8:
        print("La contraseña debe ser de entre 8 y 16 caracteres")
        return
    pwd_str = ""
    if lc:
        pwd_str += ascii_lowercase
    if uc:
        pwd_str += ascii_uppercase
    if nums:
        pwd_str += digits
    if special:
        pwd_str += punctuation
    if not pwd_str:
        print("Seleccione al menos un tipo de caracter")
        return
    return "".join([random.choice(pwd_str) for _ in range(length)])


print(generate_password(16, lc=True, uc=True, nums=True, special=True))
print(generate_password(8, lc=True, uc=True, nums=False, special=True))
print(generate_password(3, lc=True, uc=True, nums=False, special=True))
