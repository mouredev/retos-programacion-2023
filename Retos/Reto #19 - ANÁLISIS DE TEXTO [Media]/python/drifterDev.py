def analisis_texto(texto):

    numero_palabras=0
    longitud_media=0
    numero_oraciones=0
    palabra_mas_larga=""
    longitudes_totales=0

    for palabra in list(texto.split()):
        numero_palabras+=1
        if palabra[-1]==".":
            numero_oraciones+=1
            palabra=palabra.rstrip(".")
        palabra = palabra.strip("¡¿(,;?!):")
        longitudes_totales+=len(palabra)
        if len(palabra)>len(palabra_mas_larga):
            palabra_mas_larga=palabra
        
    longitud_media=longitudes_totales/numero_palabras

    print("Texto analizado.")
    print(f"Número de palabras: {numero_palabras}")
    print(f"Longitud media de las palabras: {round(longitud_media,2)}")
    print(f"Número de oraciones: {numero_oraciones}")
    print(f"Palabra más larga: '{palabra_mas_larga}'")

if __name__=="__main__":
    texto="""
    Crea un programa que analice texto y obtenga:
    Número total de palabras.
    Longitud media de las palabras.
    Número de oraciones del texto (cada vez que aparecen un punto).
    Encuentre la palabra más larga.

    Todo esto utilizando un único bucle.
    """
    analisis_texto(texto)
