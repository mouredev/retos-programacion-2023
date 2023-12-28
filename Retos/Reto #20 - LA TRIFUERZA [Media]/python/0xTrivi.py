"""
Solution author: https://github.com/0xTrivi
Challenge number 20 of @Mouredev
Source repository: https://github.com/mouredev/retos-programacion-2023

Statement:

The new "The Legend of Zelda: Tears of the Kingdom" is now available!
Create a program that draws a Triforce from "Zelda" using asterisks.

You should provide the number of rows for the triangles with a positive integer (n).
Each triangle will calculate its largest row using the formula 2n-1.
Example: Triforce 2

"""

def print_spaces(number: int):
    """Prints in a line of text the number of spaces set."""
    for j in range(number):
        print("",end=' ')


def print_asterisks(number: int):
    """Prints on a line of text the number of asterisks set 
    and colors them yellow."""
    for k in range(number):
        print("\033[33m*\033[0m", end=" ")


def print_Power(size: int, lastRowSize: int):
    """Print the upper Triforce triangle."""
    for i in range(size):
        print_spaces(lastRowSize-i)
        print_asterisks(i+1)
        print_spaces(lastRowSize-i)
        print(" ")


def print_Wisdom_and_Courage(numberOfRows: int, lastRowSize: int):
    """Print the two lower triangles of the Triforce."""
    for i in range(numberOfRows):
        print_spaces((numberOfRows-i)-1)
        print_asterisks(i+1)
        print_spaces((lastRowSize-(2*i)-1))
        print_asterisks(i+1)
        print_spaces((numberOfRows-i)-1)
        print(" ")


def print_Triforce(numberOfRows: int, lastRowSize: int):
    """Prints a yellow Triforce with the number of rows 
    established for each triangle."""
    print_Power(numberOfRows, lastRowSize)
    print_Wisdom_and_Courage(numberOfRows, lastRowSize)
    print(" ")


def what_size() -> int:
    """Allows the user to set the number of rows for each 
    triangle of the Triforce."""
    size = False
    print("How big do you want your triforce?:")
    while size == False:      
        number = int(input(" "))
        print(" ")    
        if number > 0 and type(number) == int:
            size = True
            print("")
        else:
            print("Please! write a positive integer number:")
    print("")
    return number


def print_title():
    """Print the tittle to the program."""
    print("""
                  T~~
                  |
                /"|
        T~~     |'|  T~~
    T~~ |     T~ WWWW|
    |  /"\    |  |  |/\T~~
    /"\ WWW  /"\ |' |WW|  T~~
    WWWWW/\| /   \|'/\|/"'|
    |   /__\/]WWW[\/__\WWWW
    |"  WWWW'|I_I|'WWWW'  |
    |   |' |/  -  \|' |'  |
    |'  |  |LI=H=LI|' |   |
    |   |' | |[_]| |  |'  |
    |   |  |_|###|_|  |   |
    '---'--'-/___\-'--'---'
    """)

def print_end():
    """Print the farewell to the program."""
    print("""
    ⢦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤
    ⠘⣿⣿⣿⣷⣦⣄⣀⠀⢠⠔⠀⢀⡼⠿⠿⢆⠀⠀⠲⣄⠀⣀⣠⣴⣾⣿⣿⣿⠇
    ⠀⠈⠉⠉⠛⠛⠻⠿⢿⣿⠀⢀⣾⣷⡀⢀⣾⣷⡀⠀⣿⡿⠿⠿⠛⠛⠉⠉⠁⠀
    ⠀⠀⣤⣤⣶⣶⣶⣶⣶⣿⣆⠈⠉⠉⠉⠉⠉⠉⠉⢠⣿⣶⣶⣶⣶⣶⣤⣤⠀⠀
    ⠀⠀⠘⣿⡿⠟⠛⠉⣡⣿⣿⣷⣤⠀⢠⣆⠀⣤⣶⣿⣿⣬⡉⠛⠻⠿⣿⠇⠀⠀
    ⠀⠀⠀⠀⠀⢀⣴⣿⡿⢋⣿⣿⠛⢠⣿⣿⡄⠛⢿⣿⡘⢿⣿⣦⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠻⠏⠀⣸⣿⡇⢀⠻⣿⣿⠟⣀⠸⣿⣇⠀⠙⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢠⡟⠁⣿⣿⠀⠻⣆⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢟⠉⠙⠓⠀⠘⠏⠀⠘⠟⠉⡻⠋⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("")
    print("Take care of Hyrule!")
    print("")


def main():
    """Allows the user to print one or more Triforce."""
    finish = False

    print_title()
    while finish == False:
        sizeTriforce = what_size()
        print_Triforce(sizeTriforce, (sizeTriforce*2)-1)
        validateOption = False
        while validateOption == False:
            print("Do you want to generate another Triforce?")
            print("1 - Yes")
            print("2 - No")
            option = str(input(" "))
            if option == "2" or option == "n" or option == "N" or option == "No":
                finish = True
                validateOption = True
                print("")
            elif option == "1" or option == "y" or option == "Y" or option == "Yes":  
                print("")
                validateOption = True
            else:
                print("Please! write a correct option.")

    print_end()



if __name__ == "__main__":
    main()

    