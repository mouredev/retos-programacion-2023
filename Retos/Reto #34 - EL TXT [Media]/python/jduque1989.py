import os


def write_file(filename):

    with open(filename, "a") as file:
        while True:
            line = input("Enter a line of text: ")
            if line == "":
                break
            file.write(line + "\n")


def erase_file(filename):
    with open(filename, "w") as file:
        file.write("")


# get files in directory

files_in_directory = os.listdir()

# Filter the list to only show .txt files
text_files = [file for file in files_in_directory if file.endswith(".txt")]

if text_files:
    print("The following .txt files are in the current directory:")
    for idx, file in enumerate(text_files, 1):
        print(f"{idx}. {file}")
    choise = int(input("Enter the number of the file you want to edit: "))
    filename = text_files[choise - 1]
    action = input("Write (w) or erase (e)?: ").lower()
    if action == "w":
        write_file(filename)
    elif action == "e":
        erase_file(filename)
        print(f"Content of {filename} has been cleared!")
        write_file(filename)
else:
    print("No .txt files found in the current directory.")
    print("We're going to create one for you.")
    filename = input("What do you want to name the file? ")
    filename = filename + ".txt"
    with open(filename, "w") as f:
        pass
    write_file(filename)
