import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    # Crea una lista de caracteres para elegir
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
  
    # Elegir caracteres aleatorios de la lista de caracteres
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Llamada a la función con diferentes parámetros
print(generate_password(12, True, True, True))
print(generate_password(10, False, True, False))
print(generate_password(8, True, False, True))
