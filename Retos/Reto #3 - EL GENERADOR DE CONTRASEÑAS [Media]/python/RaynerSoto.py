import random
def generador_password(elementos,letras,simbolos,numbers):
    valor = []
    while len(valor) <= elementos:
        numero = random.randint(0,2000000000000000000000000)
        if numero % 3 == 0:
            letra = generador_letras()
            if letras == True:
                numero = random.randint(0,2000000000000000000000000)
                if numero % 2 == 0:
                    letra = str(letra).lower()
            valor.append(letra)
        elif numero % 3 == 1 and simbolos == True:
            simbol = generador_simbolos()
            valor.append(simbol)
        elif numero % 3 == 2 and numbers == True:
            number = generador_numeros()
            valor.append(number)
    value = ''.join(valor)
    return value
def generador_letras():
    letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    valor = random.randrange(0,26)
    return letras[valor]
def generador_simbolos():
    simbolos = ('!','#','$','%','&','/','(',')','=','?','¿','¡','´','¨','*','~','[',']','^',';',',','.',':','<','>','|','°','¬')
    valor = random.randrange(0,len(simbolos))
    return simbolos[valor]

def generador_numeros():
    return str(random.randint(0,10))

print(generador_password(16,True,False,False))