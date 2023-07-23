def getinfiltrate(text_one:str, text_two:str):
    lenOne = len(text_one)
    lenTwo = len(text_two)
    result = []

    if lenOne!=lenTwo:
        return "The text strings must have the same length"

    for i in range(lenOne):
        if text_one[i] != text_two[i]:
            result.append(text_two[i])

    differences = len(result)
    difference_percentage = int(differences*100 / lenOne)

    if difference_percentage>50:
        return f"The text strings are {difference_percentage}%  different"

    return result

print( getinfiltrate("This is a text", "This is the tex") ) # The text strings must have the same length
print( getinfiltrate("This is a test", "This is a test") ) # []
print( getinfiltrate("I'm AnzurezDev", "I.m AnzurezDEV") ) # ['.', 'E', 'V']
print( getinfiltrate("This my test 1", "The first test") ) # The text strings are 78%  different