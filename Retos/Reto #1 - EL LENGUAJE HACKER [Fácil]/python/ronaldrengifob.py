leet = {
        #diccionario minusculas
        "a":"4", "b":"|3", "c":"[", "d":")", "e":"3", "f":"|=", "g":"&", "h":"#", "i":"1", "j":",_|", "k":">|", "l":"1", "m":"/\\/\\", "n":"^/", "o":"0", "p":"|*", "q":"(_,)", "r":"I2", "s":"5", "t":"7", "u":"(_)", "v":"\\/", "w":"\\/\\/", "x":"><", "y":"j", "z":"2",
        #diccionario numeros
        "0":"o", "1":"L", "2":"R", "3":"E", "4":"A", "5":"S", "6":"b", "7":"T", "8":"B", "9":"g",
        }
result = ""
text = input("Texto para convertir en leet: ") 

for word in text.lower():
    if word in leet:
        result += leet[word]
    else:
        result += word

print("Tu texto en leet es: " + result)