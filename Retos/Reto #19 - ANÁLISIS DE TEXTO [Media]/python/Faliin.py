texto = input("Ingresa un texto: ")


num_palabras = 0
longitud_total = 0
num_oraciones = 0
palabra_mas_larga = ""

palabras = texto.strip().split()

for palabra in palabras:

    num_palabras += 1

    
    longitud_total += len(palabra)

    
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

    
    if palabra.endswith('.'):
        num_oraciones += 1


longitud_media = longitud_total / num_palabras if num_palabras > 0 else 0


print("Número total de palabras:", num_palabras)
print("Longitud media de las palabras:", longitud_media)
print("Número de oraciones:", num_oraciones)
print("Palabra más larga:", palabra_mas_larga)
