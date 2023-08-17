import random
def password ():
    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    num = ['1','2','3','4','5','6','7','8','9','0'] 
    simb = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']

    caracteres = mayus + minus + num + simb
    pasw = []

    for i in range(16):
        caracteres_random = random.choice(caracteres)
        pasw.append(caracteres_random)

    pasw = "".join(pasw)

    return pasw

def main():

    pasw = password()
    print ('Tú nueva contraseña es: ' , pasw)

if __name__ == '__main__':
    main()
