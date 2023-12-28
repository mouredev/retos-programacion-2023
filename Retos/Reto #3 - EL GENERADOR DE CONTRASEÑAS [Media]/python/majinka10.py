from random import randrange

def passgenerator(longitud=8,conMayusculas=False, conNumeros=False, conSimbolos=False):
    minusculas='abcdefghijklmnopqrst'
    mayusculas=minusculas.upper()
    numeros='1234567890'
    simbolos=' !"#$%&)(*+,-./:;<=>?@[\]^_`{|}~'
    password=''
    longitud_obligatoria = 8 if longitud < 8 else 16 if longitud > 16 else longitud
    while len(password)!= longitud_obligatoria:
        caracterSelector=randrange(0,4,1) # 0 para minusculas, 1 para mayuscula, 2 para numero, 3 para simbolo
        if caracterSelector==1 and conMayusculas:
            password+=mayusculas[randrange(len(mayusculas))]
        elif caracterSelector==2 and conNumeros:
            password+=numeros[randrange(len(numeros))]
        elif caracterSelector==3 and conSimbolos:
            password+=simbolos[randrange(len(simbolos))]
        elif caracterSelector==0:
            password+=minusculas[randrange(len(minusculas))]
    print(password)
    
passgenerator()




