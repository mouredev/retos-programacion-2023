#Reto semanal 19
# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
# Todo esto utilizando un único bucle.
# No se tienen en cuenta caracteres especiales, solo el punto.

TotalPalabras = 0
TotalCaracteres = 0
LongitudMedia = 0
NroOraciones = 0
LargoDePalabraLarga = 0
LargoDePalabraActual = 0
PalabraLargaTemporal = ''
PalabraLarga  = "De momento no hay palabra larga"
textoParaAnalizar = input("Ingrese el texto que desea analizar: ")

caracterAnterior = ' '
for caracter in textoParaAnalizar:
    if caracter.isalpha() or caracter == ' ' or caracter == '.':
        if caracterAnterior == ' ' and caracter != ' ':
            TotalPalabras +=1
            if LargoDePalabraActual > LargoDePalabraLarga:
                PalabraLarga = PalabraLargaTemporal
                LargoDePalabraLarga = LargoDePalabraActual
            LargoDePalabraActual = 0
            PalabraLargaTemporal = ''
        if caracter != ' ':
            TotalCaracteres +=1
        if caracterAnterior != '.' and caracter == '.':
            NroOraciones += 1
        if caracter != ' ' and caracter != '.':
            PalabraLargaTemporal += caracter
            LargoDePalabraActual += 1
    caracterAnterior = caracter

if TotalPalabras > 0:
    LongitudMedia = round(TotalCaracteres / TotalPalabras)

print('Este es el análisis de su texto: ')
print(f'Número total de palabras: {TotalPalabras}')
print(f'Longitud media de las palabra: {LongitudMedia}')
print(f'Número de oraciones: {NroOraciones}')
print(f'Palabra más larga: {PalabraLarga}')