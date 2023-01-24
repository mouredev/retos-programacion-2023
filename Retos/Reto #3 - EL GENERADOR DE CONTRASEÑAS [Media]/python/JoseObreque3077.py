"""
Reto #3: El Generador de Contraseñas

Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:

- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.

(Pudiendo combinar todos estos parámetros entre ellos)
"""
import re
import string
from random import choices


class PasswordGenerator():
    """
    A class that allows the user to generate random passwords
    under specific criteria.
    """
    
    def __init__(self):
        """
        Initialize the class instance with tuples of characters: lowercase
        letters, uppercase letters, digits, and symbols.
        """
        self._lowercase_letters = tuple(string.ascii_lowercase)
        self._uppercase_letters = tuple(string.ascii_uppercase)
        self._digits = tuple(string.digits)
        self._symbols = tuple(string.punctuation)
    
    def new_password(
        self,
        length=12,
        use_uppercase=False,
        use_digits=False,
        use_symbols=False
        ):
        """
        A method that generate a random password.
        
        Parameters:
            length: Password length (integer between 8 and 12, default 12)
            use_uppercase: True is the password must contains uppercase letters
            (default False).
            use_digits: True if the password must contains digits
            (default False).
            use_symbols: True if the password must contains symbols
            (default False).
        """
        # Raise and exception for an invalid password length
        if not 8 <= length <= 12:
            raise PasswordLengthException()
        
        # Password generation characters tuple
        password_chars = self.password_chars(
            use_uppercase,
            use_digits,
            use_symbols
        )
        
        while True:
            # A random password is generated
            random_chars = choices(password_chars, k=length)
            password = ''.join(random_chars)
            
            # Password characters validation
            is_valid = self.password_validation(
                password,
                use_uppercase,
                use_digits,
                use_symbols
            )
            
            if is_valid:
                break
            
        return password
    
    def password_chars(self, uppercase, digits, symbols):
        """
        A method that generate the required set of characters for
        password generation.
        
        Parameters:
            uppercase: True if uppercase letters are required.
            digits: True if digits are required.
            symbols: True if symbols are required.
            
        Returns: A tuple of characters.
        """
        chars = self._lowercase_letters
    
        if uppercase:
            chars += self._uppercase_letters
        
        if digits:
            chars += self._digits
        
        if symbols:
            chars += self._symbols
        
        return chars
    
    def password_validation(self, password, uppercase, digits, symbols):
        """
        A method that checks if the given password is valid given specific
        criteria.
        
        Parameters:
            uppercase: True if uppercase letters are required.
            digits: True if digits are required.
            symbols: True if symbols are required.
            
        Returns: True if the password contains the required characters,
        False otherwise.
        """
        
        lowercase_regex = re.compile(r'[a-z]')
        uppercase_regex = re.compile(r'[A-Z]')
        digits_regex = re.compile(r'[0-9]')
        symbols_regex = re.compile(f'[{re.escape(str(self._symbols))}]')
        
        
        # Lowercase letters validation
        if not lowercase_regex.search(password):
            return False
        
        # Uppercase letters validation
        if uppercase and not uppercase_regex.search(password):
            return False 
        
        # Digits validation
        if digits and not digits_regex.search(password):
            return False
        
        # Symbols validation
        if symbols and not symbols_regex.search(password):
            return False
        
        return True


class PasswordLengthException(Exception):
    """
    Exception raised when the chosen password length is lower than 8 and
    greater than 12 characters.
    """
    def __init__(self):
        self.message = 'The password length must be between 8 and 12 characters'
        super().__init__(self.message)


if __name__ == '__main__':
    generator = PasswordGenerator()
    
    # Only lowercase password
    password_1 = generator.new_password()
    print(f'Password (lowercase only): {password_1}')
    
    # Only letters password
    password_2 = generator.new_password(use_uppercase=True)
    print(f'Password (letters only): {password_2}')
    
    # Alphanumeric password
    password_3 = generator.new_password(
        length=9,
        use_uppercase=True,
        use_digits=True
    )
    print(f'Password (alphanumeric): {password_3}')
    
    # All characters password
    password_4 = generator.new_password(
        length=11,
        use_uppercase=True,
        use_digits=True,
        use_symbols=True
    )
    print(f'Password (full): {password_4}')
