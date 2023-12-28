
import string
import random

'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''

class Password ():
    def __init__(self) -> str:
        self.password_length = list(range(8,17))
        self.number_case = 0
        self.alfa_case = 0
        self.simbol_case = 0

    def generate(self, password_length):
    
        style = input('\nIngrese requerimientos de clave: \n'
                            '\n*Con letras: 1\n'
                            '*Con números: 2\n'
                            '*Con símbolos: 3\n'
                            '*Con combinaciones: 12 (1 y 2) 13 (1 y 3) 23 (2 y 3) 123(1 2 y 3) \n')
        
        if style == '1':
            
            print(''.join(random.choice(string.digits) for _ in range(random.choice(password_length))))

        elif style == '2':

            print(''.join(random.choice(string.ascii_uppercase) for _ in range(random.choice(password_length))))

        elif style == '3':

            print(''.join(random.choice(string.punctuation) for _ in range(random.choice(password_length))))
        
        elif style == '12':

            print(''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(random.choice(password_length))))

        elif style == '13':

            print(''.join(random.choice(string.digits + string.punctuation) for _ in range(random.choice(password_length))))

        elif style == '23':

            print(''.join(random.choice(string.ascii_uppercase + string.punctuation) for _ in range(random.choice(password_length))))

        elif style == '123':

            print(''.join(random.choice(string.digits + string.ascii_uppercase + string.punctuation) for _ in range(random.choice(password_length))))

        else:

            pass


if __name__ == '__main__':

    password = Password()

    password.generate(password.password_length)

                
    
    


        




