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
    for letra, cantidad in contar_letras(frase).items():
        if cantidad>1:
            return 'La cadena de texto no es heterograma'
        else:
            return 'La cadena de texto es heterograma'
        
def isograma(frase):
    for letra, cantidad in contar_letras(frase).items():
        if cantidad>1:
            return 'La cadena de texto es un isograma'
        else:
            return 'La cadena de texto no es un isograma'
        
def pangrama(frase):
     for letra, cantidad in contar_letras(frase).items():
        if cantidad>=1:
            return 'La cadena de texto es un pangrama'
        else: 
            return 'La cadena de texto no es un pangrama'


print(isograma('caminantes nocturnos'))
print(heterograma('Centrifugadlos'))
print(pangrama('Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.'))

