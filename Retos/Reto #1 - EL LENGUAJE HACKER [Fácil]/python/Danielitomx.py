#Nuevo Commit
diccionario = {
    "A":"4",
    "B":"I3",
    "C":"[",
    "D":"|)",
    "E":"ë",
    "F":"ph=",
    "G":"(_+",
    "H":"#",
    "I":"1",
    "J":"._|",
    "K":">|",
    "L":"1",
    "M":"1^1",
    "N":"И",
    "O":"0",
    "P":"9",
    "Q":"(_,)",
    "R":"|2",
    "S":"es",
    "T":"-|-",
    "U":"µ",
    "V":"|/",
    "W":"\X/",
    "X":"><",
    "Y":"`/",
    "Z":"%",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o",
}

texto = input("¿Cual es el texto que deseas tranformar?: \n")
def conversor (texto):

    texto_transformado = ""

    for i in range(len(texto)):
        letra = texto.upper()[i] #Aqui quiere decir que calquier letra que te pongan en minusculas trans a mayusculas, claro para buscarlas arriba
        if letra in diccionario:
            texto_transformado += diccionario[letra]
        else:
            texto_transformado += letra
    return texto_transformado
print(conversor(texto))


