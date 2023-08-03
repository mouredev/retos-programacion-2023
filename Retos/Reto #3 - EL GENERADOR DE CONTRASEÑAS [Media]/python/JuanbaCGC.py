import string
import random

UPPERCASE = list(string.ascii_uppercase)
LOWERCASE = list(string.ascii_lowercase)
NUMBERS = list(range(10))
SYMBOLS = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", ";", ":", ",", ".", "<", ">", "/", "?", "|", "\\",
    "'", "\"", "`", "~"
]

def get_parameters():
    length = get_length()
    capital_leters = get_response("Do you want capital leters? Enter Y or N: ")
    numbers = get_response("Do you want numbers? Enter Y or N: ")
    symbols = get_response("Do you want symbols? Enter Y or N: ")
    return length,[capital_leters,numbers,symbols]

def get_length():
    length = -1
    while(length < 8 or length > 16):
        try:
            length = int(input("Enter the  password length (between 8 and 16): "))
        except ValueError:
            print("You have to introduce a number")
    return length

def get_response(question):
    while True:
        response = input(question).lower()
        if response == "y" or response == "n":
            break
    return response.lower() == "y"

def shuffle(text):
    character_list = list(text)
    random.shuffle(character_list)
    return "".join(character_list)


def get_password(parameters):
    password = ""
    characters = []
    for index,item in enumerate(parameters[1]):
        if item is True:
            if index == 0:
                password += random.choice(UPPERCASE)
                characters += UPPERCASE
            if index == 1:
                password += str(random.choice(NUMBERS))
                characters += NUMBERS
            if index == 2:
                password += random.choice(SYMBOLS)
                characters += SYMBOLS
    characters += LOWERCASE
    while len(password) < parameters[0]:
        password += str(random.choice(characters))

    return shuffle(password)


print("Welcome to the password generator.")
parameters = get_parameters()
print("Your new password is:",get_password(parameters))