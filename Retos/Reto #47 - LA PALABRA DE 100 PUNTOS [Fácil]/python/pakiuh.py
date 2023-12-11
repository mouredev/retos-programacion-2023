valores = {chr(i + 65): i + 1 for i in range(14)}
valores['Ñ'] = 15
valores.update({chr(i + 65): i + 2 for i in range(14, 26)})

puntos = 0

while puntos != 100:
    palabra = input("Introduce una palabra: ").upper()
    puntos = 0

    for letra in palabra:
        if letra in valores:
            puntos += valores[letra]
            #print(f"El valor de la letra {letra} es: {valores[letra]}")
    print("La valoración de la palabra es:", puntos)

print("¡Has alcanzado los 100 puntos!")
