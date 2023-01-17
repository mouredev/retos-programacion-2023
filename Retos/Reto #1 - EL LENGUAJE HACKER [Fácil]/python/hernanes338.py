# Dictionary with the alphanumeric charcters conversion
dict = {
'a':'4', 
'b':"|3", 
'c':'[', 
'd':")", 
'e':"3", 
'f':"|=" ,
'g':"&", 
'h':"#" ,
'i':"1", 
'j':",_|", 
'k':">|", 
'l':"1", 
'm':"/\/\\",
'n':"^/", 
'o':"0", 
'p':"|*", 
'q':"(_,)", 
'r':"I2", 
's':"5", 
't':"7", 
'u':"(_)", 
'v':"\/", 
'w':"\/\/", 
'x':"><", 
'y':"j", 
'z':"2",
'1':"L", 
'2':"R", 
'3':"E", 
'4':"A", 
'5':"S", 
'6':"b", 
'7':"T", 
'8':"B", 
'9':"g", 
'0':"o"
}

# Insert the text to translate
input = input("Introduce un texto alfanumerico para traducirlo a \"lenguaje hacker\": ").lower() # convert to lowercase to follow the dictionary format

# Empty string to append translated characters
output = ""

# Loop over the input length
for i in range(len(input)):
    # Handling spaces
    if input[i] == " ": 
        output += " "
    # Append translated characters from the dictionary
    else:
        output += (dict[input[i]])

# Print the result of translating all alphanumeric characters
print(output)