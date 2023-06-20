from unidecode import unidecode

def basic_aurebesh_tranlator(text: str, aurebesh: bool) -> str:

    basic_alphabet = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
        "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
        "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"}

    aurebesh_alphabet = dict()
    for key, value in basic_alphabet.items():
        aurebesh_alphabet[value] = key    

    unidecode_text = unidecode(text.lower().replace("ñ", "[?]")).replace("[?]", "ñ")
    translated_text = ""

    if aurebesh:

        translated_text = text

        for key, value in aurebesh_alphabet.items():
            translated_text = translated_text.replace(key, value)         

    else:

        character_index = 0
        text_len = len(text)

        while character_index < text_len:

            simple_character = unidecode_text[character_index]
            double_character = ""

            if character_index < text_len - 1:
                double_character = simple_character + unidecode_text[character_index + 1]

            if double_character in basic_alphabet:
                translated_text += basic_alphabet[double_character]
                character_index += 2
            else:
                translated_text += basic_alphabet[simple_character] if simple_character in basic_alphabet else simple_character
                character_index += 1        

    return translated_text

aurebesh = basic_aurebesh_tranlator("The MoureDev", False)
print(aurebesh)
basic = basic_aurebesh_tranlator(aurebesh, True)
print(basic)

aurebesh = basic_aurebesh_tranlator("Qué te ha parecido el reto? A mí me ha gustado mucho! Mañana sigue practicando.", False)
print(aurebesh)
basic = basic_aurebesh_tranlator(aurebesh, True)
print(basic)
