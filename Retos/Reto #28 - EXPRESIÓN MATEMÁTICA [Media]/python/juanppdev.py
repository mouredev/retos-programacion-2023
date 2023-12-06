"import re

def es_expresion_correcta(expresion):
    # Expresión regular para validar la estructura de la expresión matemática
    patron = r'^\s*([-+]?\d+(\.\d+)?(\s*[-+*/%]\s*[-+]?\d+(\.\d+)?)*\s*)$'
    
    # Comprobar si la expresión coincide con el patrón
    if re.match(patron, expresion):
        try:
            # Intentar evaluar la expresión para detectar errores de sintaxis
            eval(expresion)
            return True
        except:
            return False
    else:
        return False

# Ejemplos de uso:
expresion1 = "5 + 6 / 7 - 4"
expresion2 = "5 a 6"

print(es_expresion_correcta(expresion1))  # Output: True
print(es_expresion_correcta(expresion2))  # Output: False