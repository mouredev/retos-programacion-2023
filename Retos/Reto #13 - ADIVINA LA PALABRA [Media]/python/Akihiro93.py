import random
texto_1 = "python"

temp =""
numbers = []

for i in range(0, 3):
    n = random.randint(0, 5)
    while str(n) in temp:
        n = random.randint(0, 5)
    temp= temp + str(n)
    numbers.append(int(n))


faltantes = []
for i in numbers:
    faltantes.append(texto_1[i])
    texto_1 = texto_1[:i] + "_" + texto_1[i+1:] 


numero_intentos = 2
comprobaciones = []
l_1, l_2, l_3 = faltantes

print(f"El texto a descubrir es: '{texto_1}'")
while numero_intentos != 0:
    if set(comprobaciones) == set(faltantes):
        print("Correcto la palabra es python")
        break

    print(f"Numero de intentos: {numero_intentos}")
    entrada = input("¿Que letra falta?: ")
    if len(entrada) != 1:
        print("Solo se permite una letra")
        continue

    if l_1 == entrada:
        print(f"Correcto una de las letras es {l_1}")
        comprobaciones.append(l_1)
    elif l_2 == entrada:
        print(f"Correcto una de las letras es {l_2}")
        comprobaciones.append(l_2)
    elif l_3 == entrada:
        print(f"Correcto una de las letras es {l_3}")
        comprobaciones.append(l_3)
    else:
        print("Error: no es la letra que falta")
        numero_intentos -= 1
else:
    print("Ya no tiene más intentos")
