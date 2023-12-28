"""
Reto #19: ANÁLISIS DE TEXTO
MEDIA | Publicación: 11/05/23 | Resolución: 15/05/23
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
"""


def analice_text(text):
    
    num_sentences = text.count(".")
    list = text.split()
    num_word  = len(list)
    
    my_dict = { word : len(word) for word in list}
    ave_length = round(sum(my_dict.values()) / len(my_dict.values()), 2)

    key_max_len = max(my_dict, key=my_dict.get)
    print(my_dict)




    return num_sentences, num_word, ave_length, key_max_len





text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam volutpat, velit a aliquam cursus, justo turpis viverra libero, ac fringilla lectus justo nec turpis. Sed non ligula nec elit hendrerit laoreet. Suspendisses nec rhoncus libero. Maecenas a neque quis ipsum commodo vestibulum. Fusce consectetur urna at est ultrices, a posuere orci commodo. Vestibulum vel justo a justo tristique accumsan. Proin efficitur nisi quis metus luctus, in hendrerit lectus fermentum. Nullam sagittis, nisl vel tincidunt tristique, eros lacus tincidunt elit, vel consequat justo sapien vel eros. In hac habitasse platea dictumst. Vivamus fringilla metus ac ante varius, vel lacinia mi tincidunt. Curabitur accumsan, ex ut hendrerit semper, orci tortor volutpat ligula, sit amet blandit metus urna at tellus. Curabitur in vehicula enim. Nullam sit amet lacinia odio."

a, b, c, d = analice_text(text)
print(f"\nLa cantidad de oraciones es: {a}")
print(f"\nEl numero de palabras es: {b}")
print(f"\nLa longitud media de las palabras es: {c}")
print(f"\nLa palabra mas larga es : {d}")