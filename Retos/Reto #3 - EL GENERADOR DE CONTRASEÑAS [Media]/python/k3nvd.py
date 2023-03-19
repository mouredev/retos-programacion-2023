import random
def generate(length=8, capitalize=False, numbers=False, symbols=False):
    characters = list(range(97,123))

    if capitalize:
        characters += list(range(65,91))
    password = ""
    
    if numbers:
        characters+= list(range(48,58))

    if numbers:
        characters+= list(range(33,48)) + list(range(58,65)) + list(range(91,97))
    limited= 8  if length < 8 else 16 if length > 16 else length


    #limitedd =16
    #if limited <8:
        
    #    print('Please write 8 chars')
    #elif limitedd>16:
    #    print('Respect the length')
    #else:
    #    length
    #    print('Thanks for writing correctly')

    while len(password) < limited:
        
        password += chr(random.choice(characters))


    return password
#length= int(input('Type the numbers of chars: '))
print(generate())
print(generate(length=16, capitalize=True, numbers=True, symbols=True))

