# Reto #15: Aurebesh
#### Dificultad: Fácil | Publicación: 10/04/23 | Corrección: 17/04/23
## Enunciado

"""
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
"""

#diccionario de Español a Aurebesh
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
#diccionario de Aurebesh a Español
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
    #recorre el listado de palabras presentes en el texto, palabras por palabras
    for word in text.split():
        resultado += f"{aurebesh_dict.get(word, word)}"      
    return resultado.strip()

def es_2_aurebesh(text):
    resultado = ""
    i = 0
    text = text.upper()
    while i <= len(text) - 1:
        #valida que sea un par de letras presentes en el diccionario
        if i + 1 < len(text) and f"{text[i]}{text[i+1]}" in es_dict:
            resultado += f"{es_dict.get(f'{text[i]}{text[i+1]}')} "
            i += 1
        #caso para una letra presente en el diccionario
        else:
            resultado += f"{es_dict.get(text[i], text[i])} "
        i += 1
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    aurebesh = es_2_aurebesh(texto)
    texto_retraducido = aurebesh_2_es(aurebesh)
    print(f"Traduccion a Aurebesh: {aurebesh}")
    print(f"Traduccion a Español: {texto_retraducido}")
    print(es_2_aurebesh("Gracias Brais"))
    print(aurebesh_2_es(es_2_aurebesh("Gracias Brais")))    