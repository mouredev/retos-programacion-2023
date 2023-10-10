"""
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
"""
# Lista que se comprobara durante la ejecucion
list_of_words = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "0","1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
#funcion
def cipher_cease ():
    result = ""
    try:
#inicio del sistema
        print("Bienvenido al sistema de cifrado Cesar\nDesea cifrar o decodificar un mensaje en este programa\n(C: Para cifrar/D: Para decodificar:)")
        insest = str(input("Ingrese su peticion: "))
#sistema de cifrado
        if insest.upper() == "C":
            word = str(input("Ingrese la palabra a cifrar: "))
            code = int(input("Ingrese la clave para el cifrado: "))
            for index in word:
                vaule = index.upper()
                if vaule in list_of_words:
                    pocition = list_of_words.index(vaule)
                    result += list_of_words[(pocition + code)]
            result = result.lower()
#sistema de decifrado
        elif insest.upper() == "D":
            word = str(input("Ingrese la palabra a cifrada: "))
            code = int(input("Ingrese la clave para el decifralo: "))
            for index in word:
                vaule = index.upper()
                if vaule in list_of_words:
                    pocition = list_of_words.index(vaule)
                    result += list_of_words[(pocition - code)]
            result = result.capitalize()
#contro de errorres en inicio
        else:
            print ({"Error": "Parametro inicial no aceptado"})
            sentenc = str(input("Desea arracar el programa denuevo?\n(S: si / N: no)\nColoque su peticion: "))
            if sentenc.upper == "S":
                cipher_cease ()
            elif sentenc.upper == "N":
                pass
    except:
            return {"Error": "Sistema no pudo funcionar"}
#resultado
    finally:
        print("Gracias por usar nuestro servicio de codificacion.")
        return result
print(cipher_cease ())
