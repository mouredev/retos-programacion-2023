import random

hello_text ="""Welcome to

            *******     **     ********     *******  *******   ***    **
            *******    *  *    ***          *        **        ** *   **
            *******   ******   ********     *  ****  *******   **  *  **
            ***      ***  ***       ***     *    **  **        **   * **  
            ***     ****  **** ********     *******  *******   **    ***
_________________________________________________________________________________\n
"""

print(hello_text)

while True:
    pass_length = int(input("Select number of characters (min. 8 - max. 16): "))
    if pass_length < 8:
        print("Pass too short, please select a value between 8 and 16")
    elif pass_length > 16:
        print("Pass too long, please select a value between 8 and 16")
    else:
        break

while True:
    include_upper = str(input("Would you like to include capital letters? (y - n): ")).lower()
    if include_upper == "y" or include_upper == "n":
        break
    else:
        print("Wrong input, please select y or n")


while True:
    include_numbers = str(input("Would you like to include numbers? (y - n): ")).lower()
    if include_numbers == "y" or include_numbers == "n":
        break
    else:
        print("Wrong input, please select y or n")

while True:
    include_symbols = str(input("Would you like to include simbols? (y - n): ")).lower()
    if include_symbols == "y" or include_symbols == "n":
        break
    else:
        print("Wrong input, please select y or n")

passwd = ""
full_string = "abcdefghijklmnopqrstuvwxyz"
if include_numbers == "y":
    full_string += "0123456789"
if  include_upper == "y":
    full_string += "abcdefghijklmnopqrstuvwxyz".upper()
if include_symbols == "y":
    full_string += "~!@#$%^&*()_-+={[}]|:;<,>.?/"

max_random_num = len(full_string)

for i in range(0, pass_length):
    random_pos = random.randrange(0, max_random_num)
    passwd += str(full_string[random_pos])

print("+-------------------------------------------------")
print("| Generated password is: " + passwd)
print("+-------------------------------------------------")
