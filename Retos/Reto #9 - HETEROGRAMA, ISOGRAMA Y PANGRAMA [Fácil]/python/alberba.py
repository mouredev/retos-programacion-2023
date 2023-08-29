import string

def is_heterograma(text: str) -> bool:
    uses = dict()
    text = text.strip().lower()
    for letra in text:
        if uses.get(letra, 0) == 0:
            uses[letra] = 1
        else:
            return False
    return True
    
def is_isograma(text: str) -> bool:
    uses = dict()
    text = text.strip().lower()
    for letra in text:
        uses_ultima_letra = uses.get(letra, 0) + 1
        uses[letra] = uses_ultima_letra

    for letra in uses.items():
        if letra[1] != uses_ultima_letra:
            return False
    
    return True

def is_pangrama(text:str) -> bool:
    alphabet = list(string.ascii_lowercase)
    text = text.strip().lower()
    for letra in text:
        if letra in alphabet:
            alphabet.remove(letra)
    return len(alphabet) == 0

print(is_heterograma("hiperblanduzcos"))
print(is_heterograma("hiperblanduzcós    !!w"))
print(is_isograma("anna"))
print(is_pangrama("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"))