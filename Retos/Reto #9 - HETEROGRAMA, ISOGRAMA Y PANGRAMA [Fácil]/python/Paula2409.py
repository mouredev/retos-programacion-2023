"""
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
"""
import string 

def evaluate_text():
    """
    The function evaluates whether a given text is a heterogram, isogram, or pangram based on the
    occurrence of letters in the text.
        
    Args:
        text (str): any text given by user

    Returns:
        str: returns if the text is a heterogram, an isogram and a pangram.
    """    
    # Input a word or phrase   
    text = input("Ingrese un texto o palabra para evaluar: ")
    # Process the input
    new_text = text.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace(' ', '')
    simbols = string.punctuation

    letters_present = {}

    for char in new_text:
        if char in simbols:
            new_text = new_text.replace(char, "")
        else:
            if char in letters_present:
                letters_present[char] += 1
            else:
                letters_present[char] = 1

    values = list(letters_present.values())
    
    def is_heterogram():
        # Heterogram: is a word, phrase or sentence in which no letter of the alphabet occurs more than once.
        if len(set(values)) == 1:
            return f"The text '{text}' is a heterogram"
        else:
            return f"The text '{text}' is not a heterogram"


    def is_isogram():
        # Isogram: word or phrase in which each letter occurs the same number of times.
        for value in values:
            if value != values[0]:
                return f"The text '{text}' is an Isogram"
        return f"The text '{text}' is not an Isogram"

    def is_pangrama():
        # Pangrama: word, phrase or sentence in which all letters of the alphabet are present.
        letters = list(string.ascii_lowercase) + ['ñ']
        for letter in letters:
            if letter in text:
                letters.remove(letter)
        if len(letters) == 0:
            return f"The text '{text}' is a pangram"
        else:
            return f"The text '{text}' is not a pangram"
        
    print(is_heterogram())
    print(is_isogram())
    print(is_pangrama())

evaluate_text()
