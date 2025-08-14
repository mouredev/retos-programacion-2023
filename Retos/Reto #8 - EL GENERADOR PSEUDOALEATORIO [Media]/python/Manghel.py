"""
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del
lenguaje de programación seleccionado.

Es más complicado de lo que parece...
"""

from datetime import datetime
from typing import Optional

def random_number_generator(
        seed: Optional[int] = None,
        *,
        count: int = 100,
        a: int = 1664525,
        c: int = 1013904223,
        m: int = 101):
    """
    Generates a sequence of pseudo-random numbers between 0 and 100 
    using a linear congruential generator algorithm (LCG).

    Args:
        seed (Optional[int]): Initial seed for the generator. If not 
        provided, the current microsecond is used.
        count (int): Number of random numbers to generate (default is 100).
        a (int): Multiplier constant for the algorithm (default is 1664525).
        c (int): Increment constant for the algorithm (default is 1013904223).
        m (int): Modulus to limit the range of numbers (default is 101).

    Yields:
        int: Pseudo-random number in the range [0, 100].
    """

    if seed is None:
        seed = datetime.now().microsecond % m

    x = seed
    for _ in range(count):
        x = (a * x + c) % m
        yield x


if __name__ == "__main__":
    for num in random_number_generator():
        print(num)
