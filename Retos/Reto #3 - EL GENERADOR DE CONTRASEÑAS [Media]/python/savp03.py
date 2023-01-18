# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import random

def run ():
    
    def generador_password(longitud, mayuscula, numero, simbolo):
        
        list_minus = ("a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z")
        list_mayus = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
        list_nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        list_simbolos = ("!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "^", "_", "`", "{", "|", "}", "~")

        password = []

        if longitud <8 or longitud > 16:
            print("La longitud tiene que ser entre 8 y 16")
            exit()

        else:

            if mayuscula == True and numero == True and simbolo == True:
                caracteres = list_minus + list_mayus + list_nums + list_simbolos

            elif mayuscula == True and numero == True and simbolo == False:
                caracteres = list_minus + list_mayus + list_nums 

            elif mayuscula == True and numero == False and simbolo == True:
                caracteres = list_minus + list_mayus + list_simbolos
                
            elif mayuscula == True and numero == False and simbolo == False:
                caracteres = list_minus + list_mayus

            elif mayuscula == False and numero == True and simbolo == True:
                caracteres = list_minus + list_nums + list_simbolos

            elif mayuscula == False and numero == True and simbolo == False:
                caracteres = list_minus + list_nums 

            elif mayuscula == False and numero == False and simbolo == True:
                caracteres = list_minus 

        for i in range (longitud):
            caracter_aleatorio =  random.choice(caracteres)
            password.append(caracter_aleatorio)

        password = "".join(password)

        print(password)

    generador_password(8, True, False, True)
    generador_password(15, True, True, False)
    generador_password(20, True, True, True)  

if __name__ == "__main__":
    run()