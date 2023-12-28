import math

def test_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False        

def test_even(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_fibonacci(n):
    n_plus = 5 * n * n + 4
    n_minus = 5 * n * n - 4
    
    if is_perfect_square(n_plus) or is_perfect_square(n_minus):
        return True
    else:
        return False


def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number       


def test_pair_even_fibonacci(n):
    if n > 1:
        pair = test_pair(n)
        even = test_even(n)
        fibonacci = test_fibonacci(n)
        print("Result for => " + str(n) + " pair: " + str(pair) + " | even: " + str(even) + " | fibonacci: " + str(fibonacci))
    else:
        print("Please enter a number greater than 1")

test_pair_even_fibonacci(2)
test_pair_even_fibonacci(3)
test_pair_even_fibonacci(4)
test_pair_even_fibonacci(5)
test_pair_even_fibonacci(6)
test_pair_even_fibonacci(7)
test_pair_even_fibonacci(8)
test_pair_even_fibonacci(9)
test_pair_even_fibonacci(-2)
test_pair_even_fibonacci(0)




