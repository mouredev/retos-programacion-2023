# ninguna letra se repite
def is_heterograma(string):
    string = string.lower()
    if len(string) == len(set(string)):
        return True
    else:
        return False

# todas la letras tienen la misma cantidad de repeticiones
def is_isograma(string):
    string = string.lower()
    letras = {}
    for letra in string:
        if letra.isalpha():
            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1

    if all(valor == list(letras.values())[0] for valor in letras.values()):
        return True
    else:
        return False

# contine todas la letras del abecedario
def is_pangrama(string):
    string = string.lower()
    for letter in 'abcdefghijklmnñopqrstuvwxyz':
        if letter not in string:
            return False
    return True

string = input('Frase o palabra: ').replace(" ", "")

if is_heterograma(string):
    print(f'{string} es heterograma')
if is_pangrama(string):
    print(f'{string} es pangrama')
if is_isograma(string):
    print(f'{string} es isograma')
else:
    print('No es heterograma, isograma ni pangrama')
