"""
 * Crea una función que sea capaz de transformar Español al lenguaje básico 
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
"""

basicAlphabet = {
    "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
    "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
    "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
    "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"
}


def translate(text):
    translated_text = ""
    i = 0
    while i < len(text):
        if text[i:i+2] in basicAlphabet:
            translated_text += basicAlphabet[text[i:i+2]]
            i += 2
        else:
            translated_text += basicAlphabet.get(text[i].lower(), text[i])
            i += 1
    return translated_text


print(translate("Brais"))
print(translate("Mouredev"))
