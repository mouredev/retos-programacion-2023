import  numpy as np


class PasswordGen:

    lowerCase = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
        8: "i",
        9: "j",
        10:"k",
        11:"l",
        12:"m",
        13:"n",
        14:"o",
        15:"p",
        16:"q",
        17:"r",
        18:"s",
        19:"t",
        20:"u",
        21:"v",
        22:"w",
        23:"x",
        24:"y",
        25:"z"
    }
    capCase = {
        0:  "A",
        1:  "B",
        2:  "C",
        3:  "D",
        4:  "E",
        5:  "F",
        6:  "G",
        7:  "H",
        8:  "I",
        9:  "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z"
    }
    numbers = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9"
    }
    symbols = {
        0: "!",
        1: "¡",
        2: "?",
        3: "¿",
        4: "@",
        5: "/",
        6: "#",
        7: "$",
        8: "&",
        9: "€"
    }

    def __init__(self, length = 16, withmayus = True, withnumbers = True, withsymbols = True):
        self.length = length
        self.withmayus = withmayus
        self.withnumbres = withnumbers
        self.withsymbols = withsymbols
        self.iter = [
            self.lowerCase,
            self.capCase,
            self.numbers,
            self.symbols
        ]

        if self.withmayus == False:
            self.iter.remove(self.capCase)
        elif self.withnumbres == False:
            self.iter.remove(self.numbers)
        elif self.withsymbols == False:
            self.iter.remove(self.symbols)

        if self.length < 8 or self.length > 16:
            print("La contraseña debe tener entre 8 y 16 caracteres")

        else:
            self.generate()


    def generate(self):
        passw = ""
        #  for each slot in the password
        for i in range(0,self.length):
            n = np.random.randint(0,len(self.iter))
            group = self.iter[n]  # select one of the dicts randomly
            index = np.random.randint(0, len(group))
            char = group[index]
            passw = passw + char

        print(passw)

if __name__ == "__main__":
    gen = PasswordGen(length=16, withmayus=False)
    # passw = gen.generate()