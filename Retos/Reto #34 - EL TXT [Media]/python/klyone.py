#!/usr/bin/env python3

import os.path

TXT_FILE_NAME = "input.txt"

if __name__ == "__main__":
    file_exists = os.path.exists(TXT_FILE_NAME)

    if not file_exists:
        append = False
    else:
        file_is_file = os.path.isfile(TXT_FILE_NAME)
        if not file_is_file:
            print("Error: input.txt exists but is not a file")
            exit(1)

        append = input("Do you want to append data to the file?: ")

        if append.lower() == "yes":
            append = True
            file = open(TXT_FILE_NAME, "r")
            print(file.read())
            file.close()
        else:
            append = False

    file = open(TXT_FILE_NAME, "a" if append else "w")

    quit = False
    while not quit:
        sentence = input("Next setence (@#quit to exit): ")
        if sentence == "@#quit":
            quit = True
        else:
            file.write(sentence)
            file.write("\n")

    file.close()
