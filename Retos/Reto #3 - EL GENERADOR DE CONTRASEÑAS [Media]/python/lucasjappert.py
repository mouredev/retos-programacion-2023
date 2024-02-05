import string
import random

def get_new_password(pass_length: int, include_upper_case_letters: bool = True, include_numbers: bool = True, include_symbols: bool = True):
    if pass_length < 8 or pass_length > 16: return "--------"
    result: str = ""

    possible_chars = string.ascii_lowercase
    if include_upper_case_letters: possible_chars += string.ascii_uppercase
    if include_numbers: possible_chars += string.digits
    if include_symbols: possible_chars += string.punctuation

    for i in range(0, pass_length):
        random_index = random.randint(0, len(possible_chars) - 1)
        result += possible_chars[random_index]

    return result

print("Contraseñas aleatorias que permiten mayúsculas, números y símbolos")
for pass_length in range(6, 18):
    print(get_new_password(pass_length))
    
print("Contraseñas aleatorias que permiten mayúsculas y números, pero NO símbolos")
for pass_length in range(6, 18):
    print(get_new_password(pass_length, True, True, False))
    
print("Contraseñas aleatorias que permiten mayúsculas, pero NO números ni símbolos")
for pass_length in range(6, 18):
    print(get_new_password(pass_length, True, False, False))
    
print("Contraseñas aleatorias que NO permiten mayúsculas ni números ni símbolos")
for pass_length in range(6, 18):
    print(get_new_password(pass_length, False, False, False))