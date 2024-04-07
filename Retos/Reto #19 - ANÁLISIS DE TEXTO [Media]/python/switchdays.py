"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 """

input_text = input("Introduce un texto (Asegúrese de que el texto finaliza con un punto): ")

def analyzer(text):

    words = text.split() # Convertimos el texto en una lista de strings, en la que cada palabra es un string diferente.
    total_words = 0
    total_char = 0
    total_sentences = 0
    most_long = max(words, key=len)
    invalid_char = ("(", ")", ",", "!", "-", "_", ":", ";", "/", "?", "¿", "+", '"') # Caracteres que la función no tendrá en cuenta.

    for char in text:

        if char not in invalid_char:
            total_char +=1

            if char == " ":
                total_words += 1
                total_char -=1
            elif char == ".":
                total_words += 1
                total_char -=1
                total_sentences += 1

    print("Total palabras:", total_words)
    print("La longitud media de las palabras es: ", total_char/total_words)
    print("El número total de oraciones es :", total_sentences)
    print("La palabra mas larga es: ", most_long)

analyzer(input_text)