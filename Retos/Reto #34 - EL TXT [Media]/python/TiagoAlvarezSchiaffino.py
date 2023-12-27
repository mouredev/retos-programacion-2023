import os
from pathlib import Path


def ask_user_action() -> str:
    """
    Ask the user for the desired action.

    Returns:
        str: User's choice (A, W, Q).
    """
    while True:
        print("What do you want to do?")
        print("\tA - Keep writing on the existing file")
        print("\tW - Remove the content and start writing from the beginning")
        print("\tQ - Quit")
        action = input("Enter your choice (A/W/Q): ").upper()

        if action in ["A", "W", "Q"]:
            return action


def write_to_file(file_path: Path):
    """
    Write text to a file based on user interaction.

    Args:
        file_path (Path): Path to the file.
    """
    mode = "w" if not file_path.exists() else ask_user_action()

    with open(file_path, mode) as file:
        if mode == "A":
            with open(file_path, "r") as existing_file:
                print("Existing content:")
                print(existing_file.read())
        elif mode == "Q":
            print("Quitting the program.")
            return

        while True:
            user_text = input("Type a line to insert (type 'Q' to exit): ")
            
            if user_text.upper() == "Q":
                break

            file.write(f"{user_text}\n")

    print("File operation completed.")


def main():
    file_path = Path("text.txt")
    write_to_file(file_path)


if __name__ == "__main__":
    main()
