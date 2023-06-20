def heterograma(st):
    letras=[]
    for j in st:
        if not(j in letras):
            letras.append(j)
    if letras==list(st):
        return "es heterograma"
    else:
        return "no es heterograma"

def isograma(st):
    lista=list(st)
    retu=True
    for i in range (len(lista)):
        if lista.count(lista[i])!=lista.count(lista[i-1]):
            retu=False
            break
    if retu:
        return "Es un isograma"
    else:
        return "No es un isograma"

def pangrama(st):
    letrasAlfa="abcdefghijklmnopqrstuvwxyz"
    letras=list(letrasAlfa)
    if set(letras)==set(list(st)):
        return "es un pangrama"
    else: 
        return "no es un pangrama"

if __name__ == "__main__":
    palabra1=input()
    palabra=palabra1.replace(" ", "", palabra1.count(" "))
    print()
    print("La palabra ingresada: "+isograma(palabra)+ ", "+heterograma(palabra)+ " y "+pangrama(palabra))

