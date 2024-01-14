def print_multiplication_table(number):
    """
    Prints the multiplication table for the given number from 1 to 10.

    Args:
    - number (int): The number for which the multiplication table is generated.
    """
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    try:
        number = int(input("Enter a number to generate its multiplication table (1 to 10): "))

        if 1 <= number <= 10:
            print_multiplication_table(number)
        else:
            print("Error: The number must be in the range of 1 to 10.")
    except ValueError:
        print("Error: Enter a valid integer.")

if __name__ == "__main__":
    main()
