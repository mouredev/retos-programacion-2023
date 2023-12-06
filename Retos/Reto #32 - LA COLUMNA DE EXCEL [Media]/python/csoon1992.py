import string

letters: list = list(string.ascii_uppercase)
lettersCount: int = len(letters)

def getColumnNumberFromName(columnName: str) -> int:
    finalColumnNumber: int = 0
    
    try:
        for index, nameLetter in enumerate(columnName):
            
            ndx:int = index + 1
            letterIndex: int = letters.index(nameLetter) + 1
            
            if index != len(columnName) - 1:
                finalColumnNumber += (letterIndex * ndx * lettersCount)
            else:
                # if is looping the last letter from columnName, add its number
                finalColumnNumber += letters.index(nameLetter) + 1
                
            
    except ValueError:
        print("Column name not found.")
        
    return finalColumnNumber
    
print(getColumnNumberFromName('A'))
print(getColumnNumberFromName('Z'))    
print(getColumnNumberFromName('AA'))
print(getColumnNumberFromName('CA'))