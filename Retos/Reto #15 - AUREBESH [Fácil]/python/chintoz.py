spanish_to_aurebek = {
    "a": "aurebek",
    "b": "besh",
    "c": "cresh",
    "ch": "cherek",
    "d": "dorn",
    "e": "esk",
    "ae": "enth",
    "eo": "onith",
    "f": "forn",
    "g": "grek",
    "h": "herf",
    "i": "isk",
    "j": "jenth",
    "k": "krill",
    "kh": "krenth",
    "l": "leth",
    "m": "mern",
    "n": "nern",
    "ng": "nen",
    "o": "osk",
    "oo": "orenth",
    "p": "peth",
    "q": "qek",
    "r": "resh",
    "s": "senth",
    "sh": "shen",
    "t": "trill",
    "th": "thesh",
    "u": "usk",
    "v": "vev",
    "w": "wesk",
    "x": "xesh",
    "y": "yirt",
    "z": "zerek"
}

aurebek_to_spanish = {v: k for k, v in spanish_to_aurebek.items()}


def matches(substring, dictionary):
    inner_matches = []
    for key in dictionary:
        if str(key).startswith(substring):
            inner_matches.append(key)
    return inner_matches


def translate(input_text, dictionary):
    translated_text = ""
    prev_matches = []
    prev_current = ""
    for character in input_text:
        if not character.isalpha():
            if prev_current == "":
                translated_text = translated_text + character
            else:
                translated_text = translated_text + dictionary[prev_current] + character
            prev_matches = []
            prev_current = ""
            continue
        current = prev_current + character
        new_matches = matches(current, dictionary)
        if len(new_matches) == 1:
            if current not in dictionary:
                prev_current = current
                prev_matches = new_matches
                continue
            translated_text = translated_text + dictionary[current]
            prev_matches = []
            prev_current = ""
        if len(new_matches) > 1:
            prev_matches = new_matches
            prev_current = current
        if len(new_matches) == 0 and len(prev_matches) > 0:
            translated_text = translated_text + dictionary[prev_current]
            prev_current = character
            prev_matches = matches(prev_current, dictionary)

    if prev_current != "":
        translated_text = translated_text + dictionary[prev_current]

    return translated_text


if __name__ == '__main__':

    inputText = input("Introduce el texto que quieras traducir: ").lower()
    direction = int(input("Cómo quieres traducir el texto 1: Español -> Aurebesh, 2: Aurebesh -> Español: "))
    if direction != 1 and direction != 2:
        print("Opción de lenguaje seleccionada incorrecta")
        exit(0)

    if direction == 1:
        selected_dictionary = spanish_to_aurebek
    else:
        selected_dictionary = aurebek_to_spanish

    print(translate(inputText, selected_dictionary))
