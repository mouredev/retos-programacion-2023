"""
Exercise
"""


def is_heterogram(texto):
    """Verify if the text is a heterogram (without repeated letters)."""
    texto = texto.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    letras = set()
    for char in texto:
        if char.isalpha():
            if char in letras:
                return False
            letras.add(char)
    return True


def is_isogram(texto):
    """Verify if the text is an isogram (without repeated letters)."""
    texto = texto.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    letras = set()
    for char in texto:
        if char.isalpha():
            if char in letras:
                return False
            letras.add(char)
    return True


def is_pangram(texto, alfabeto="abcdefghijklmnopqrstuvwxyz"):
    """Verify if the text is a pangram (contains all the alphabet letters)."""
    texto = texto.lower()
    letras_texto = set([char for char in texto if char in alfabeto])
    return len(letras_texto) == len(alfabeto)


if __name__ == "__main__":
    texto = "The quick brown fox jumps over the lazy dog"
    print(is_pangram(texto))
    texto = "The big fox jumps."
    print(is_isogram(texto))
    texto = "The big dwarf only jumps."
    print(is_heterogram(texto))

