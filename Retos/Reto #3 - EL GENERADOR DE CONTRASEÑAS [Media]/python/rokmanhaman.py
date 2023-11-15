import random
import string



class password():

    possible_characters = []

    def __init__(self, long, upper_case=False, numeric=False, symbolyc=False):
        self.long = long
        self.final_lenght = 8 if long < 8 else 16 if long > 16 else long
        self.upper_case = upper_case
        self.numeric = numeric
        self.symbolyc = symbolyc
    

    def config(self):

        ###
        if self.upper_case == 0:
            l_lower_case = list(string.ascii_lowercase)
            for l in l_lower_case:
                self.possible_characters.append(l)
        elif self.upper_case == 1:
            l_letters = list(string.ascii_letters)
            for l in l_letters:
                self.possible_characters.append(l)
        else:
            print("error Elija 0 o 1")
        ###
        if self.numeric == 0:
            pass
        elif self.numeric == 1:
            l_digits = list(string.digits)
            for l in l_digits:
                self.possible_characters.append(l)
        ###
        if self.symbolyc == 0:
            pass
        elif self.symbolyc ==1:
            l_punctuation = list(string.punctuation)
            for l in l_punctuation:
                self.possible_characters.append(l)
        
        return ' los caracteres posibles son: ' +'\n'+ '{}'.format(self.possible_characters) #+ '{} {} {} {}'.format(self.long, self.upper_case, self.numeric, self.symbolyc)
    

    def generattor(self):
        pass_out = []
        for i in range(self.final_lenght):

            pass_out.append(random.choice(self.possible_characters))
        
        return 'la contraseña es: {}'.format(''.join(pass_out))



pwd1 = password(20,True, True, True)


pwd1.config()

print(pwd1.generattor())


