"""
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
  Podrás configurar generar contraseñas con los siguientes parámetros:
  - Longitud: Entre 8 y 16.
  - Con o sin letras mayúsculas.
  - Con o sin números.
  - Con o sin símbolos.
  (Pudiendo combinar todos estos parámetros entre ellos)
"""
#libraries
import random

#general variables / lists
lowerList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numList = ["0","1","2","3","4","5","6","7","8","9"]
simbolList = ["!","#","$","%","&","/","(",")","=","?","¿","¡","*","+","~","{","}","[","]","-","_","|","¬"]

lowerUpperList = lowerList + upperList
lowerNumberList = lowerList + numList
lowerSimbolList = lowerList + simbolList
lowerUpperNumList = lowerList + upperList + numList
lowerNumberSimbolList = lowerList + numList + simbolList
lowerUpperSimbolsList = lowerList + upperList + simbolList
fullList = lowerList + upperList + numList + simbolList

passList = []
passString = ""

#input
print("\n-------- Password generator --------")
passLen = int(input("Select number of characters (min. 8 - max. 16): "))
upperIncluded = input("Would you like to include capital letters? (yes - no): ")
numbersIncluded = input("Would you like to include numbers? (yes - no): ")
simbolsIncluded = input("Would you like to include simbols? (yes - no): ")

#option verification
if upperIncluded == "yes" and numbersIncluded == "no" and simbolsIncluded == "no":
    while len(passList) != passLen:
        element = random.choice(lowerUpperList)
        passList.append(element)
elif upperIncluded == "no" and numbersIncluded == "yes" and simbolsIncluded == "no":
    while len(passList) != passLen:
        element = random.choice(lowerNumberList)
        passList.append(element)
elif upperIncluded == "no" and numbersIncluded == "no" and simbolsIncluded == "yes":
    while len(passList) != passLen:
        element = random.choice(lowerSimbolList)
        passList.append(element)
elif upperIncluded == "yes" and numbersIncluded == "yes" and simbolsIncluded == "no":
    while len(passList) != passLen:
        element = random.choice(lowerUpperNumList)
        passList.append(element)
elif upperIncluded == "no" and numbersIncluded == "yes" and simbolsIncluded == "yes":
    while len(passList) != passLen:
        element = random.choice(lowerNumberSimbolList)
        passList.append(element)
elif upperIncluded == "yes" and numbersIncluded == "no" and simbolsIncluded == "yes":
    while len(passList) != passLen:
        element = random.choice(lowerUpperSimbolsList)
        passList.append(element) 
elif upperIncluded == "yes" and numbersIncluded == "yes" and simbolsIncluded == "yes":
    while len(passList) != passLen:
        element = random.choice(fullList)
        passList.append(element)  
elif upperIncluded == "no" and numbersIncluded == "no" and simbolsIncluded == "no": 
    while len(passList) != passLen:
        element = random.choice(lowerList)
        passList.append(element)      

#converting list to string
for item in passList:
    passString += item

#output
print(passString)