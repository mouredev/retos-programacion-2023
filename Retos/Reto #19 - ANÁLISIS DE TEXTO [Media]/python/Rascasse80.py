texto = input("Introduce un texto: ")

lista_palabras = texto.replace(".", "").split(" ")

suma_longitudes = 0
for palabra in lista_palabras:
    suma_longitudes += len(palabra)

longitud_media = suma_longitudes / len(lista_palabras)

print(f"El número total de palabras es {len(lista_palabras)}")
print(f"La longitud media de las palabras es: {longitud_media}")
if texto.endswith("."):
    print(f"El número total de oraciones es {texto.count('.')}")
else:
    print(f"El número total de oraciones es {texto.count('.')+1}")
print(f"La palabra más larga es: {max(lista_palabras, key=len)}")