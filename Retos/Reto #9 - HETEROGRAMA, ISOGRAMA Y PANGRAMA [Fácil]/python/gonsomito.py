"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""
def heterograma(cadena):                    #es una palabra o frase que no contiene ninguna letra repetida
    frase_en_modo_dict=recuento(cadena)
    for grama in frase_en_modo_dict:        #para cada letra compruebo que no se repita
        if frase_en_modo_dict[grama] > 1:   #si hay más de 1 es que se repite ;) y se sale.
            return
    print("Es un heterograma.")
        
def isograma(cadena):                       #es una palabra o frase en la que cada letra aparece el mismo número de veces.
    frase_en_modo_dict=recuento(cadena)     
    veces=max(frase_en_modo_dict.values())  #busco el valor máximo y compruebo que se repita igual numero de veces y más de 1 vez.
    for grama in frase_en_modo_dict:
        if frase_en_modo_dict[grama] < veces or frase_en_modo_dict[grama] == 1:
            return
    print("Es un isograma.")

def pangrama(cadena):                   #es una frase en la que aparecen todas las letras del abecedario.
    if len(recuento(cadena)) == 27:        
        print("Es un pangrama.")        #en el abecedario español hay 27 letras. Esto es, si tengo 27 elementos es pangrama ;)

        
def recuento(cadena_a_comprobar):       #con esta función compuebo que caracteres hay y cuantas veces
    contador_letras={}
    for c in cadena_a_comprobar:
        if c in contador_letras:
            contador_letras[c]=contador_letras[c]+1
        else:
            contador_letras[c]=1
    return contador_letras              #y lo devuelvo como diccionario
  

def limpia_botas(text):                 #esta función quita espacios en blanco, símbolos y tildes
    text=text.lower()                   #es un poquito chapucera, pero tampoco domino tanto python.
    text="".join(letra for letra in text if not letra.isdigit())          #limpieza de números
    text=text.replace(" ","")
    text=text.replace(",","")
    text=text.replace(".","")
    text=text.replace("?","")
    text=text.replace("!","")
    text=text.replace("¿","")
    text=text.replace("¡","")
    text=text.replace(";","")
    text=text.replace(":","")
    text=text.replace("á","a")
    text=text.replace("é","e")
    text=text.replace("í","i")
    text=text.replace("ó","o")
    text=text.replace("ú","u")
    text=text.replace("ü","u")
    #print(text)
    return text

cadena=input("Que frase vamos a comprobar")             #guardemos la cadena en minúsculas para limpiarla de espacios y tildes y signos de puntuacion
                      
heterograma(limpia_botas(cadena))
isograma(limpia_botas(cadena))
pangrama(limpia_botas(cadena))
