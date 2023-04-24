import random as r

def generatePassword(length, capital, numbers, symbols):
    if (length < 8):
        print("ERROR: Longitud demasiado corta")
    elif (length > 16):
        print("ERROR: Longitud demasiado larga")
    else:
        possibleCharacters = "abcdefghijklmnopqrstuvwxyz"
            
        if (capital == True):
            possibleCharacters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
        if (numbers == True):
            possibleCharacters += "0123456789"
                
        if (symbols == True):
            possibleCharacters += "-_/&%$|@#~¬?!<>"
        
        max_random_num = len(possibleCharacters)        
        passwd = "" * max_random_num
                
        for i in range(1, length):
            random_pos = r.randrange(0, max_random_num)
            passwd += str(possibleCharacters[random_pos])
            
        print("The password is: " + passwd)

generatePassword(10, False, False, False)
generatePassword(12, False, False, False)
generatePassword(14, False, False, True)
generatePassword(16, False, False, True)
generatePassword(9, False, True, False)
generatePassword(11, False, True, False)
generatePassword(13, False, True, True)
generatePassword(15, False, True, True)
generatePassword(8, True, False, False)
generatePassword(11, True, False, False)
generatePassword(14, True, False, True)
generatePassword(17, True, False, True)
generatePassword(15, True, True, False)
generatePassword(12, True, True, False)
generatePassword(9, True, True, True)
generatePassword(6, True, True, True)
