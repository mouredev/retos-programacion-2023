### Reto #3 - EL GENERADOR DE CONTRASEÑAS ###
'''
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
    - Longitud: Entre 8 y 16.
    - Con o sin letras mayúsculas.
    - Con o sin números.
    - Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
'''

### Decision type of development ###
# For this challenge, we will try to use as few modules as possible to weight the learning to reuse, 
# therefore, neither the "argparse" for parameter input, nor the "string" for possible password characters is used.

import sys, random

parameters_help = '''
    usage: carresoft_python.py [-l{8-16}] [-u] [-n] [-s]

    optional arguments:
    -h          Show this help message.

    -l{8-16}    Sets password length between 8 and 16 characters. Default 8.    

    -u          Also generate with uppercase letters.

    -n          Also generate with numbers.

    -s          Also generate with symbols.
'''

# Function for parameter management
def parameters_ctrl():
    global uniques_parameters
    global password_length
    parameters = sys.argv[1:len(sys.argv)]
    uniques_parameters = set(map(lambda x: x[:2], parameters)) # The first two positions are collected to avoid the length number of the parameter "-l".

    if {'-h'} <= uniques_parameters or len(sys.argv) == 1:
        print("\n    # Password Generator #\n")
        print(parameters_help)
        return 0

    if not {'-h', '-l', '-u', '-n', '-s'} >= uniques_parameters: 
        incorrect_parameters()
        return -1
    if {'-l'} <= uniques_parameters:
        for parameter in parameters:
            if parameter[:2] == '-l':
                password_length = parameter[2:len(parameter)]
                try: 
                    if int(password_length) < 8 or int(password_length) > 16:
                        incorrect_parameters()
                        return -1
                except:
                    incorrect_parameters()
                    return -1
    return 1

def incorrect_parameters():
    print("\n    Incorrect parameters.\n")
    print(parameters_help)

#Function to generate source characters according to parameters
def character_filling():
    global characters_base
    global characters
    characters_base = [chr(i) for i in range(characters["l"][0], characters["l"][1]+1)]
    if '-u' in uniques_parameters: characters_base += [chr(i) for i in range(characters["u"][0], characters["u"][1]+1)]
    if '-n' in uniques_parameters: characters_base += [chr(i) for i in range(characters["n"][0], characters["n"][1]+1)]
    if '-s' in uniques_parameters: 
        characters_base += [chr(i) for i in range(characters["s1"][0], characters["s1"][1]+1)]
        characters_base += [chr(i) for i in range(characters["s2"][0], characters["s2"][1]+1)]



if __name__ == "__main__":
    # We will use the function "chr" with the ASCII equivalents
    # For the symbols we will use two sections, s1 and s2
    characters = {"l": [97,122], "u": [65,90], "n": [48, 57], "s1": [33,47], "s2": [58,64]}
    characters_base = []
    uniques_parameters = set()   
    password_length = 8 # Assigned by default
    password = ''

    # Calling parameter control
    parameters_ctrl = parameters_ctrl()
    if parameters_ctrl <= 0: sys.exit(parameters_ctrl)

    # Calling character filling
    character_filling()

    # Generating the password according to the desired length
    for i in range(int(password_length)):
        # It is not contemplated that there is at least one of each option.
        password += characters_base[random.randint(0,len(characters_base)-1)]
    
    print(f"Password: {password}")


