# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

import random

def passwordGenerator():
        characters = "abcdefghijklmnopqrstuvwxyz"
        length = 0
        
        while (length < 8 or length > 16):
            length = int(input("Digite la longitud que desea que tenga la constraseña entre 8 y 16 caracteres:\n"))
        
        password = " " * length
        
        upperCaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!$%&()=/?¿¡:,_-|@#+*{}[]^\\ñ"
        
        containsLetters = input("¿Desea que su contraseña contenga letras mayúsculas?"
                + "\n s) si"
                + "\n n) no \n").lower().strip()[0]
        characters += upperCaseletters if  containsLetters == 's' else ""
        
        containsNumbers = input("¿Desea que su contraseña contenga números?"
                + "\n s) si"
                + "\n n) no \n").lower().strip()[0]
        characters += numbers if containsNumbers == 's' else ""
                
        containsSymbols = input("¿Desea que su contraseña contenga símbolos?"
                + "\n s) si"
                + "\n n) no \n").lower().strip()[0]
        characters += symbols if containsSymbols == 's' else ""
        
        if (len(characters) == 0):
            print("No se puede generar una contraseña sin caracteres")
            return ""
        
        return list(map(lambda letter: characters[random.randint(0, len(characters))], [*password]))

print("".join(passwordGenerator()))