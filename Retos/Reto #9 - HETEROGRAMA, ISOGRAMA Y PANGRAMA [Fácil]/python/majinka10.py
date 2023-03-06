def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def contar_letras(frase):
    alfabeto={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'ñ':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,
              'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    frase=normalize(frase.lower())
    for letra in frase:
        if letra in alfabeto:
            alfabeto[(letra)]+=1
        else:
            letra
    return alfabeto

def heterograma(frase):
    es_heterograma=False
    for letra, cantidad in contar_letras(frase).items():
        if cantidad>=1:
            if cantidad==1:
                es_heterograma=True
            elif cantidad!=1:
                es_heterograma=False
                break   
        else:
            letra
    return 'La cadena de texto es un heterograma' if es_heterograma else 'La cadena de texto no es heterograma'
        
def isograma(frase):
    max=0
    es_isograma=False
    for letra, cantidad in contar_letras(frase).items():
        if cantidad>=1:
            max=cantidad
            break
    
    for letra, cantidad in contar_letras(frase).items():
        if cantidad>=1: 
            if cantidad == max:
                es_isograma=True
            elif cantidad!=max:
                es_isograma=False
        else:
            letra
    return 'La cadena de texto es un isograma' if es_isograma else 'La cadena de texto no es un isograma'
        
def pangrama(frase):
    es_pangrama=False
    for letra, cantidad in contar_letras(frase).items():
        if cantidad>=1:
            es_pangrama=True
        else: 
            es_pangrama=False
    return 'La cadena de texto es un pangrama' if es_pangrama else 'La cadena de texto no es un pagrama'

print(isograma('caminantes nocturnos'))
print(isograma('Rara'))
print(heterograma('Centrifugadlos'))
print(heterograma('Hoola'))
print(pangrama('Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.'))
print(pangrama('Hola'))