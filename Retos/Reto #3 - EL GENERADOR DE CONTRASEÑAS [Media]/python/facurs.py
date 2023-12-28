"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""

import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    """
    Genera una contraseña aleatoria con los parámetros especificados.
    
    length: int entre 8 y 16
    use_uppercase: bool
    use_numbers: bool
    use_symbols: bool
    """
    if not 8 <= length <= 16:
        raise ValueError("La longitud debe ser entre 8 y 16 caracteres")
    password_chars = ""
    if use_uppercase:
        password_chars += string.ascii_uppercase
    if use_numbers:
        password_chars += string.digits
    if use_symbols:
        password_chars += string.punctuation
    if not use_uppercase and not use_numbers and not use_symbols:
        password_chars += string.ascii_letters + string.digits

    return ''.join(random.choice(password_chars) for i in range(length))

print(generate_password(8, True, True, True))


"""
Crea la funcion generate_password, la cual acepta 4 argumentos, longitud, mayusculas, numeros y simbolos
controla que el tamaño sea entre 8 y 16
consulta si usar mayus, numeros, simbolos
si ninguno de estos se usa retorna una contraseña con letras minusculas
"""