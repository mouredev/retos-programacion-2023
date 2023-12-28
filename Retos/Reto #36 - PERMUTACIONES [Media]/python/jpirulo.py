class PermutationsGenerator:
    def __init__(self, word):
        self.word = word

    def generate_permutations(self):
        permutations = self._generate_permutations(self.word)
        return permutations

    def _generate_permutations(self, word):
        if len(word) == 0:
            return [""]
        permutations = []
        for i in range(len(word)):
            current_letter = word[i]
            remaining_letters = word[:i] + word[i+1:]
            sub_permutations = self._generate_permutations(remaining_letters)
            for sub_permutation in sub_permutations:
                permutations.append(current_letter + sub_permutation)
        return permutations

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    generator = PermutationsGenerator(palabra)
    permutations = generator.generate_permutations()
    for permutation in permutations:
        print(permutation)
