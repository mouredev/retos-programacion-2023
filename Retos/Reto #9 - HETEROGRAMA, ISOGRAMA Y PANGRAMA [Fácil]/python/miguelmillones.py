#Crea 3 funciones, cada una encargada de detectar si una cadena de
#texto es un heterograma, un isograma o un pangrama.

TEX=''
abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def heterograma():
    n=1
    count=0
    for i in TEX:
        resp=i in TEX[n:len(TEX)]
        if resp is True:
            count+=1
        n+=1
    if count>0:
        het='no'
    else:
        het='yes'
    return het

def pangrama():
    count=0
    for i in abc:
        resp=i in TEX
        if resp is True:
            count+=1
    if count==27:
        pan='yes'
    else:
        pan='no'
    return pan

def isograma():
    n=1
    count=0
    for i in TEX:
        resp=i in TEX[n:len(TEX)]
        if resp is True:
            count+=1
        n+=1
    if count>0:
        iso='yes'
    else:
        iso='no'
    return iso

TEX=input("Ingrese cadena de texto a evaluar: ").upper()
HET=heterograma()
PAN=pangrama()
ISO=isograma()
if HET == 'yes':
    print("La cadena de texto es heterograma")
else:
    print("La cadena de texto no es heterograma")

if PAN == 'yes':
    print("La cadena de texto es pangrama")
else:
    print("La cadena de texto no es pangrama")

if ISO == 'yes':
    print("La cadena de texto es isograma")
else:
    print("La cadena de texto no es isograma")
