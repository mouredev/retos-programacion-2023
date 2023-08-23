"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras. [x]
 * - Longitud media de las palabras. [x]
 * - Número de oraciones del texto (cada vez que aparecen un punto). [x]
 * - Encuentre la palabra más larga. [x]
 *
 * Todo esto utilizando un único bucle.
"""

def text_analyzer(text):
    palabras_total = 0 
    numero_oraciones_del_texto = 0
    palabra_mas_larga = ""
    palabra_actual = ""
    cantidad_letras_palabra_actual = 0
    cantidad_letras_palabra_larga = 0
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    characters = 0
    
    for i in text:
        # Total words
        if i in letters:
            characters += 1
        elif i == " ":
            palabras_total += 1 
        #  Text sentence length
        if i == '.':
            numero_oraciones_del_texto += 1
        # Long word
        if i in letters:
            palabra_actual += i 
            cantidad_letras_palabra_actual += 1
            if cantidad_letras_palabra_actual > cantidad_letras_palabra_larga:
                palabra_mas_larga = palabra_actual
                cantidad_letras_palabra_larga = cantidad_letras_palabra_actual
        else:
            if i == " ":
                palabra_actual = ''
                cantidad_letras_palabra_actual = 0
        
    # Total words 2  
    if (text[-1] in letters or text[-1] == "."):
        palabras_total += 1
        
    print(f'El numero total de palabras es: {palabras_total}')
    print(f'Longitud media de las palabras: {characters / palabras_total}')
    print(f'Número de oraciones del texto: {numero_oraciones_del_texto}')
    print(f'Encuentre la palabra más larga: {palabra_mas_larga}')
    
    
texto = input('Pone el texto: ') 
print(texto)
prueba1 = text_analyzer(texto)