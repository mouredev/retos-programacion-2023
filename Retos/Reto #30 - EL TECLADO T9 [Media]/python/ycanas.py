def T9Keyboard(sequence: str) -> str:
    characters = sequence.split('-')
    output = str()

    if T9Check(characters):
        for combination in characters:
            number = int(combination[0])
            key = keyboard[number]

            index = (len(combination) - 1) % len(key)
            output = output + key[index]
    
        return output.upper()
    
    return "Error"


def T9Check(characters: list()) -> bool:
    if not characters:
        return False
    
    for combination in characters:
        if not combination:
            return False
        
        reference = combination[0]

        for item in combination:
            if not item.isdigit() or not item == reference:
                return False
            
    return True


keyboard = (
    (' '),  (',', '.', '?', '!'),
    ('a', 'b', 'c'), ('d', 'e', 'f'),
    ('g', 'h', 'i'), ('j', 'k', 'l'),
    ('m', 'n', 'o'), ('p', 'q', 'r', 's'),
    ('t', 'u', 'v'), ('w', 'x', 'y', 'z'), 
)

print(T9Keyboard("999-2-444-777"))
print(T9Keyboard("6-666-88-777-33-0-3-33-888"))
print(T9Keyboard("6-676-88-777-33-3-33-888"))
print(T9Keyboard("6-6a6-88-777-33-3-33-888"))
print(T9Keyboard(""))
print(T9Keyboard("2222"))
