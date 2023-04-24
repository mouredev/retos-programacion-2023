import random
def passwordGenerator():
    length = str(input("Cual quieres que sea la longitud de la contraseña? (8-16): "))
    want_upper = input("Quieres que contenga letras mayúsculas? (y,n): ")
    want_num = input("Quieres que contenga numeros? (y,n): ")
    want_simb = input("Quieres que contenga símbolos? (y,n): ")

    count = 1
    password = ""
    choosed = list()

    while(count <= int(length)):
        lower = chr(random.randrange(97, 122))
        choosed.append(lower)

        if(want_upper == "y"):
            upper = chr(random.randrange(65, 90))
            choosed.append(upper)

        if(want_num == "y"):
            num = random.randint(1,9)
            choosed.append(str(num))

        if(want_simb == "y"):      
            simb = random.choice((chr(random.randrange(33, 47)), chr(random.randrange(58, 64)), chr(random.randrange(91, 96))))
            print(simb)
            choosed.append(simb)

        password += random.choice(choosed)
        count += 1
    return password
print(passwordGenerator())