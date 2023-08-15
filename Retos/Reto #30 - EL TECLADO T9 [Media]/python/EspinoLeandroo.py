t9 = [" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def t9_to_text(input: str) -> str:
    message = ""
    
    if(input != ""):
        sequences = input.split("-")
        
        for number_sequence in sequences:
            number = int(number_sequence[0])
            
            if(len(number_sequence) <= len(t9[number])):
                message = message + t9[number][len(number_sequence)-1]
            else:
                message = "Error!\tInvalid sequence"
    else:
        message = "Error!\tInvalid Input"
    
    return message

print(t9_to_text("0-555-33-2-66-3-777-666-1111"))
print(t9_to_text(""))
print(t9_to_text("2222"))
print(t9_to_text("6-666-88-777-33-0-3-33-888"))
print(t9_to_text("6-676-88-777-33-3-33-888"))
print(t9_to_text("6-6a6-88-777-33-3-33-888"))