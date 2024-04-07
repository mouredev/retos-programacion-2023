class PseudoRandomGenerator:
    """
    Class for a pseudo-random number generator.
    """

    def __init__(self, seed):
        """
        Initialize the generator with a seed.

        Args:
            seed (int): The seed value for the generator.
        """
        self.state = seed

    def generate(self):
        """
        Generate a pseudo-random number between 0 and 100.

        Returns:
            int: The generated pseudo-random number.
        """
        a = 1664525
        c = 1013904223
        m = 2 ** 32
        self.state = (a * self.state + c) % m
        return self.state % 101

def main():
    """
    Main function to run the pseudo-random number generator.
    """
    seed = int(input("Enter a seed: "))
    generator = PseudoRandomGenerator(seed)

    for _ in range(10):
        random_number = generator.generate()
        print(random_number)

if __name__ == "__main__":
    main()
