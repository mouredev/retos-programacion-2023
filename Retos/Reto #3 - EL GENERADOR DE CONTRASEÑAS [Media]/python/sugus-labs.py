import string
import random 

def generate_password(
    length: int = 12, 
    upper_letters: bool = True,
    numbers: bool = True,
    symbols: bool = True):
    
    """ Generato password function """
    
    password = ""
    alphabet_str = ""
        
    if upper_letters:
        alphabet_str = alphabet_str + string.ascii_letters
    else:
        alphabet_str = alphabet_str + string.ascii_lowercase
    if numbers:
        alphabet_str = alphabet_str + string.digits
    if symbols:
        alphabet_str = alphabet_str + string.punctuation
    
    alphabet_list = list(alphabet_str)
    
    for num in range(0, length):
        char = random.choice(alphabet_list)
        password = password + char
        
    return password
            
if __name__ == "__main__":
    passw = generate_password(16)
    print(passw)