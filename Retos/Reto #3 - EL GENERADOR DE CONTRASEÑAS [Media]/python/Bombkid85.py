import string
import random


def gen_password():
    password = ""
    characters = string.ascii_lowercase

    config = configuration()
    lenth = config[0]
    upper = config[1]
    number = config[2]
    symbol = config[3]

    if upper == True:
        characters += string.ascii_uppercase
    if number == True:
        characters += string.digits
    if symbol == True:
        characters += string.punctuation
    characters = list(characters)
    for char in range(lenth):
        password += random.choice(characters)
    print(password)


def configuration():
    print("Configuración password\nCampo en blanco será aleatorio")

    lenth = 0
    upper = ""
    number = ""
    symbol = ""

    while lenth < 8 or lenth > 16:
        lenth = input("Introduce la longitud del password (entre 8 y 16):")
        if lenth == "":
            lenth = int(random.randint(8, 16))
            break
        lenth = int(lenth)
        if lenth < 8 or lenth > 16:
            print("Valor no valido, debe ser un número entre 8 y 16")
            
    while upper is not True and upper is not False:
        upper = input("Utilizar mayúsculas (y/n):")
        if upper == "y":
            upper = True
        elif upper == "n":
            upper = False
        elif upper == "":
            upper = random.choice([True, False])
        else:
            print("Valor no valido")

    while number is not True and number is not False:
        number = input("Utilizar números (y/n):")
        if number == "y":
            number = True
        elif number == "n":
            number = False
        elif number == "":
            number = random.choice([True, False])
        else:
            print("Valor no valido")

    while symbol is not True and symbol is not False:        
        symbol = input("Utilizar símbolos (y/n):")
        if symbol == "y":
            symbol = True
        elif symbol == "n":
            symbol = False
        elif symbol == "":
            symbol = random.choice([True, False])
        else:
            print("Valor no valido")

    return lenth, upper, number, symbol
    
gen_password()
