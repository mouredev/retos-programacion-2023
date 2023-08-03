import math


def is_prime_number(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True


def is_fibonacci_number(n: int) -> bool:
    """
    n is in the Fibonacci sequence if ((5 * n^2) + 4) or ((5 * n^2) - 4) is a perfect square
    """
    
    def is_perfect_square(x: int) -> bool:
        """
        Returns wheter this number is a perfect square
        
        """
        s = int(math.sqrt(x))
        return s * s == x
    
    to_eval = (5 * n * n)
    
    return is_perfect_square(to_eval + 4) or is_perfect_square(to_eval - 4)


def is_even_number(n: int) -> bool:
    return n % 2 == 0


def evaluate_number(n: int) -> bool:
    is_prime = is_prime_number(n)
    is_fibonacci = is_fibonacci_number(n)
    is_even = is_even_number(n)
    
    result = f"{n} "
    result += "es primo, " if is_prime else "no es primo, "
    result += "es fibonacci, " if is_fibonacci else "no es fibonacci, "
    result += "es par" if is_even else "es impar"
    
    print(result)
    


if __name__ == "__main__":
    evaluate_number(2)
    evaluate_number(7)
    evaluate_number(8)
    evaluate_number(9)