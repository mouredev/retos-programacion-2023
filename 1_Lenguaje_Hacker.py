from typing import Text

def convert_to_leet(text: Text) -> Text:
    """
    Convierte un texto en lenguaje "leet" o "1337".

    Args:
        text (str): El texto a convertir.

    Returns:
        str: El texto convertido a "leet".

    Example:
        >>> convert_to_leet("Hola, mundo!")
        'H0l4, mund0!'
    """
    leet_table = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '6',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2'
    }
    
    converted_text = ""
    
    for char in text:
        converted_text += leet_table.get(char.lower(), char)
    
    return converted_text


if __name__ == "__main__":
    texto = input("Ingrese el texto a convertir a 'leet': ")
    texto_convertido = convert_to_leet(texto)
    print("Texto convertido a 'leet':", texto_convertido)
