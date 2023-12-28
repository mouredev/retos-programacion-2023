import random

letras_minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letras_mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeros = ["1","2","3","4","5","6","7","8","9","10"]
simbolos = ["!","$","%","&","/","=","@","#","~","+","-","*",":",";","¨"]

opciones = [letras_minusculas]

while True:
    longitud = int(input("Elige la longitud de la contraseña (entre 8 y 16 caractéres): "))
    if longitud >= 8 and longitud <= 16:
        break

while True:
    mayusculas = input("¿Quieres añadir mayúsculas? [S/N]: ")
    mayusculas = mayusculas.upper()
    if mayusculas == "S":
        opciones.append(letras_mayusculas)
        break
    elif mayusculas == "N":
        break

while True:
    check_numeros = input("¿Quieres añadir números? [S/N]: ")
    check_numeros = check_numeros.upper()
    if check_numeros == "S":
        opciones.append(numeros)
        break
    elif check_numeros == "N":
        break

while True:
    check_simbolos = input("¿Quieres añadir símbolos? [S/N]: ")
    check_simbolos = check_simbolos.upper()
    if check_simbolos == "S":
        opciones.append(simbolos)
        break
    elif check_simbolos == "N":
        break

contraseña = ""

for i in range(0,longitud):
    eleccion = random.randint(0,(len(opciones)-1))
    valor = random.randint(0,len(opciones[eleccion])-1)
    contraseña += opciones[eleccion][valor]

print(contraseña)