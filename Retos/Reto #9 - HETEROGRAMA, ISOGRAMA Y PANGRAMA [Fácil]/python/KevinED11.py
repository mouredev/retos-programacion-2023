"""
Un heterograma es una palabra que no contiene letras repetidas. Es decir, todas las letras de la palabra son diferentes. 

Un isograma es una palabra o frase en la que todas las letras se repiten el mismo número de veces. Es decir, no hay letras repetidas más veces que otras. 

Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez. 

"""

from string import ascii_lowercase


def is_heterogram(text: str) -> bool:

    text = "".join(text.lower().split())

    if any(text.count(letra) > 1 for letra in text):
        return False

    return True


def is_isogram(text: str) -> bool:

    u_letters = set("".join(text.lower().split()))
    text = "".join(text.lower().split())

    return len(u_letters) == len(text)


def is_pangram(text: str) -> bool:
    text = set("".join(text.lower().split()))

    if "ñ" in text:
        abc = tuple(ascii_lowercase + "ñ")
        return len(text) == len(abc)

    abc = tuple(ascii_lowercase)

    return len(text) == len(abc)


if __name__ == "__main__":
    print(is_heterogram(text="kevin sal"))  # output True

    print(is_isogram(text="kevin sal"))  # output True

    # output True
    print(is_pangram(text="The quick brown fox jumps over the lazy dogñ"))
