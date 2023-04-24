import random
import string

print("Escribe un programa que sea capaz de generar contraseñas de forma aleatoria." 
  , "\nPodrás configurar generar contraseñas con los siguientes parámetros:"
  , "\n- Longitud: Entre 8 y 16."
  , "\n- Con o sin letras mayúsculas."
  , "\n- Con o sin números."
  , "\n- Con o sin símbolos."
  , "\n- (Pudiendo combinar todos estos parámetros entre ellos)\n")

def convertYN(input):
    if input == "y" or input == "Y":
        return True
    elif input == "n" or input == "N":
        return False
    else:
        return "null"
        

def get_random_string(lenght, mayus, nums, symbols):
    data = [string.ascii_lowercase]
    
    if mayus:
       data.append(string.ascii_uppercase)
       
    if nums:
        data.append(string.digits)
        
    if symbols:
         data.append(string.punctuation)
         
    passw = ""
    for num in range(0, lenght, 1):
        type = random.choice(data)
        passw += random.choice(type)
    
    print("Generated pass -> " ,passw)

def answer():
    lenght = input ("Longitud: Entre 8 y 16.")
    lenght = int(lenght) if lenght.isdigit() else 0
    areturn = {"check" : True}
    if lenght < 8 or lenght > 16:
        print("Error longitud ")
        areturn["check"] = False
        return areturn
    else:
        areturn["lenght"] = lenght
        
    areturn["mayus"] = convertYN(input("Mayusculas y/n"))
    areturn["nums"] = convertYN(input("Numeros y/n"))
    areturn["symbols"] = convertYN(input("Simbolos y/n"))
    
    if areturn["mayus"] == "null" or areturn["nums"] == "null" or areturn["symbols"] == "null":
        print("Porfavor, responda las preguntas con Y/N")
        areturn["check"] = False
    
    return areturn

data = {"check" : False}
while data["check"] == False:
    data = answer()
    mayus = data["mayus"] if "mayus" in data else ""
    nums =data["nums"] if "nums" in data else ""
    symbols = data["symbols"] if "symbols" in data else ""
    lenght = data["lenght"] if "lenght" in data else ""
    

    
get_random_string(lenght, mayus, nums, symbols)




