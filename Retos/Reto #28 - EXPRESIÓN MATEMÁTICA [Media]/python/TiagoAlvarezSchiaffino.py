def check_math_expression(expression: str) -> bool:
    """
    Check if a mathematical expression is correct.

    Args:
        expression (str): The mathematical expression to check.

    Returns:
        bool: True if the expression is correct, False otherwise.
    """
    components = expression.split()

    if len(components) < 3 or len(components) % 2 == 0:
        return False
    
    for index, component in enumerate(components):
        if index % 2 == 0:
            try:
                float(component)
            except ValueError:
                return False
        else:
            if component not in ["+", "-", "*", "/", "%"]:
                return False

    return True

if __name__ == "__main__":
    expression1 = "3 + 5"
    expression2 = "3 a 5"
    expression3 = "-3 + 5"
    expression4 = "- 3 + 5"
    expression5 = "-3 a 5"
    expression6 = "-3+5"

    print(check_math_expression(expression1))
    print(check_math_expression(expression2))
    print(check_math_expression(expression3))
    print(check_math_expression(expression4))
    print(check_math_expression(expression5))
    print(check_math_expression(expression6))