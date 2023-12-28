#Get input from user
nat = input("Texto a traducir: ").lower()
#Definir función Leetify
def leetify (txt):
    al = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    ah = [" ", "4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\/", "\/\/", "><", "j", "2", "L", "R", "E", "A", "S", "b", "T", "B", "g", "o"]
    trad = ""
    for i in txt:
        x = 0
        for j in al:
            if j == i:
                trad = trad + ah[x]
            else:
                x+=1
    return trad
print (leetify(nat))