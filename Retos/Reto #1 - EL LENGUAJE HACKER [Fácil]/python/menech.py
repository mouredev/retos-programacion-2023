#Diccionario con los valores a cambiar
coder = {
    "A":"4", "B":"I3", "C":"[", "D":")", "E":"3", "F":"|=", 
    "G":"&", "H":"#", "I":"1", "J":",_|", "K":">|", "L":"1", 
    "M":"/\/\\", "N":"^/", "O":"0", "P":"|*", "Q":"(_,)", 
    "R":"I2", "S":"5", "T":"7", "U":"(_)", "V":"\/", "W":"\/\/", 
    "X":"><", "Y":"j", "Z":"2", "1":"L", "2":"R", "3":"E", 
    "4":"A", "5":"S", "6":"b", "7":"T", "8":"B", "9":"g", "0":"o" }

#Función que va comprobando si el caracter esta en el diccionario coder y si no deja el caracter sin traducir para los espacios, simbolos, saltos de linea, etc...
def traducir_lenguaje_hacker(text):
    text = text.upper()
    print_text = ""
    for indice in range(len(text)):
        if text[indice] in coder:        
            print_text += coder[text[indice]]
        else: 
            print_text += text[indice] 
        
    print(print_text)

if __name__ == '__main__':
    print("") #simplemente se pone un salto de linea para separa bien las pruebas
    traducir_lenguaje_hacker("Esto es una prueba para traducir a lenguaje hacker")
    print("") #simplemente se pone un salto de linea para separa bien las pruebas
    traducir_lenguaje_hacker("Es importante probar tambien los numeros, por ejemplo el 1 o el 9")
    print("") #simplemente se pone un salto de linea para separa bien las pruebas
    traducir_lenguaje_hacker("a b C D e f g h I J K L M N O P Q R S t u v w x y z 1 2 3 4 5 6 7 8 9 0")
    print("") #simplemente se pone un salto de linea para separa bien las pruebas
