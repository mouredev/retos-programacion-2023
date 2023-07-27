phone_codes_list = { 
    2: 'a',       
    22: 'b',      
    222: 'c',     
    3: 'd',      
    33: 'e',     
    333: 'f',    
    4: 'g',      
    44: 'h',      
    444: 'i',    
    5: 'j',      
    55: 'k',      
    555: 'l',     
    6: 'm',     
    66: 'n',      
    666: 'o',     
    7: 'p',       
    77: 'q',     
    777: 'r',     
    7777: 's',    
    8: 't',       
    88: 'u',      
    888: 'v',     
    9: 'w',      
    99: 'x',      
    999: 'y',     
    9999: 'z'     
}

input_code = input('Entrada: ').split('-')

def verify_input(input_code):
    for code in input_code:
        if not code.isnumeric():
            print('Los códigos tienen que ser numéricos.')
            return False
        
        code_to_int = int(code)
        if code_to_int not in phone_codes_list:
            print('Hay un código que no es válido.')
            return False
        
        if len(code) > 1:
            number_to_verify = code[0]
            for number in code:
                if number != number_to_verify:
                    print('Si un bloque tiene más de un número, debe ser siempre el mismo.')
                    return False
    return True
    


def print_text(input_code, phone_codes_list, verify_input):
    if verify_input(input_code):
        print('Salida: ', end='')
        for code in input_code:
            code_to_int = int(code)
            print((phone_codes_list[code_to_int]).upper(), end='')
        print()
        print('¡¡ Todo salió perfecto !!')
    else:
        print('¡¡ Algo ha salido mal !!')
    


print_text(input_code, phone_codes_list, verify_input) 

