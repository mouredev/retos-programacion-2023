
def isHeterogram(string : str) -> bool: #This function evaluates for both heterograms and isogram. 
    letters = set()

    for char in string:
        if char in letters:
            return False
        else: 
            letters.add(char)

    return True

def isPangram(string : str) -> bool:
    
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    letters = set(filter(str.isalpha, string.lower())) # Convert the string to lower characters and remove non-alphabetical characters

    return letters == alphabet # True if there's at least one of each elements in the set False otherwise



if __name__ == '__main__':
    string_test_1 = "The quick brown fox jumps over the lazy dog"
    string_test_2 = "murcielago"
    result = ""
    result += "Es heterograma " if isHeterogram(string_test_2) else "No es heterograma "
    result += "y es panagrama." if isPangram(string_test_2) else "y no es panagrama"
    print(result)