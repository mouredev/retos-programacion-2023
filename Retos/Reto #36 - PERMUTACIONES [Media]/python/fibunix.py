#  Crea un programa que sea capaz de generar e imprimir todas las 
#  permutaciones disponibles formadas por las letras de una palabra.
#  - Las palabras generadas no tienen por qué existir.
#  - Deben usarse todas las letras en cada permutación.
#  - Ejemplo: sol, slo, ols, osl, los, lso 


import unittest
import math

# -----------------------------------------------------------------------------
# WordPermutation Class
# ----------------------------------------------------------------------------- 

class WordPermutation:
    ''''
    Based on a given word generate all possible permutations 
    of the characters that composes that word.
    Pre-condition: The word is intended to be a single word, if it's a phrase it will be treated as a single word.
    '''
    def __init__(self, word) -> None:
        self.word = word
        self.permutations = set()


    def generate_permutations(self):
        ''''
        Generates all possible permutations for the given word
        '''
        self._permutations_recursive('', self.word)
        return self.permutations


    def _permutations_recursive(self, current, remaining):

        if len(remaining) == 0 :
            self.permutations.add(current)
            return
        
        for i in range(len(remaining)):
            next_char = remaining[i]
            new_current = current + next_char
            new_remaining = remaining[:i] + remaining[i + 1:]
            self._permutations_recursive(new_current, new_remaining)


# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------

class WordPermutationTestSuite(unittest.TestCase):
    ''''
    Test Case for word permutation class
    '''
    def setUp(self) -> None:
        self.word = 'abcd'
        self.word_permutation = WordPermutation(word=self.word)

        return super().setUp()


    def test_initialization(self):
        # assert
        self.assertEqual(self.word_permutation.word, self.word)

    
    def test_permutations_contains_word(self):
        # act
        permutations = self.word_permutation.generate_permutations()
        # assert
        self.assertIn(self.word, permutations)

    
    def test_permutations_simple_aa(self):
        word = 'aa'
        self.word_permutation = WordPermutation(word)
        # act
        permutations = self.word_permutation.generate_permutations()
        # assert
        self.assertIn(word, permutations)


    def test_permutations_simple_aa_count(self):
        word = 'aa'
        self.word_permutation = WordPermutation(word)
        # act
        permutations = self.word_permutation.generate_permutations()
        # assert
        self.assertEqual(len(permutations), 1)


    def test_permutations_count_unique_chars(self):
        # Act
        permutations = self.word_permutation.generate_permutations()
        # Assert
        self.assertEqual(len(permutations), math.factorial(len(self.word)))

    
    def test_permutations_count_repeated_chars(self):
        # Arrange
        word = 'abcdeee'
        self.word_permutation = WordPermutation(word)
        # Act 
        self.word_permutation.generate_permutations()
        # Assert -> P(7) / P(3)
        self.assertEqual(len(self.word_permutation.permutations), 840)


    def test_random_permutation_in_permutations(self):
        # Arrange
        word = 'asdfghi'
        self.word_permutation = WordPermutation(word)
        # Act 
        self.word_permutation.generate_permutations()
        # Assert
        self.assertIn('ihgfdsa', self.word_permutation.permutations)
        


# -----------------------------------------------------------------------------
# Main Program / Unit Test Run / Main Execution
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()