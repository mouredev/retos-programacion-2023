def test_math_expr(text: str, symbol_list: list):
    
    is_math_expr = False
    text_symbol_list = [c for c in text.replace(" ", "") if not c.isdigit()]
    print(text_symbol_list)
    last_symbol = None
    for ch in text_symbol_list:
        if ch not in symbol_list:
            return False 
    try:
        result = eval(text)
        result_clean = abs(int(result))
        is_math_expr = True
    except:
        is_math_expr = False            
    return is_math_expr
                                              
if __name__ == "__main__":

    operation_list = ["+", "-", "*", "/", "%"]
    symbol_list = operation_list + [" ", "."]
    text = "1 + 1 / -6.5"
    is_math_expr = test_math_expr(text, symbol_list)
    print(is_math_expr)