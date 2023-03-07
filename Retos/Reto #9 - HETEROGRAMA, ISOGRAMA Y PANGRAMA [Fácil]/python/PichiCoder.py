import string

def heterograma(palabra) -> bool:
    """
    Args:
        palabra (string)
    Use:
    Detecta si la cadena es heterograma. Esto es una palabra o 
    frase que no contiene ninguna letra repetida.
    """
    test = ""
    for i in palabra:
        if i == " ": continue
        if i not in test: test += i
        else: return False
    return True

def isograma(palabra) -> bool:
    """
    Args:
        palabra (string)
    Use:
    Detecta si la cadena es isograma. Esto es una palabra o frase 
    en la que cada letra aparece el mismo número de veces. 
    """
    test = ""
    for i in palabra:
        if i == " ": continue
        if i not in test: test += i
        
    counts = palabra.count(test[0])

    for l in test:
        if palabra.count(l) != counts:
            return False
    return True

def pangrama(frase) -> bool:
    """
    Args:
        frase (string)
    Use:
    Detecta si la cadena es un pangrama. Esto es una frase 
    en la que aparecen todas las letras del abecedario.
    """
    for i in string.ascii_lowercase:
        if i not in frase.lower(): return False
    return True
