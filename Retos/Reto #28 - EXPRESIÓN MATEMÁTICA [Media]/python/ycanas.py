def check(expression: str) -> bool:
    componentes = expression.split(' ')
    
    if len(componentes) >= 3 or len(componentes) % 2 == 0:
        for index, value in enumerate(componentes):
            if index % 2 == 0:
                try:
                    float(value)
                except:
                    return False

            else:
                if value not in ('+', '-', '*', '/', '%'):
                    return False
        
        return True
    
    return False
    

print(check("3 + 5"))
print(check("3 a 5"))
print(check("-3 + 5"))
print(check("- 3 + 5"))
print(check("-3 a 5"))
print(check("-3+5"))
print(check("3 + 5 - 1 / 4 % 8"))
