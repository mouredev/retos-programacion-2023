class TextDetector:

  def __init__(self, word: str):
    self.word = word
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def is_isograma(self):
    """
        Checks if a letter repeats within the word.
        Returns True if it's an isogram, otherwise False.
        """
    seen_letters = set()

    for letter in self.word.lower():
      if letter.isalpha():
        if letter in seen_letters:
          return False
        seen_letters.add(letter)
      else:
        return False
    return True

  def is_heterogram(self):
    """
        Checks if the word is a heterogram.
        Returns True if it's a heterogram, otherwise False.
        """
    unique_letters = []

    for letter in self.word.lower():
      if letter.isalpha():
        if letter in unique_letters:
          return False
        unique_letters.append(letter)
      else:
        return False
    return True

  def is_pangrama(self):
    """
        Checks if the word is a pangram.
        Returns True if it's a pangram, otherwise False.
        """
    arr_letters = []

    for letter in self.word.lower():
      if letter in self.alphabet and letter not in arr_letters:
        arr_letters.append(letter)

    return len(arr_letters) == len(self.alphabet)


# Create an instance and use its methods.
objeto = TextDetector("Luz")
print("The word is an isogram ✅" if objeto.is_isograma(
) else "The word is not an isogram ❌")

# Create another instance and use its methods.
objeto2 = TextDetector("Loco")
print("It's a heterogram ✅" if objeto2.is_heterogram(
) else "It's not a heterogram ❌")

# Create another instance and use its methods.
objeto3 = TextDetector("Loco de que no puede")
print("It's a pangram ✅" if objeto3.is_pangrama() else "It's not a pangram ❌")
