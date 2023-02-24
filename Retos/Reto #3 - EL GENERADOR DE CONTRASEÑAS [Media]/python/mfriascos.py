import random


class Password():

    def __init__(self, size) -> None:
        self.size = size
        self.passwd = []
        self.list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.list_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', "'", '"', '<', '>', ',', '.', '?', '/']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']


    def generate_password(self, with_upper, with_symbols, with_numbers):
            
        password_generator = [self.list_low]
        
        if with_upper:
            password_generator.append(self.list_upper)
        if with_symbols:
            password_generator.append(self.symbols)
        if with_numbers:
            password_generator.append(self.numbers)

        for i in range(self.size):
            choice_list = random.choice(password_generator)
            self.passwd.append(random.choice(choice_list))
                
        passwd_str = ''.join(self.passwd)
                
        return passwd_str


    def _with_upper(self):
        option = input('\nWith Capital letter? [Y/N]: ').upper()
        return option in ['Y', 'YES']


    def _with_symbols(self):
        option = input('\nWith symbols? [Y/N]: ').upper()
        return option in ['Y', 'YES']


    def _with_numbers(self):
        option = input('\nNumbers Include? [Y/N]: ').upper()
        return option in ['Y', 'YES']


print("\n               PASSWORD GENERATOR      \n")
print('*'*50)

size = int(input("\n  Choice password size 8 - 16: "))

while size < 8 or size > 16:
    print("\nInvalid Option, choice the correct format 8 - 16\n")
    size = int(input("  Choice password size: "))

new_password = Password(size)

print('\n'+new_password.generate_password(new_password._with_upper(),new_password._with_symbols(),new_password._with_numbers())+'\n')
