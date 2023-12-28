#Recibe el diccionario con los caracteres y el caracter corresponduiente a la palbra digitada
def converter_hacker_len(dictionary: dict, char: str) -> str:
    result = ""
    for obj in dictionary:
        if(obj["caracter"] == char):
            result = obj["value"]
            break  
    return result
    
dictionary_lenguage = [
    {
        "caracter": "A",
        "value": "4"
    },
    {
        "caracter": "B",
        "value": "I3"
    },
    {
        "caracter": "C",
        "value": "["
    },
    {
        "caracter": "D",
        "value": ")"
    },
    {
        "caracter": "E",
        "value": "3"
    },
    {
        "caracter": "F",
        "value": "|="
    },
    {
        "caracter": "G",
        "value": "&"
    },
    {
        "caracter": "H",
        "value": "#"
    },
    {
        "caracter": "I",
        "value": "1"
    },
    {
        "caracter": "J",
        "value": ",_|"
    },
    {
        "caracter": "K",
        "value": ">|"
    },
    {
        "caracter": "L",
        "value": "1"
    },
    {
        "caracter": "M",
        "value": "/\\/\\"
    },
    {
        "caracter": "N",
        "value": "^/"
    },
    {
        "caracter": "O",
        "value": "0"
    },
    {
        "caracter": "P",
        "value": "|*"
    },
    {
        "caracter": "Q",
        "value": "(_,)"
    },
    {
        "caracter": "R",
        "value": "I2"
    },
    {
        "caracter": "S",
        "value": "5"
    },
    {
        "caracter": "T",
        "value": "7"
    },
    {
        "caracter": "U",
        "value": "(_)"
    },
    {
        "caracter": "V",
        "value": "\/"
    },
    {
        "caracter": "W",
        "value": "\\/\\/"
    },
    {
        "caracter": "X",
        "value": "><"
    },
    {
        "caracter": "Y",
        "value": "j"
    },
    {
        "caracter": "Z",
        "value": "I2"
    }]
result = ""
word = input("Ingrese la palabra: ")

for character in word.upper():
    result += converter_hacker_len(dictionary=dictionary_lenguage, char=character)

print("El resultado es:", result)