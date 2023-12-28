math_expressions = [
    "2 + ",
    "2 + 3",
    "2 + 3.6",
    "2 + 3.6 * 9",
    "2 + 3.6 *  9",
    "2 + 3.6 % 9",
    "2 + 3.6 * 9 ",
    "2 +- 3.6 * 9",
    "-2 + 3.6 * 9",
    "2 + 3.6 * 9 + 3",
    "2 + 3.6 / i + 6",
    "2 + 3.6 / 9 a 3 * 5",
    " 2 + 3.6 + 9 + 3",
    " 2 + 3.6 v 9 + 3"]

operations = ["+", "-", "*", "/", "%"]

def randomExpression() -> str:
    import random
    """ Devuelve una expresión matemática aleatoria."""
    return random.choice(math_expressions)

def checkExpression(expression: str) -> bool:
    """ 
    Comprueba si la expresión matemática es correcta.
    Retorna true o false.
    Para que sea correcta debe poseer como mínimo un número, una operación y otro número separados por un espacio.
    Puede contener números positivos, negativos, enteros o decimales.
    Operaciones soportadas: + - * / % 
    """
    split_expression = expression.split(" ")
    if len(split_expression) < 3:
        return False
    
    for i in range(0, len(split_expression), 2):
        try:
            float(split_expression[i])
        except ValueError:
            return False
    for i in range(1, len(split_expression), 2):
        if split_expression[i] not in operations:
            return False    
    return True

try:
    expression = randomExpression()
    print(f"La expresión matemática: '{expression}' es {checkExpression(expression)}")
except Exception as e:
    print(f"Ha ocurrido un error: {str(e)}")

