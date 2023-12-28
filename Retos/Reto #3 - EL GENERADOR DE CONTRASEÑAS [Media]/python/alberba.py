import random

def password_generator(length = 8, capital = False, numbers = False, symbol = False):
    characters = list()
    
    characters += list(range(97, 123))

    if capital:
        characters += list(range(65, 91))
    if numbers:
        characters += list(range(48, 58))
    if symbol:
        characters += list(range(58, 65)) + list(range(33, 48)) + \
                    list(range(123, 127)) + list(range(91,97))
        
    length = 8 if length < 8 else 16 if length > 16 else length

    password = str()
    for i in range(length):
        password += chr(random.choice(characters))

    return password

print(password_generator())
print(password_generator(length=16))
print(password_generator(length=1))
print(password_generator(length=22))
print(password_generator(length=12, capital=True))
print(password_generator(length=12, capital=True, numbers=True))
print(password_generator(length=12, capital=True, numbers=True, symbol=True))
print(password_generator(length=12, capital=True, symbol=True))

