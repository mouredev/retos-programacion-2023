import re

def main():
    expression1 = "5 + 6 / 7 - 4"
    expression2 = "5 a 6"

    print(validate_math_expression(expression1))
    print(validate_math_expression(expression2))

def validate_math_expression(expression):
    tokens = re.split(r'\s+', expression)
    
    if len(tokens) % 2 == 0:
        return False

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not is_number(token):
                return False
        else:
            if not is_operation(token):
                return False

    return True

def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_operation(token):
    return re.match(r'[+\-*/%]', token)

if __name__ == "__main__":
    main()
