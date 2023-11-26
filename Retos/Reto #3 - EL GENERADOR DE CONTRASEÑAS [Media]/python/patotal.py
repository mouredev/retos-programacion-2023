import random, string

base = list(string.ascii_lowercase)

while True:
    longitud = int(input("Indique longitud de contraseña a generar entre 8 y 16 caracteres: "))
    if longitud < 8 or longitud > 16:
        print ("Número fuera de rango, vuelva a intentarlo")
    else:
        break

pregunta_mayusculas = input("¿Puede contener mayúsculas? y/n: ")
pregunta_nro = input("¿Puede contener números? y/n: ")
pregunta_especiales = input("¿Puede contener caracteres especiales? y/n: ")

if pregunta_mayusculas == "y":
    for i in string.ascii_uppercase:
        base.append(i)

if pregunta_nro == "y":
    for i in string.digits:
        base.append(i)

if pregunta_especiales == "y":
    for i in string.punctuation:
        base.append(i)

passw = ""
for i in range(longitud):
    passw += random.choice(base)

print (f"Su contraseña es: {passw}")