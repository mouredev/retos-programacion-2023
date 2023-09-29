from secrets import choice
import string


def generate_password(
    length: int, 
    include_caps=False, 
    include_numbers=False,
    include_symbols=False,
) -> str:
    if length < 8 or length > 16:
        raise ValueError("La longitud debe ser entre 8 y 16")
    
    characters = string.ascii_lowercase
    
    if include_caps:
        characters += string.ascii_uppercase
        
    if include_numbers:
        characters += string.digits
        
    if include_symbols:
        characters += string.punctuation
        
    return "".join(choice(characters) for _ in range(length))
    
    
if __name__ == "__main__":
    password_16 = generate_password(length=16, include_caps=True, include_numbers=True, include_symbols=True)
    assert len(password_16) == 16
    print(password_16)
    
    password_8 = generate_password(length=8, include_caps=True)
    assert len(password_8) == 8
    print(password_8)
    
    password_11 = generate_password(length=11, include_caps=True, include_numbers=True)
    assert len(password_11) == 11
    print(password_11)
    
    password_15 = generate_password(length=15, include_symbols=True)
    assert len(password_15) == 15
    print(password_15)