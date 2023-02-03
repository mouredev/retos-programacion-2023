'''*
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

'''
import string
import secrets

def parameters(upperCase=True, numbers=True, symbols=True):
    alphabet = ""
    # si upperCase es verdadero
    if upperCase:
        # traemos todo el alfabeto en minusculas y mayusculas
        alphabet = string.ascii_letters
    else:
        alphabet += string.ascii_lowercase
    
    if numbers:
        alphabet += string.digits
    
    if symbols:
        alphabet += string.punctuation
    
    #print(f"alphabet: {alphabet}")

    return alphabet




if __name__ == "__main__":
    # menu
    upperCase = input("Quieres que tu clave lleve Mayusculas?: (s) or (n): ")
    numbers = input("Quieres que tu clave lleve Números?: (s) or (n): ")
    symbols = input("Quieres que tu clave lleve Símbolos?: (s) or (n): ")
    longitud = int(input("De que tamaño quieres tu contraseña?: (min: 8, max: 16): "))
    if (longitud >= 8) and (longitud <= 16):
        upperCase = True if upperCase.lower() == 's' else False
        numbers = True if numbers.lower() == 's' else False
        symbols = True if symbols.lower() == 's' else False

        alphabet = parameters(upperCase=upperCase, numbers=numbers, symbols=symbols)
        password = ''.join(secrets.choice(alphabet) for i in range(longitud))
        print(f"Tu contraseña: {password}")
    else:
        print("No se pudo completar la contraseña por la longitud!")