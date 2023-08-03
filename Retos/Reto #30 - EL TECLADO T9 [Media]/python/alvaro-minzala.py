def t9_to_text(sequence: str) -> str:
    
    if check_t9(sequence):

        t9 = [" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

        text = ""

        for number_sequence in sequence.split("-"):

            number = int(number_sequence[0])
            key = t9[number]
            text += key[(len(number_sequence) - 1) % len(key)]

        return text
    
    return "error"

def check_t9(sequence: str) -> bool:
    if not sequence:
        return False
    
    for number_sequence in sequence.split("-"):

        reference = number_sequence[0]

        for item in number_sequence:
            if not item.isdigit() or item != reference:
                return False
            
            return True
        
print(t9_to_text("2-555-888-2-777-666"))