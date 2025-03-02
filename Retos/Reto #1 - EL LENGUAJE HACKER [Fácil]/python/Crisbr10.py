#Definimos el diccionario para relacionar cada letra del alfabeto español al leet
dictionary = {
    "A" : "4",
    "B" : "I3",
    "C" : "[",
    "D" : ")",
    "E" : "3",
    "F" : "|=",
    "G" : "&",
    "H" : "#",
    "I" : "1",
    "J" : ",_|",
    "K" : ">|",
    "L" : "1",
    "M" : "/\\/\\",
    "N" : "^/",
    "O" : "0",
    "P" : "|*",
    "Q" : "(_,)",
    "R" : "I2",
    "S" : "5",
    "T" : "7",
    "U" : "(_)",
    "V" : "\\/",
    "W" : "\\/\\/",
    "X" : "><",
    "Y" : "j",
    "Z" : "2"
}

def translate(text:str):
    
    #Eliminamos espacios al inicio y final y pasamos todas las letras a mayúsculas
    text_upper = text.strip()
    text_upper = text.upper()
    
    translated_text = ""
    
    for character in text_upper:
        #Verificamos que el caracter esta en el diccionario
        if character in dictionary.keys():
            translated_text += dictionary[character]  
        #Si no está se le agrega al texto traducido directamente por no tener traducción en el leguaje leet
        else:
            translated_text += character
    return translated_text   

#Ejemplo de uso de la función
print(translate("Hello Python !"))