import random

def generatePassword(length: int = 8, with_upper: bool = True, with_number: bool = True, with_symbol: bool = True) -> str:
    chars = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]

    if with_upper:
        upper_letters = [str.upper(ch) for ch in chars]
        chars += upper_letters

    if with_number:
        numbers = str(list(range(10)))
        chars += numbers
    
    if with_symbol:
        symbols = [
            '!', '@', '#', '$', '%', '&', '*', '?', '+', '-', '=', '_', '|', '/', '\\', '^', '~', '<', '>', ':',
            ';', ',', '.', '(', ')', '[', ']', '{', '}', '"', "'", '`', '¡', '¿'
        ]
        chars += symbols
    
    if (length >= 6) & (length <= 16):
        pwd = []
        for _ in range(length):
            pwd.append(random.choice(chars))
        pwd = ''.join(pwd)
            
    else:
        pwd = '¡Error! La longitud de la contraseña debe ser entre 8 y 16'
    
    return pwd

if __name__=='__main__':
    password = generatePassword(length=16, with_upper=True, with_number=False, with_symbol=True)
    print(password)
