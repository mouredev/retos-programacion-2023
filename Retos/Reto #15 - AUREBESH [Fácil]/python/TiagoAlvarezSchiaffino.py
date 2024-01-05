from unidecode import unidecode

def aurebesh_translator(text: str, to_aurebesh: bool) -> str:
    """
    Translate text between Spanish and Aurebesh.

    Args:
        text (str): The text to be translated.
        to_aurebesh (bool): If True, translates from Spanish to Aurebesh; otherwise, translates from Aurebesh to Spanish.

    Returns:
        str: The translated text.
    """
    basic_alphabet = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
        "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
        "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"
    }

    basic_to_aurebesh = {v: k for k, v in basic_alphabet.items()}

    unidecode_text = unidecode(text.lower().replace("ñ", "[?]")).replace("[?]", "ñ")
    translated_text = ""

    if to_aurebesh:
        for key, value in basic_alphabet.items():
            text = text.replace(key, value)
    else:
        character_index = 0
        text_len = len(text)
        while character_index < text_len:
            simple_character = unidecode_text[character_index]
            double_character = ""
            if character_index < text_len - 1:
                double_character = simple_character + unidecode_text[character_index + 1]
            if double_character in basic_to_aurebesh:
                translated_text += basic_to_aurebesh[double_character]
                character_index += 2
            else:
                translated_text += basic_alphabet[simple_character] if simple_character in basic_alphabet else simple_character
                character_index += 1        

    return translated_text

# Examples
spanish_text = "Hola, ¿cómo estás?"
aurebesh_translation = aurebesh_translator(spanish_text, to_aurebesh=True)
spanish_translation = aurebesh_translator(aurebesh_translation, to_aurebesh=False)

print(f"Original text: {spanish_text}")
print(f"Aurebesh translation: {aurebesh_translation}")
print(f"Spanish translation: {spanish_translation}")
