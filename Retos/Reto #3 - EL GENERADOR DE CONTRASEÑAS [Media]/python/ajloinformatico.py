
from os import system
from random import choices
from string import digits, ascii_lowercase, ascii_uppercase

"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""

SPECIAL_CHARACTERS = "SPECIAL_CHARACTERS"
NUMBERS = "NUMBERS"
UPPER_CASSES = "UPPER_CASSES"
APP_NAME = """
#######################################
          PASSWORD-GENERATOR

            by infolojo
          https:://infolojo.es
        Antonio José Lojo Ojeda
#######################################
"""


class ErrorMessages:
    def __init__(self):
        self.password_length = "Error: Password length must be in a range between 8 and 16"
        self.number_expected = "Error: Its not a number"
        self.true_or_false_expected = "Error: We need y (yes) or n (not) as argument"

    def throw_password_length_error(self):
        print(self.password_length)

    def throw_number_expected_error(self):
        print(self.number_expected)

    def throw_true_or_false_expected_error(self):
        print(self.true_or_false_expected)


class PasswordGenerator:
    def __init__(self):
        # TODO update name to password_length
        self.leng: int
        self.special_symbols: bool
        self.numbers: bool
        self.upper_casses: bool
        self.errors = ErrorMessages()
        self.punctuation = "!#$%&()*+-/<=>?@[\]{|}"

    def create_password(self):
        # get 
        password_content = ascii_lowercase
        
        # Add user suggests
        if self.special_symbols:
            password_content += self.punctuation

        if self.numbers:
            password_content += digits

        if self.upper_casses:
            password_content += ascii_uppercase

        # get random element for list and return a new list with k leng to convert into string with "".join
        print("\n" + "".join(choices(list(password_content), k=self.leng)))

    def clear(self):
        # uncomment by checking your or
        # clear windows screen
        # system('CLS')
        # clear linux screen
        system('clear')

    def run(self):
        self.clear()
        print(APP_NAME)
        self.get_parameters()
        self.create_password()

    def update_bool_value(self, type: str, value: bool):
        if type == SPECIAL_CHARACTERS:
            self.special_symbols = value
        elif type == NUMBERS:
            self.numbers = value
        elif type == UPPER_CASSES:
            self.upper_casses = value

    def check_bool_input(self, type: str, inputText: str):
        """Check an user bool input
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        bool_input_ready: bool = False
        while (bool_input_ready != True):
            bool_input = input(f"\n{inputText}? [y/n]\n>> ").lower()
            if bool_input == "y" or bool_input == "n":
                self.update_bool_value(type = type, value = bool_input == "y")
                bool_input_ready = True
            else:
                self.errors.throw_true_or_false_expected_error()

    
    def check_len_input(self):
        """Check password legnth input
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        
        len_ready: bool = False
        while(len_ready == False):
            try:
                len_input: int = int(input("\nWhat length of password do you want (It must be in a range from 8 to 16)\n>> ")) 
                if len_input < 8 or len_input > 16:
                    self.errors.throw_password_length_error()
                else:
                    self.leng = len_input
                    len_ready = True
            except:
                self.errors.throw_number_expected_error()
                

    def get_parameters(self):
        # check length # TODO CHECK DEFAULT ON CLASS INIT
        self.check_len_input()

        # check upper case
        self.check_bool_input(type=UPPER_CASSES, inputText="Do you want to use upper casses")
        
        # check numbers
        self.check_bool_input(type=NUMBERS, inputText="Do you want to use numbers")
        
        # check special characters
        self.check_bool_input(type=SPECIAL_CHARACTERS, inputText="Do you want to use special characters")          
            
        
if __name__ == "__main__":
    PasswordGenerator().run()
