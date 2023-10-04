"""/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */"""

def get_text():
    return input("Texto: ").strip()

def check_text(texto):
    point = 0
    number_words = 0
    max_lenght = ""
    media = 0 
    lista = texto.split(" ")
    lista_filtrada = []
    for word in lista:
        number_words += 1
        if "." in word:
            point +=1
            word = word.replace(".","")
        word = ''.join(char for char in word if char.isalnum())
        if len(word) > len(max_lenght):
            max_lenght = word
        media = media + len(word)
    print(f"El texto tiene {number_words} palabras, la longitud media es {int(media/number_words)}, tiene {point+1} oraciones y la palabra más larga es'{max_lenght}'")
    
def main():
    texto = get_text()
    check_text(texto)
    
if __name__ == "__main__":
    main()