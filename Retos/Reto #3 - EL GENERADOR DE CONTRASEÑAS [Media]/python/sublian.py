"""
Reto #3: EL GENERADOR DE CONTRASEÑAS
 Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

Enunciado
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

# ficheros necesarios
import secrets
import string

def leer_entero(texto="Indique el tamaño de la contraseña: "):
    entrada = input(texto)
    try:
        entrada = int(entrada)
        return entrada
    except ValueError:
        print ("La entrada es incorrecta: escribe un numero entero")
        return 0


def leer_cadena(texto):
    entrada = input(texto).upper()    
    if entrada.isalpha() and entrada == "S":
        return entrada
    elif entrada =="N":
        return False
    else:
        print("La entrada es incorrecta: escribe un caracter [s/n]")
        leer_cadena(texto)

if __name__ == '__main__':

    print("..::Reto #3: EL GENERADOR DE CONTRASEÑAS::..")
    alphabet=""

    clave_tam = leer_entero()
    if clave_tam>7 and clave_tam<17:
        res_letras= leer_cadena("Desea que posea letras mayúsculas [s/n]: ")
        if res_letras =="S":
            letters = string.ascii_uppercase   
            alphabet +=letters 
        
        res_numeros= leer_cadena("Desea que posea numeros [s/n]: ")
        if res_numeros =="S": 
            digits = string.digits 
            alphabet +=digits    

        res_simbolos= leer_cadena("Desea que posea símbolos [s/n]: ")
        if res_simbolos =="S":
            special_chars = string.punctuation
            alphabet +=special_chars 

        if res_letras or res_numeros or res_simbolos:
            # generate a password string
            pwd = ''
            for i in range(clave_tam):
                pwd += ''.join(secrets.choice(alphabet))
            print(pwd)      
        else:    
            print("No ha selecionado Letras, Numeros ni simbolos. No se puede generar la contraseña!")       
    else:    
        print("No se puede generar la contraseña. El rango permitido es de 8 a 16")

#alphabet = letters + digits + special_chars
