import random, string

caracteres = string.ascii_lowercase

longitud = 0
while int(longitud) < 8 or int(longitud) > 16:
    longitud = input("Ingresar longitud deseada (entre 8 y 16): ")

letras = input("puede contener letras mayusculas? ponga Si o No: ")
if letras.lower() == "si": caracteres += string.ascii_uppercase
 
numeros = input("Puede contener numeros? ponga Si o No: ")
if numeros.lower() == "si": caracteres += string.digits

simbolos = input("Puede contener simbolos? ponga Si o No: ")
if simbolos.lower() == "si": caracteres += string.punctuation

random_list = random.sample(caracteres, k=int(longitud))
contraseña = "".join(random_list)

print(contraseña)
