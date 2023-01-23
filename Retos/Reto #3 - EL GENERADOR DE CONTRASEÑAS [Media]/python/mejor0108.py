import secrets

def get_char() -> str:
    index = secrets.randbelow(94)
    return chr(index + 32 )

def get_password() ->str:
    password = ""
    cantidad_caracteres = secrets.randbelow(8) + 8
    for i in range(cantidad_caracteres):
        password = password + get_char()
    return password
        
    
    
if __name__ == '__main__':
    print(get_password() )
    


    