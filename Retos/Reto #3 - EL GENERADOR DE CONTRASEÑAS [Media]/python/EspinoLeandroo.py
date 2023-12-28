import random

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbols_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
allChars = []

password = ""
length = input("Longitud de la contraseña [8-16]:")
mayus = input("Incluir Mayusculas (S/N):")
numbers = input("Incluir Números (S/N):")
simbols = input("Incluir Simbolos (S/N):")

if mayus == "S":
    [allChars.append(str(c).capitalize())  for c in letters_list]

[allChars.append(str(c))  for c in letters_list]

if numbers == "S":
    [allChars.append(str(c).capitalize())  for c in numbers_list]
    
if simbols == "S":
    [allChars.append(str(c).capitalize())  for c in simbols_list]


for i in range(0, int(length) + 1):
    password += str(random.choice(allChars))

print("Contraseña generada: " + password)