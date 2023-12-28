import string, random

symbolsPool = string.punctuation
numbersPool = string.digits
upperPool = string.ascii_uppercase
lowerPool = string.ascii_lowercase

def main():
    generatedPass = ''
    configurations = {}
    print('\n\t\tPASSWORD CONFIGURATIONS\n\n')
    try:
        while(True):
            passInput = input('Password length? (8 or 16): ')
            passLength = int(passInput)
            if(passLength == 8 or passLength == 16):
                configurations['length'] = passLength
                print(f'Password Length: {passLength}')
                break
            else:
                print('Invalid Input')

        while(True):
            letterInput = str(input('Password with uppercase? (yes or no): '))
            boolInput = checkInput(letterInput) 
            if(type(boolInput) == bool):
                configurations['upLetters'] = boolInput
                break
            else:
                print('Invalid Input')
        
        while(True):
            numInput = str(input('Password with numbers? (yes or no): '))
            boolInput = checkInput(numInput)
            if(type(boolInput) == bool):
                configurations['numbers'] = boolInput
                break
            else:
                print('Invalid Input')
        
        while(True):
            symInput = str(input('Password with symbols? (yes or no): '))
            boolInput = checkInput(symInput)
            if(type(boolInput) == bool):
                configurations['symbols'] = boolInput
                break
            else:
                print('Invalid Input')

        generatedPass =  genPassword(configurations)
        print(f'Password Generated: {generatedPass}')

    except:
        print('Unexpected Error, try again later')
        exit(0)

def generateUpLetter(length):
    letters = ''
    if(length == 8):
        for i in range(0, 2):
            letters += random.choice(upperPool)
        return letters
    elif(length == 16):
        for i in range(0, 4):
            letters += random.choice(upperPool)
        return letters

def generateLowLetter(length):
    letters = ''
    if(length == 8):
        for i in range(0, 2):
            letters += random.choice(lowerPool)
        return letters
    elif(length == 16):
        for i in range(0, 4):
            letters += random.choice(lowerPool)
        return letters

def generateSymbol(length):
    symbols = ''
    if(length == 8):
        for i in range(0, 2):
            symbols += random.choice(symbolsPool)
        return symbols
    elif(length == 16):
        for i in range(0, 4):
            symbols += random.choice(symbolsPool)
        return symbols

def generateNumber(length):
    numbers = ''
    if(length == 8):
        for i in range(0, 2):
            numbers += random.choice(numbersPool)
        return numbers
    elif(length == 16):
        for i in range(0, 4):
            numbers += random.choice(numbersPool)
        return numbers

def checkInput(inputStr):
    if(inputStr == 'yes'):
        return True
    elif(inputStr == 'no'):
        return False
    else:
        return 0
    
def genPassword(confList):
    genPass8 = ''
    genPass16 = ''

    length = confList.get('length')
    lettCheck = confList.get('upLetters')
    numCheck = confList.get('numbers')
    symCheck = confList.get('symbols')

    if(length == 8):

        if(lettCheck):
            genPass8 += generateUpLetter(length)
            genPass8 += generateLowLetter(length)
        else:
            for i in range(0, 2):
                genPass8 += generateLowLetter(length)
        
        if(numCheck):
            genPass8 += generateNumber(length)
        else:
            genPass8 += generateLowLetter(length)

        if(symCheck):
            genPass8 += generateSymbol(length)
        else:
            genPass8 += generateLowLetter(length)

        return genPass8

    elif(length == 16):

        if(lettCheck):
            genPass16 += generateUpLetter(length)
            genPass16 += generateLowLetter(length)
        else:
            for i in range(0, 2):
                genPass16 += generateLowLetter(length)
        
        if(numCheck):
            genPass16 += generateNumber(length)
        else:
            genPass16 += generateLowLetter(length)

        if(symCheck):
            genPass16 += generateSymbol(length)
        else:
            genPass16 += generateLowLetter(length)

        return genPass16

    else:
        print('Unexpected Error, check the configurations')
        exit(0)

if __name__ == '__main__':
    main()