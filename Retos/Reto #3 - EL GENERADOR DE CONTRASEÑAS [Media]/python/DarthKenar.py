import random
class Passwords():
    selected_characters={
            '1':'upper',
            '2':'lower',
            '3':'number',
            '4':'especial'}
    characters={
            "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "lower": "abcdefghijklmnopqrstuvwxyz",
            "number": "12345678901234567890",
            "especial": "!@/#$%&_*-](}@[){?\'"}
    
    def __init__(self, length, selected, *args, **kwargs):
        """Creates an object of type Passwords containing the necessary attributes to perform the corresponding password operations (e.g. generate password).

        Args:
            length (int): "Length of your password: between 8 and 16 characters."\n
            selected (str): "Choose the options to combine:\n\t\t1: Upper\n\t\t2: Lower\n\t\t3: Number\n\t\t4: Especial\n\t\t Example:13 --> Generated password -> Upper + Number = R9539EMY25"
        """

        self.length = length
        self.selected = selected
    
    def generate(self)->str:
        All = "".join(self.characters[self.selected_characters[i]] for i in self.selected)
        password = "".join(random.choice(All) for i in range(self.length))
        self.password = password
        print(self.password)

contraseña = Passwords(10,"13")
contraseña.generate()
