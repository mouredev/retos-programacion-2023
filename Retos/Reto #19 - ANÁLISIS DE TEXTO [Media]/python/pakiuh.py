"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
"""
longitud_palabra = 0
oracion = 0
longitud_mas_larga = 0


texto = 'Al contrario del pensamiento popular, el texto de Lorem Ipsum no es simplemente texto aleatorio. Tiene sus raices en una pieza cl´sica de la literatura del Latin, que data del año 45 antes de Cristo, haciendo que este adquiera mas de 2000 años de antiguedad. Richard McClintock, un profesor de Latin de la Universidad de Hampden-Sydney en Virginia, encontró una de las palabras más oscuras de la lengua del latín, "consecteur", en un pasaje de Lorem Ipsum, y al seguir leyendo distintos textos del latín, descubrió la fuente indudable. Lorem Ipsum viene de las secciones 1.10.32 y 1.10.33 de "de Finnibus Bonorum et Malorum" (Los Extremos del Bien y El Mal) por Cicero, escrito en el año 45 antes de Cristo. Este libro es un tratado de teoría de éticas, muy popular durante el Renacimiento. La primera linea del Lorem Ipsum, "Lorem ipsum dolor sit amet..", viene de una linea en la sección 1.10.32. El trozo de texto estándar de Lorem Ipsum usado desde el año 1500 es reproducido debajo para aquellos interesados. Las secciones 1.10.32 y 1.10.33 de "de Finibus Bonorum et Malorum" por Cicero son también reproducidas en su forma original exacta, acompañadas por versiones en Inglés de la traducción realizada en 1914 por H. Rackham.'

palabras_texto = texto.split()

#print(palabras_texto)

numero_palabras = len(palabras_texto)

for i in range(numero_palabras):
    longitud_palabra += len(palabras_texto[i])
    if palabras_texto[i][-1]==".":
        oracion += 1
    if i>=1 and len(palabras_texto[i])>=len(palabras_texto[i-1]):
        longitud_mas_larga = len(palabras_texto[i])
        palabra_mas_larga = palabras_texto[i]

longitud_media = longitud_palabra / numero_palabras

print (f"El numero total de palabras del texto es: {numero_palabras}")
print(f"La longitud media de las palabras es: {round(longitud_media,2)} letras")
print (f"La cantidad de oraciones en el texto son: {oracion}")
print(f"El número de letras de la palabra más larga es: {longitud_mas_larga} y es: '{palabra_mas_larga}'")
