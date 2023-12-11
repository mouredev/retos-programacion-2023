#LA PALABRA DE 100 PUNTOS

"""
* Crea un programa que calcule los puntos de una palabra.
* - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
*   español de 27 letras, la A vale 1 y la Z 27.
* - El programa muestra el valor de los puntos de cada palabra introducida.
* - El programa finaliza si logras introducir una palabra de 100 puntos.
* - Puedes usar la terminal para interactuar con el usuario y solicitarle
*   cada palabra.
"""

alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
valor_letra = {}

# Crear el diccionario de valores de letras
for i, letra in enumerate(alfabeto, 1):
    valor_letra[letra] = i

# Función para sumar los valores de las letras en una palabra
def sumar_valores_palabra(palabra):
    suma = 0
    for letra in palabra.upper():  # Convertir la palabra a mayúsculas para manejar letras mayúsculas o minúsculas
        if letra in valor_letra:
            suma = suma + valor_letra[letra]  # suma += valor_letra[letra]
    return suma


resultado = 0
while resultado != 100:
    palabra = input("Introduce una palabra: ")
    resultado = sumar_valores_palabra(palabra)
    print(f"La suma de los valores de las letras en '{palabra}' es: {resultado}")

print(f"Felicidades el valor en {palabra} en 100!")

        

