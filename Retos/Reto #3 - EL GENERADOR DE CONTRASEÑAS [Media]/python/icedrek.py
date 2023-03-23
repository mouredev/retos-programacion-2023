'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 '''
import random

def password_generator(length_pass, upper_pass, number_pass, symbol_pass):
    '''
    ASCII values:
      symbols     : 33-47
      numbers[0-9]: 48-57
      uppercase   : 65-90
      lowercase   : 97-122
    '''

    if length_pass < 8 or length_pass > 16:
        return "ERROR - longitud debe estar entre 8 y 16"
    if upper_pass.lower() != "n" and upper_pass.lower() != "s":
        return "ERROR - indicar mayusculas Si(s) o No(n)"
    if number_pass.lower() != "n" and number_pass.lower() != "s":
        return "ERROR - indicar numeros Si(s) o No(n)"
    if symbol_pass.lower() != "n" and symbol_pass.lower() != "s":
        return "ERROR - indicar simbolos Si(s) o No(n)"

    ranks = ["lower_range"]    
    if upper_pass.lower() == "s": ranks.append("upper_range")
    if number_pass.lower() == "s": ranks.append("number_range")
    if symbol_pass.lower() == "s": ranks.append("symbol_range")

    output = ""

    for i in range(length_pass):
        rank_selected = random.choice(ranks)
        
        if rank_selected == "lower_range":           
           output += chr((random.randint(97, 122)))        
        elif rank_selected == "upper_range":
          output += chr((random.randint(65, 90)))
        elif rank_selected == "number_range":
          output += chr((random.randint(48, 57)))
        elif rank_selected == "symbol_range":          
          output += chr((random.randint(33, 47)))
        else:
           return "ERROR - Error en selección de rangos"
        
    return output

length_pass = 16
upper_pass = "n"
number_pass = "s"
symbol_pass = "s"
print(password_generator(length_pass, upper_pass, number_pass, symbol_pass))
