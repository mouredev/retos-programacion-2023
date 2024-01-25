class Fibonacci:
    def is_perfect_square(self, num):
        """
        Check if a number is a perfect square.

        Args:
        num (int): The number to check.

        Returns:
        bool: True if the number is a perfect square, False otherwise.
        """
        square_root = int(num**0.5)
        return square_root * square_root == num

    def is_fibonacci_number(self, num):
        """
        Check if a number is a Fibonacci number.

        Args:
        num (int): The number to check.

        Returns:
        bool: True if the number is a Fibonacci number, False otherwise.
        """
        return self.is_perfect_square(5 * (num * num) + 4) or self.is_perfect_square(5 * (num * num) - 4)

def verify_number(num):
    """
    Verify if a number is prime, Fibonacci, and even, and print the results.

    Args:
    num (int): The number to verify.
    """
    results = [str(num)]

    is_prime = num > 1
    if is_prime:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

    results.append("prime" if is_prime else "not prime")

    is_fibonacci = Fibonacci().is_fibonacci_number(num)
    results.append("Fibonacci" if is_fibonacci else "not Fibonacci")

    results.append("even" if num % 2 == 0 else "odd")

    print(f"{results[0]} is {results[1]}, {results[2]}, and {results[3]}.")

verify_number(7)
