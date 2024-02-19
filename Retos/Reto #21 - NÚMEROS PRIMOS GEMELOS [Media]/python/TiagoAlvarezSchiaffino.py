def is_prime(num: int) -> bool:
    """
    Check if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True

def twin_primes(max_range: int):
    """
    Find and display all pairs of twin prime numbers within a specific range.

    Args:
        max_range (int): The maximum limit of the range.

    Example:
        For max_range=20:
            (3, 5), (5, 7), (11, 13), (17, 19)
    """
    prime_numbers = [x for x in range(max_range) if is_prime(x)]
    twin_prime_pairs = []
    for first, second in zip(prime_numbers[:-1], prime_numbers[1:]):
        if second - first == 2:
            twin_prime_pairs.append(f"({first}, {second})")
    print(", ".join(twin_prime_pairs))

# Example
twin_primes(20)
