import re

def expression(expression):
    if re.fullmatch(r'([0-9]+\s?[+-/*%^]\s?)*[0-9]+', expression):
        return True
    else:
        return False


print(expression("3+2+3+2/4-2"))
