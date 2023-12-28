import re

def math_ex( expression ):
    match = re.search("^(-?\d+(\.\d+)?\s+[-+*/%]\s+)*-?\d+(\.\d+)?$", expression)
    validator = True if match else False
    return validator

test1 = math_ex( "5 + 6 / 7 - 4" ) # false
test2 = math_ex( "5 a 6" ) # false

print( test1 )
print( test2 )