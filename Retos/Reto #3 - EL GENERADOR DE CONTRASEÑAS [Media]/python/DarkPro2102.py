import secrets
import string

class PassGenerator:
    
    def __init__(self, size: int, spe_char: bool = True, nums: bool = True, upper :bool = True) -> None:
        
        self.size = size
        self.spe_char = spe_char
        self.nums = nums
        self.upper = upper
    
    def generate(self):
        
        if self.size <= 8 or self.size >= 16:
            raise Exception("Invalid longitude for a password")

        alphabet = string.ascii_letters if self.upper else string.ascii_lowercase
        numbers = string.digits if self.nums else ""
        special = string.punctuation if self.spe_char else ""

        password = ''.join(secrets.choice(alphabet + numbers + special) for _ in range(self.size))

        return password
    
if __name__ == "__main__":
    
    Password1 = PassGenerator(15)
    Password2 = PassGenerator(10, nums=False, spe_char=False)
    
    print(Password1.generate())
    print(Password2.generate())
