import string

def is_heterograma(texto: str) -> bool:
    for i in texto:
        if i == " " or i.isdigit():
            continue

        i = (
            i.lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .replace("ü", "u")
        )

        if texto.count(i) > 1:
            return False
    return True

def is_isograma(texto: str) -> bool:
    conteos = set()
    for i in texto:
        if i == " " or i.isdigit():
            continue
        if texto.count(i) > 1:
            conteos.add(texto.count(i))
    return len(conteos) == 1

def is_pangrama(texto: str) -> bool:
    base = string.ascii_lowercase + "ñ"

    for i in texto:
        i = (
            i.lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .replace("ü", "u")
        )

        base = base.replace(i, "")

    return len(base) == 0

print(is_heterograma(input("Ingrese heterograma: ")))
print(is_isograma(input("Ingrese isograma: ")))
print(is_pangrama(input("Ingrese pangrama: ")))
