"""
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará True o False.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> True
 * "5 a 6" -> False
"""

import re

def check_expression(expression):
    OPERATORS = ["+", "-", "*", "/", "%"]
    expression_list = re.split("\s+", expression.strip())


    # if no 3 elements -> NOK

    if len(expression_list) < 3:
        print("\nThere must be at least 3 elements in the expression.")
        return False


    # if no operators at all -> NOK

    if not any([element for element in expression_list if element in OPERATORS]):
        print("\nThere are no operators in this expression.")
        return False


    # if expression starts or ends with operator -> NOK
    # * expression can start with "-" or "+"

    if (
        expression_list[0] in OPERATORS and expression_list[0] != "-" and expression_list[0] != "+" or
        expression_list[len(expression_list) - 1] in OPERATORS
    ):
        print(
            "\nExpressions can not start with operators (except "-" or "+").\nExpressions can not end with operators."
        )
        return False


    # check operators between numbers
    
    last_element = ""
    
    for element in expression_list:
        # if two operators together (no space between them) -> NOK
        if len(element) > 1 and not re.match(r"^\d+$", element):
            print("\nThis expression has more than one operator without spacing.")
            return False

        # if no operators between numbers -> NOK
        if re.match(r"^\d+$", last_element) and re.match(r"^\d+$", element):
            print("\nMissing operator between numbers.")
            return False

        # if two operators between numbers -> NOK
        if (
            last_element in OPERATORS and element in OPERATORS and
            element != "-"    # allowed for the number sign
        ):
            print("\nMissing number between operators.")
            return False

        # if not allowed operator -> NOK
        if re.match(r"(?!-|\+|\/|%|\*)[\W]", element):
            print("\nThere is a not allowed operator in this expression.")
            return False

        last_element = element


    # if no errors -> OK

    return True


print(check_expression("5 + 6 / 7 - 4"))      # True
print(check_expression("a + b / c - d"))      # True -> letters can be considered numbers
print(check_expression("5 / - 6"))            # True -> "-" operator allowed after another operator (number sign)

print(check_expression("5 a 6"))              # False -> no operators
print(check_expression("+ 5 - 6 8"))          # False -> missing operator between numbers
print(check_expression("+ 5 - 6 / % 8"))      # False -> missing number between operators
print(check_expression("5 & - 6"))            # False -> not allowed operator