from string import ascii_lowercase


def is_heterograma(text: str) -> bool:
    "Ninguna letra repetida"
    text = text.replace(" ", "").lower()
    chars = {}
    for t in text:
        if t in chars:
            return False
        chars[t] = 0
    return True


def is_isograma(text: str) -> bool:
    "Las letras aparecen el mismo numero de veces"
    text = text.replace(" ", "").lower()
    chars = {}
    for t in text:
        if not t in chars:
            chars[t] = 0
        chars[t] += 1
    value = list(chars.values())[0]
    for v in chars.values():
        if value != v:
            return False
    return True


def is_pangrama(text: str) -> bool:
    "Aparecen todas las letras del abecedario"
    text = text.replace(" ", "").lower()
    for letter in ascii_lowercase:
        if not letter in text:
            return False
    return True


text = "nononono"
print(is_heterograma(text))
print(is_isograma(text))
print(is_pangrama(text))
