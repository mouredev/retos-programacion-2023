#Primero defino el alfabeto ocn un diccionario, así a cada letra le corresponde una palabra en Aurebesh
español = {
    'a': 'Aurek',
    'b': 'Besh',
    'c': 'Cresh',
    'd': 'Dorn',
    'e': 'Esk',
    'f': 'Forn',
    'g': 'Grek',
    'h': 'Herf',
    'i': 'Isk',
    'j': 'Jenth',
    'k': 'Krill',
    'l': 'Leth',
    'm': 'Mern',
    'n': 'Nern',
    'ñ': 'eñe',
    'o': 'Osk',
    'p': 'Peth',
    'q': 'Qek',
    'r': 'Resh',
    's': 'Senth',
    't': 'Trill',
    'u': 'Usk',
    'v': 'Vev',
    'w': 'Wesk',
    'x': 'Xesh',
    'y': 'Yirt',
    'z': 'Zerek',
    'ch': 'Cherek',
    'eo': 'Onith',
    'ng': 'Nen',
    'oo': 'Orenth',
}

#De esta manera inviero el diccionario anterior, las claves pasan a ser los valores y viceversa
aurebesh = {valor.lower(): clave for clave, valor in español.items()}

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

def traductor(original, texto):

    texto_traducido=''
    texto=normalize(texto).lower()

    if original == 'Español':

        contador=0
        
        while contador<len(texto):

            solo_caracter=texto[contador]

            if solo_caracter not in español:
                    texto_traducido+=solo_caracter
                    contador+=1

            elif contador<(len(texto)-1):

                doble_caracter=solo_caracter+texto[contador+1]

                if doble_caracter in español:
                    texto_traducido+=español[doble_caracter].lower()
                    contador+=2

                elif solo_caracter in español:
                    texto_traducido+=español[solo_caracter].lower()
                    contador+=1

            elif solo_caracter in español:
                    texto_traducido+=español[solo_caracter].lower()
                    contador+=1

    elif original=='Aurebesh':

        texto_traducido=texto

        for key, value in aurebesh.items():
            texto_traducido=texto_traducido.replace(key,value)

    return texto_traducido.capitalize()
            
a= traductor('Español', 'Qué buen reto. Nos vemos mañana!')
print(a)
print(traductor('Aurebesh',a))