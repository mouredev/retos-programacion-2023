es_dict = {
    "A": "Aurek",
    "B": "Besh",
    "C": "Cresh",
    "D": "Dorn",
    "E": "Esk",
    "F": "Forn",
    "G": "Greer",
    "H": "Herf",
    "I": "Isk",
    "J": "Jenth",
    "K": "Krill",
    "L": "Leth",
    "M": "Mern",
    "N": "Nern",
    "O": "Osk",
    "P": "Peth",
    "Q": "Qek",
    "R": "Resh",
    "S": "Senth",
    "T": "Trill",
    "U": "Usk",
    "V": "Vev",
    "W": "Wesk",
    "X": "Xesh",
    "Y": "Yirt",
    "Z": "Zerek",
    "OO": "Orenth",
    "SH": "Shen",
    "TH": "Thesh",
    "AE": "Enth",
    "EO": "Onith",
    "NG": "Nen",
}

aurebesh_dict = {
    "Aurek": "A",
    "Besh": "B",
    "Cresh": "C",
    "Dorn": "D",
    "Esk": "E",
    "Forn": "F",
    "Greer": "G",
    "Herf": "H",
    "Isk": "I",
    "Jenth": "J",
    "Krill": "K",
    "Leth": "L",
    "Mern": "M",
    "Nern": "N",
    "Osk": "O",
    "Peth": "P",
    "Qek": "Q",
    "Resh": "R",
    "Senth": "S",
    "Trill": "T",
    "Usk": "U",
    "Vev": "V",
    "Wesk": "W",
    "Xesh": "X",
    "Yirt": "Y",
    "Zerek": "Z",
    "Orenth": "OO",
    "Shen": "SH",
    "Thesh": "TH",
    "Enth": "AE",
    "Onith": "EO",
    "Nen": "NG",
}


def aurebesh_2_es(text):
    resultado = ""
    for word in text.split():
        resultado += f"{aurebesh_dict.get(word, word)} "
    return resultado.strip()


def es_2_aurebesh(text):
    resultado = ""
    i = 0
    text = text.upper()
    while i <= len(text) - 1:
        if i + 1 < len(text) and f"{text[i]}{text[i+1]}" in es_dict:
            resultado += f"{es_dict.get(f'{text[i]}{text[i+1]}')} "
            i += 1
        else:
            resultado += f"{es_dict.get(text[i], text[i])} "
        i += 1
    return resultado.strip()


if __name__ == "__main__":
    input_text = input("Ingrese un texto: ")
    lenguaje_raro = es_2_aurebesh(input_text)
    text_nuevamente_en_espanol = aurebesh_2_es(lenguaje_raro)
    print(f"traduccion a aurebesh: {lenguaje_raro}")
    print(f"traduccion a español: {text_nuevamente_en_espanol}")
