def pythagorean_triples(max_num: int) -> list:
    """
    Finds Pythagorean triples less than or equal to the given number.

    Args:
    - max_num (int): The maximum value for the elements in the triple.

    Returns:
    - list: A list of tuples representing Pythagorean triples.
    """
    triples = []

    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):
            ab_squared = a**2 + b**2
            c = int(ab_squared**0.5)
            if c > max_num:
                break
            if c**2 == ab_squared:
                triples.append((a, b, c))

    return triples

max_value = 20
result = pythagorean_triples(max_value)
print(result)
