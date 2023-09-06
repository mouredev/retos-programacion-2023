palabra = "murcielago"
respuesta = ""

def heterograma(palabra):
    pos = 0
    for i in palabra:
        pos+=1
        for j in palabra[pos:]:
            if i == j:
                return False
    return True


def isograma(palabra):
    minimo = palabra.count(palabra[0])
    for i in palabra[1:]:
        if palabra.count(i) != minimo:
            return False
    return True

def pangrama(palabra):
    abc = "abcdefghijklmnñopqrstuvwxyz"
    if len(palabra) < 27:
        return False
    else:
        for i in abc:
            if i not in palabra:
                return False
                break
        else:
            return True

if heterograma(palabra):
    respuesta += "Es un heterograma"
else:
    respuesta += "No es un heterograma"

if isograma(palabra):
    respuesta += ", un isograma"
else:
    respuesta += ",no es un isograma"

if pangrama(palabra):
    respuesta += " y un pangrama"
else: 
    respuesta += " y no es un pangrama"

print(respuesta)