"""
Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA

Crea 3 funciones, cada una encargada de detectar si una cadena de
texto es un heterograma, un isograma o un pangrama.

Debes buscar la definición de cada uno de estos términos.
"""

from collections import Counter
from re import sub
from string import ascii_lowercase
from unicodedata import normalize


class TextAnalyzer:
    """
    A class that contains methods for text analysis.
    """
    def is_heterogram(self, text:str) -> bool:
        """
        Determines whether a string is a heterogram, meaning that it does not
        contain any repeated letters.

        Args:
            text (str): The word or phrase to check.

        Returns:
            bool: True if the word or phrase is a heterogram, False otherwise.
        """
        normalized_text = self.normalize_string(text)
        char_counter = Counter(normalized_text)
        return len(char_counter) == len(normalized_text)

    def is_isogram(self, text:str) -> bool:
        """
        Checks if a given word or phrase is an isogram, i.e., a word or phrase
        in which each letter appears the same number of times.

        Args:
            text (str): The word or phrase to check.
        Returns:
            bool: True if the word or phrase is an isogram, False otherwise.
        """
        normalized_text = self.normalize_string(text)
        char_counter = Counter(normalized_text)
        char_freq = [value for char, value in char_counter.most_common()]
        return min(char_freq) == max(char_freq)
        
    def is_pangram(self, text:str) -> bool:
        """
        Check if a given text is a pangram. A pangram is a sentence or phrase
        that contains all the letters of the alphabet at least once. 

        Args:
            text (str): The text to check.

        Returns:
            bool: True if the text is a pangram, False otherwise.
        """
        normalized_text = self.normalize_string(text)
        return set(normalized_text) == set(ascii_lowercase)
        
        
        
    def normalize_string(self, text:str) -> str:
        """
        Normalizes a string by removing diacritical marks (e.g. accents,
        umlauts), spaces and non-alphanumeric characters.
        
        Args:
            text (str): A string to normalize.

        Returns:
            str: The normalized string.
        """
        # Step 1: Transform text into a lowercase string and remove spaces
        # Example: Buen día, mundo! -> buendía,mundo!
        text_without_spaces = text.lower().replace(' ', '')
        
        # Step 2: Applies a canonical unicode decomposition
        # Example: buendía,mundo! -> buendi\u0301a,mundo!
        canonical_unicode_text = normalize(
            'NFKD',
            text_without_spaces
        )
        
        # Step 4: Transforms the canonical text into an ASCII byte string
        # Example: buendi\u0301a,mundo! -> (byte) buendia,mundo!
        ascii_bytes_string = canonical_unicode_text.encode(
            'ASCII',
            'ignore'
        )
        
        # Step 5: Transforms the ACII bytes string into a regular Python string
        # Example: (byte) buendiamundo -> buendiamundo
        text_without_diacritics = ascii_bytes_string.decode('ASCII')
        
        # Step 6: Remove all non-alphanumeric characters
        # Example: buendiamundo! -> buendiamundo
        text_without_symbols = sub(
            pattern=r'[^a-z\s]',
            repl='',
            string=text_without_diacritics
        )
        
        return text_without_symbols

if __name__ == '__main__':
    analyzer = TextAnalyzer()
    
    # Heterogram
    print(analyzer.is_heterogram('El Piso!'))
    print(analyzer.is_heterogram('perro'))
    
    # Isogram
    print(analyzer.is_isogram('papa'))
    print(analyzer.is_isogram('para'))
    
    # Pangram
    pangram = ('Un jugoso zumo de piña y kiwi bien frío es exquisito y'
               ' no lleva alcohol.')
    not_pangram = 'perro'
    print(analyzer.is_pangram(pangram))
    print(analyzer.is_pangram(not_pangram))
