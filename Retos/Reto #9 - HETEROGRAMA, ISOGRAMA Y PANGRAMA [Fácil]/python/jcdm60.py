import string


def es_heterograma(palabra):

    # True si la palabra es un heterograma, si no se repiten letras.

    letras = set()
    for letra in palabra:
        if letra.isalpha():
            if letra.lower() in letras:
                return False
            letras.add(letra.lower())
    return True


def es_isograma(palabra):

    # True si la palabra es un isograma, si no se repiten letras pero se pueden repetir otros caracteres.

    letras = set()
    for letra in palabra:
        if letra.isalpha():
            if letra.lower() in letras:
                return False
            letras.add(letra.lower())
    return True


def es_pangrama(palabra):

    # True si la palabra es un pangrama, si contiene todas las letras del alfabeto.

    abecederaio = set(string.ascii_lowercase)
    for letra in palabra:
        if letra.isalpha():
            abecederaio.discard(letra.lower())
    return len(abecederaio) == 0


if __name__ == "__main__":
    print(es_heterograma("centrifugados"))
    print(es_isograma("prueba"))
    print(es_pangrama("abcdefghijklmnñopqrstuvwxyz"))
