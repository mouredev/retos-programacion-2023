import re

def is_expression(expression: str) -> bool:
    if re.fullmatch(r'([0-9]+\s?[+-/*%^]\s?)*[0-9]+', expression):
        return True
    else:
        return False
    
print(is_expression("6+5+43"))
print(is_expression("6 +5"))
print(is_expression("6 + 555487"))
print(is_expression("6 +")) 