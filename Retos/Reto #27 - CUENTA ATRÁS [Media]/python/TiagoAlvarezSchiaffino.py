import time

def countdown(start: int, seconds: int):
    """
    Perform a countdown starting from a given number with a specified interval.

    Args:
        start (int): The starting number for the countdown.
        seconds (int): The number of seconds between each count.

    Raises:
        ValueError: If either start or seconds is not a positive integer.

    Returns:
        None
    """
    if not isinstance(start, int) or not isinstance(seconds, int):
        raise ValueError("Both parameters must be integers.")
    
    if start <= 0 or seconds <= 0:
        raise ValueError("Both parameters must be positive integers greater than zero.")
    
    for num in range(start, -1, -1):
        print(num)
        time.sleep(seconds)
    
    print("Countdown completed!")

def get_positive_integer(prompt: str) -> int:
    """
    Get a positive integer from the user.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the countdown.")

    start_number = get_positive_integer("Enter the number to start the countdown from: ")
    seconds_interval = get_positive_integer("Enter the seconds between each count: ")

    countdown(start_number, seconds_interval)

if __name__ == "__main__":
    main()
