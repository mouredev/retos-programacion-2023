import random
import string

def generate_password(lenght, lower_case, upper_case , digits, special_chars):
    chars_lower = string.ascii_lowercase
    chars_upper = string.ascii_uppercase
    chars_digits = string.digits
    chars_special = string.punctuation
    
    try:
        lenght = int(lenght)
    except:
        print("ERROR! Add an integer value in the parameter 'lenght'.")
        exit()
    
    password = ""
    selected_chars = ""
    if lower_case:
        selected_chars += chars_lower
    if upper_case:
        selected_chars += chars_upper
    if digits:
        selected_chars += chars_digits
    if special_chars:
        selected_chars += chars_special
    
    if not selected_chars:
        print("You must add one type of character (Remember using True/False). Try again.")
        exit()
    
    for _ in range(lenght):
        char = random.choice(selected_chars)
        password += char
        
    print(password)

generate_password(12, True, True, True, False)