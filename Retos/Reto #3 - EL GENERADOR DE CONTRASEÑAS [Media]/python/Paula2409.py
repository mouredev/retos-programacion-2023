"""
## Enunciado

```
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
```
"""

import string
import random

def generate_password() -> str:
    """
    The function 'generate_password' generate a random password based on the given parameters.

    Args: 
        None
    
    Returns:
        str: password with letters, numbers and symbols.
    """
    
    # List of letters (lower and upper), numbers and symbols
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    code = letters+numbers+symbols
    
    # Generate a random number for the lenght of password 
    k = random.randint(8,16) 

    # Generate password 
    password = "".join(random.choices(code,k=k))
   
    return password

print(generate_password())