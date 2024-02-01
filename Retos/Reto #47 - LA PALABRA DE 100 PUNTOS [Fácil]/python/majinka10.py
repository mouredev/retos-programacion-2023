# En esta parte del código creo el diccionario utilizando
# codigo ASCII y enumerando cada letra para asignarle el valor

diccionario = {}

for i, code in enumerate(range(65, 91)):
    if i+1 < 15:
        diccionario[chr(code)] = i+1
    else:
        diccionario[chr(code)] = i+2
else:
    diccionario[chr(209)] = 15 # Else para añadir la Ñ

# Funcion para calcular los puntos de la palabra
def puntos_palabra(diccionario: dict, palabra: str) -> int:
    valor = 0
    for letra in palabra:
        valor += diccionario[letra.upper()]
    return valor

# Funcion para obligar al usuario a introducir una palabra.
def leer_palabra():
    while True:
        entrada = input("Introduce una palabra\n")
        if entrada.isalpha() and len(entrada) > 0:
            return entrada
        else:
            print("La entrada debe ser una palabra.")

# Funcion para encontrar una palabra con 100 puntos.
def onehundred_word():
    palabra = leer_palabra()
    valor = puntos_palabra(diccionario, palabra)
    if valor != 100:
        print(f'Esta palabra tiene {valor} puntos!')
        return onehundred_word()
    else:
        return 'Felicitaciones!. Encontraste una palabra de 100 puntos.'
    
print(onehundred_word())