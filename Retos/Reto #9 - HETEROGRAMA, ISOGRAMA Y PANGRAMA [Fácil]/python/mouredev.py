import re
from unidecode import unidecode


def __char_counter(text: str) -> dict[str, int]:

    no_number_text = re.sub(r"\d+", "", text.lower().replace(" ", ""))
    no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)

    # Obtenemos el unicode pero preservando la ñ
    unicode = unidecode(no_punt_text.replace("ñ", ".")).replace(".", "ñ")

    char_counter = dict()

    for char in unicode:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return char_counter


def isHeterogram(text: str) -> bool:
    for counter in __char_counter(text).values():
        if counter > 1:
            return False

    return True


def isIsogram(text: str) -> bool:
    order = 0
    for counter in __char_counter(text).values():
        if order is 0:
            order = counter
        if order is not counter:
            return False

    return True


def isPangram(text: str) -> bool:
    return len(__char_counter(text).keys()) is 27


print(isHeterogram("hiperblanduzcos"))
print(isHeterogram("hiperblanduzcós    !!w"))
print(isIsogram("anna"))
print(isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"))
