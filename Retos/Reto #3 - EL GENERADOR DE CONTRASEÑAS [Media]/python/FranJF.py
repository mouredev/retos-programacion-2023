"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
import string

class PasswordGenerator():
    def generar(self, longitud:int, con_mayus:bool, con_numeros:bool, con_simbolos:bool):
        
        if longitud > 16 or longitud < 8:
            raise Exception("He recibido una longitud incorrecta.")
        
        letras:str = string.ascii_letters if con_mayus else string.ascii_lowercase
        numeros:str = string.digits if con_numeros else ""
        simbolos:str = string.punctuation if con_simbolos else ""
        
        all_combinaciones:str = letras + numeros + simbolos
        
        return ''.join(random.choice(all_combinaciones) for i in range(longitud))

    
password_generator = PasswordGenerator()
password1 = password_generator.generar(14, True, True, True)
password2 = password_generator.generar(16, False, True, True)
password3 = password_generator.generar(8, False, True, False)

print(password1)
print(password2)
print(password3)
