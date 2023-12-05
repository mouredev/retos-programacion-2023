import random

#Función que genera una contraseña con valores por defecto
def password_creator(length = 8, uppercase = "no", number = "no", symbol = "no"):
    #Variables
    password = ""
    random_character = ""

    try:
        #Generamos la contraseña según las opciones marcadas con el codigo ASCII
        #Solo letras minusculas entre 8 y 16 letras de longitud
        if length >= 8 and length <= 16 and uppercase == "no" and number == "no" and symbol == "no":
            while length > 0:
                password += chr(random.randint(97, 122))
                length-=1
        #Con letras minusculas y mayusculas entre 8 y 16 letras de longitud
        elif length >= 8 and length <= 16 and uppercase == "si" and number == "no" and symbol == "no":
            while length > 0:
                random_character = random.randint(65, 122)
                if random_character >= 65 and random_character <= 90 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        #Con letras minusculas y numeros
        elif length >= 8 and length <= 16 and uppercase == "no" and number == "si" and symbol == "no":
            while length > 0:
                random_character = random.randint(48, 122)
                if random_character >= 48 and random_character <= 57 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        #Con letras minusculas y simbolos
        elif length >= 8 and length <= 16 and uppercase == "no" and number == "no" and symbol == "si":
            while length > 0:
                random_character = random.randint(33, 122)
                if random_character >= 33 and random_character <= 47 or random_character >= 60 and random_character <= 64 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        #Con letras minusculas, mayusculas y numeros
        elif length >= 8 and length <= 16 and uppercase == "si" and number == "si" and symbol == "no":
            while length > 0:
                random_character = random.randint(48, 122)
                if random_character >= 48 and random_character <= 57 or random_character >= 65 and random_character <= 90 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        #Con letras minusculas, mayusculas y simbolos
        elif length >= 8 and length <= 16 and uppercase == "si" and number == "no" and symbol == "si":
            while length > 0:
                random_character = random.randint(33, 122)
                if random_character >= 33 and random_character <= 47 or random_character >= 60 and random_character <= 95 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        #Con letras minusculas, numeros  y simbolos
        elif length >= 8 and length <= 16 and uppercase == "no" and number == "si" and symbol == "si":
            while length > 0:
                random_character = random.randint(33, 122)
                if random_character >= 33 and random_character <= 57 or random_character >= 60 and random_character <= 64 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        #Con letras minusculas, mayusculas, numeros y simbolos
        elif length >= 8 and length <= 16 and uppercase == "si" and number == "si" and symbol == "si":
            while length > 0:
                random_character = random.randint(33, 122)
                if random_character >= 33 and random_character <= 57 or random_character >= 60 and random_character <= 95 or random_character >= 97 and random_character <= 122:
                    password += chr(random_character)
                    length -= 1
        else:
            print("Error length debe se un número entre 8 y 16, y los parametros uppercase, number o symbol deben ser un \"si\" o un \"no\"")
    except TypeError:
        print("Error length debe se un número entre 8 y 16, y los parametros uppercase, number o symbol deben ser un \"si\" o un \"no\"")

    return password

print(password_creator(length = 10, uppercase = "si", number = "si", symbol = "si"))
print(password_creator(uppercase = "si"))
print(password_creator(length = 10, uppercase = "no", number = "si"))
print(password_creator(length = 12, uppercase = "no", number = "no", symbol = "si"))
print(password_creator(length = 10, uppercase = "si", number = "si"))
print(password_creator(length = 10, uppercase = "si", number = "no", symbol = "si"))
print(password_creator(length = 14, uppercase = "no", number = "si", symbol = "si"))
print(password_creator(length = 16, uppercase = "si", number = "si", symbol = "si"))
