import random

letras = ['A','a','B','b','C','c','D','d','E','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
simbolos = ['!','#','$','%','&','/','(',')','=','?','¡','¿']

eliminados = []

def generador_password():
    for i in range(5):
        letra_eliminada = letras.pop(random.randint(0, len(letras)-1))
        numero_eliminado = numeros.pop(random.randint(0, len(numeros)-1))
        simbolo_eliminado = simbolos.pop(random.randint(0, len(simbolos)-1))
        eliminados.append(letra_eliminada)
        eliminados.append(simbolo_eliminado)
        eliminados.append(numero_eliminado)

    random.shuffle(eliminados)
    password = ''.join(eliminados)
    return password

password = generador_password()
print(password)