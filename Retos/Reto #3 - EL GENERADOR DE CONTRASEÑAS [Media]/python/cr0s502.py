import random2

def generarPassword():    
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "12345678901234567890"
    especial = "!@/#$%&_*-](}@[){?\'"

    length = int(input("Ingresa la longitud de tu password: "))
    all = upper + lower + number + especial
    
    passwords = "".join(random2.choice(all) for i in range(length))
    return passwords


print(generarPassword())
