"""
Crea un programa que analice texto y obtenga:
- Número total de palabras.
- Longitud media de las palabras.
- Número de oraciones del texto (cada vez que aparecen un punto).
- Encuentre la palabra más larga.

Todo esto utilizando un único bucle.
"""

import re

def text_analyzer(text: str) -> tuple[int,float,int,list[str]]:
    """
    Analiza un texto y obtiene estadísticas básicas.

    Calcula los siguientes indicadores:
        - Número total de palabras.
        - Longitud media de las palabras.
        - Número de oraciones (cada vez que aparece un punto).
        - Palabra más larga encontrada.

    Todo el análisis se realiza utilizando un único bucle.

    Args:
        text (str): Texto de entrada a analizar.

    Returns:
        tuple[int, float, int, str]: Una tupla con:
            - int: Total de palabras.
            - float: Longitud media de las palabras.
            - int: Número de oraciones.
            - str: Palabra más larga.

    Raises:
        TypeError: Si el argumento proporcionado no es una cadena.
        ValueError: Si el texto está vacío.
    """
    if not isinstance(text, str):
        raise TypeError("El argumento debe ser una cadena de texto.")
    if not text:
        raise ValueError("El texto no puede estar vacío.")

    clean_text = re.sub(r"[^a-zA-Z0-9\s.]", "", text)
    count_words = 0
    media = 0
    count_sentences = 0
    largest_word = []

    total_words = clean_text.strip().split()
    count_words = len(total_words)

    total_char = 0
    for word in total_words:
        if word.endswith('.'):
            count_sentences += 1
            word = word[:-1]
        if len(largest_word) == 0 or len(word) == len(largest_word[0]):
            largest_word.append(word)
        elif len(word) > len(largest_word[0]):
            largest_word.clear()
            largest_word.append(word)
        if word == total_words[-1]:
            count_sentences += 1
        total_char += len(word)

    media = total_char / count_words

    return (count_words, media, count_sentences, largest_word)


if __name__ == "__main__":
    text = "uno dos tres. cuatro cinco seis. siete ocho nueve diez."
    results = text_analyzer(text)
    print(f"Total de palabras: {results[0]}\nLongitud media de las palabras: {results[1]}")
    print(f"Numero de oraciones: {results[2]}\nPalabra mas larga: {results[3]}")
