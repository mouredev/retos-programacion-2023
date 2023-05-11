
def random_numbers(seed : int, a : int, c : int, m : int, length : int, out_range : int = 100) -> list[int]:
    """
    Using the linear congruential method: 

    Xn+1 = (aXn + c) mod m

    Where:

        Xn is the current value in the sequence
        Xn+1 is the next value in the sequence
        a, c, and m are constants that determine the behavior of the algorithm

    """
    current_value = seed
    numbers = []

    for i in range(length):
        next_value = (a * current_value + c) % m
        current_value = next_value
        current_value = current_value % out_range # Map the value to the desired output range.
        numbers.append(current_value)

    return numbers

if __name__ == '__main__':
    seed = 7952
    a = 1459
    c = 1235
    m = 2**32

    generated_numbers = random_numbers(seed, a, c, m, 10, 100)
    print(generated_numbers)