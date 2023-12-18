import string
import secrets

def password_generator(user_length, upper_case, numbers, symbols):
    """
    Generate a random password based on user-defined parameters.

    Args:
    user_length (int): Length of the password.
    upper_case (bool): Include uppercase letters or not.
    numbers (bool): Include numbers or not.
    symbols (bool): Include symbols or not.

    Returns:
    str: Generated password.
    """
    characters = string.ascii_lowercase
    if upper_case:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(user_length))
        if (
            any(c in string.ascii_lowercase for c in password) and
            any(c in string.ascii_uppercase for c in password) and
            any(c in string.digits for c in password) and
            any(c in string.punctuation for c in password)
        ):
            return password

def get_user_input():
    """
    Get user input for password generation parameters.

    Returns:
    tuple: Password generation parameters (user_length, upper_case, numbers, symbols).
    """
    try:
        user_length = int(input("Enter the password length (between 8 and 16): "))
        if not (8 <= user_length <= 16):
            print("Warning: Length automatically adjusted to 8 (minimum) or 16 (maximum).")
    except ValueError:
        print("Error. The password must be a number between 8 and 16.")
        return get_user_input()

    upper_case = input("Include uppercase letters? (Yes/No): ").lower()
    numbers = input("Include numbers? (Yes/No): ").lower()
    symbols = input("Include symbols? (Yes/No)").lower()

    if upper_case not in {'yes', 'no'}:
        print("Error: Respond with 'Yes' or 'No' to include uppercase letters.")
        return get_user_input()

    if numbers not in {'yes', 'no'}:
        print("Error: Respond with 'Yes' or 'No' to include numbers.")
        return get_user_input()

    if symbols not in {'yes', 'no'}:
        print("Error: Respond with 'Yes' or 'No' to include symbols.")
        return get_user_input()

    upper_case = upper_case == 'yes'
    numbers = numbers == 'yes'
    symbols = symbols == 'yes'

    return user_length, upper_case, numbers, symbols

if __name__ == "__main__":
    print("Random Password Generator")
    user_input = get_user_input()
    password = password_generator(*user_input)
    print(f"Your generated password is: {password}")