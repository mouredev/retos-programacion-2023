diccionario = {}

for i, code in enumerate(range(65, 91)):
    if i+1 < 15:
        diccionario[chr(code)] = i+1
    else:
        diccionario[chr(code)] = i+2
else:
    diccionario[chr(209)] = 15

def puntos_palabra(diccionario: dict, palabra: str) -> int:
    valor = 0
    for letra in palabra:
        valor += diccionario[letra.upper()]
    return valor

def leer_palabra():
    while True:
        entrada = input("Introduce una palabra\n")
        if entrada.isalpha() and len(entrada) > 0:
            return entrada
        else:
            print("La entrada debe ser una palabra.")

def onehundred_word():
    palabra = leer_palabra()
    valor = puntos_palabra(diccionario, palabra)
    if valor != 100:
        print(f'Esta palabra tiene {valor} puntos!')
        return onehundred_word()
    else:
        return 'Felicitaciones!. Encontraste una palabra de 100 puntos.'
    
print(onehundred_word())