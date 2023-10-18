texto = "Este es un ejemplo. En este texto, vamos a contar palabras y oraciones. ¡Espero que funcione!"

numero_palabras = 0
longitud_total_palabras = 0
numero_oraciones = 0
palabra_mas_larga = ""

# Bandera para seguir el estado de una palabra
dentro_de_palabra = False

# Variable para almacenar temporalmente una palabra
palabra_actual = ""

# Recorremos el texto caracter por caracter
for caracter in texto:
    # Si el caracter es una letra o un guión (para palabras compuestas), lo agregamos a la palabra actual
    if caracter.isalpha() or caracter == "-":
        palabra_actual += caracter
        dentro_de_palabra = True
    else:
        # Si estamos dentro de una palabra y encontramos un separador, incrementamos el contador de palabras
        if dentro_de_palabra:
            numero_palabras += 1
            longitud_total_palabras += len(palabra_actual)
            
            # Comprobamos si esta palabra es la más larga hasta ahora
            if len(palabra_actual) > len(palabra_mas_larga):
                palabra_mas_larga = palabra_actual
            
            palabra_actual = ""
            dentro_de_palabra = False
    
    # Si el caracter es un punto, incrementamos el contador de oraciones
    if caracter == ".":
        numero_oraciones += 1

# Verificamos la última palabra si el texto no termina con un separador
if dentro_de_palabra:
    numero_palabras += 1
    longitud_total_palabras += len(palabra_actual)
    if len(palabra_actual) > len(palabra_mas_larga):
        palabra_mas_larga = palabra_actual

# Calculamos la longitud media de las palabras
longitud_media_palabras = longitud_total_palabras / numero_palabras if numero_palabras > 0 else 0


print("Número total de palabras:", numero_palabras)
print("Longitud media de las palabras:", longitud_media_palabras)
print("Número de oraciones:", numero_oraciones)
print("Palabra más larga:", palabra_mas_larga)
