def traducir_aurebesh(texto):
    aurebesh = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
        "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
        "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"
    }

    texto_traducido = ''
    for caracter in texto:
        if caracter.lower() in aurebesh:
            texto_traducido += aurebesh[caracter.lower()]
        else:
            texto_traducido += caracter

    return texto_traducido


# Ejemplo de uso
texto_original = "Hola Moure, ¿cómo estás? me estoy poniendo al corriente con los retos de programación me habia quedado en el 8"

texto_traducido = traducir_aurebesh(texto_original)
print("Texto traducido:", texto_traducido)
