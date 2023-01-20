#password
import random
valid_chars = [] 

valid_chars += list("abcdefghijklmnopqrstuvwxyz")
password = ""


print("Generador de Contraseñas, Marca ACME")

while True:
    try:
        longitud = int(input("Ingrese Longitud deseada Minimo 8 Maximo 16: "))
        if longitud < 8 or longitud > 16:
            raise ValueError("La longitud debe ser entre 8 y 16.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        maymin = input(
            "Desea que su password contega letras Mayusculas? S/N: ")
        if maymin.upper() not in ['S', 'N']:
            raise ValueError("Ingrese S o N.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        number = input("Desea que su password Numeros? S/N: ")
        if number.upper() not in ['S', 'N']:
            raise ValueError("Ingrese S o N.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        simbolos = input(
            "Desea que su Password contenga Caracteres Especiales S/N: ")
        if simbolos.upper() not in ['S', 'N']:
            raise ValueError("Ingrese S o N.")
        break
    except ValueError as e:
        print(e)



if maymin.lower() == 's':
    valid_chars += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if number.lower() =="s":
    valid_chars += list("0123456789")
if simbolos.lower() == 's':
    valid_chars += list("!@#$%^&*()_+-=[]{}|;':\"<>,.?/")



for i in range(longitud):
    password += random.choice(valid_chars)
print(f"Su Nuevo password es: {password}")





import random
valid_chars = [] 

valid_chars += list("abcdefghijklmnopqrstuvwxyz")
password = ""


print("Generador de Contraseñas, Marca ACME")

while True:
    try:
        longitud = int(input("Ingrese Longitud deseada Minimo 8 Maximo 16: "))
        if longitud < 8 or longitud > 16:
            raise ValueError("La longitud debe ser entre 8 y 16.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        maymin = input(
            "Desea que su password contega letras Mayusculas? S/N: ")
        if maymin.upper() not in ['S', 'N']:
            raise ValueError("Ingrese S o N.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        number = input("Desea que su password Numeros? S/N: ")
        if number.upper() not in ['S', 'N']:
            raise ValueError("Ingrese S o N.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        simbolos = input(
            "Desea que su Password contenga Caracteres Especiales S/N: ")
        if simbolos.upper() not in ['S', 'N']:
            raise ValueError("Ingrese S o N.")
        break
    except ValueError as e:
        print(e)



if maymin.lower() == 's':
    valid_chars += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if number.lower() =="s":
    valid_chars += list("0123456789")
if simbolos.lower() == 's':
    valid_chars += list("!@#$%^&*()_+-=[]{}|;':\"<>,.?/")



for i in range(longitud):
    password += random.choice(valid_chars)
print(f"Su Nuevo password es: {password}")





