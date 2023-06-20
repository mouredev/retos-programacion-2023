import unittest
import random
from enum import Enum

# -----------------------------------------------------------------------------
# GuessGame
# -----------------------------------------------------------------------------
class GameStatus(Enum):
  IN_PROGRESS = 1
  LOST = 2
  WON = 3


class GuessGame:
  def __init__(self, word, attempts=3, char="_") -> None:
    self.original_word = word
    self.word = word
    self.attempts = attempts
    self.char = char
    self.status = GameStatus.IN_PROGRESS


  def hide_letters(self):
    word_len = len(self.original_word)
    hide_upto = round(word_len * 0.6)

    # replace the letter with a _
    while hide_upto > 0:
        random_letter = random.choice(self.word)
        hide_upto -= 1
        self.word = self.word.replace(random_letter, self.char, 1)

  def take_guess(self, guess):
    
    self.validate_guess(guess)
    
    if guess == self.original_word:
      self.status = GameStatus.WON
      self.word = self.original_word
      return
    elif len(guess) > 1:
      self._decrease_attempts()
      return
    
    if guess not in self.original_word:
      self._decrease_attempts()
      return
    
    # if we are here then there is a match for the guess char
    for i in range(len(self.original_word)):
      if self.original_word[i] == guess:
        self.word = self.word[:i] + guess + self.word[i+1:]

    if self.original_word == self.word:
      self.status = GameStatus.WON

  
  def validate_guess(self, guess):
    if self.status != GameStatus.IN_PROGRESS:
      raise Exception("The game finished")
    
    guess_len = len(guess)
    word_len = len(self.word)

    if guess_len > word_len  or (guess_len > 1 and guess_len < word_len):
      raise Exception("Invalid argument")
    

  def _decrease_attempts(self):
    self.attempts -= 1
    if self.attempts == 0:
      self.status = GameStatus.LOST

# -----------------------------------------------------------------------------\
# Game Manager
# -----------------------------------------------------------------------------
def manager():
  words = ["github", "renacimiento", "development", "plataforma"]
  word = random.choice(words)

  guess_game = GuessGame(word, attempts=3)
  guess_game.hide_letters()

  print(guess_game.word)
  print(f"Attempts: {guess_game.attempts}")
  while guess_game.status == GameStatus.IN_PROGRESS:
    guess = input("Please enter your guess: ")
    try:
      guess_game.take_guess(guess)
      print(guess_game.word)
      print(f"Attempts: {guess_game.attempts}")
    except Exception as e:
      print(e)

  print(f"Game finished: {guess_game.status}")
  


# -----------------------------------------------------------------------------
# TestCases
# -----------------------------------------------------------------------------
class TestGuessGame(unittest.TestCase):

  def test_initialize_game(self):
    # arrange
    word = "plataforma"
    attempts = 3

    # act
    guessGame = GuessGame(word, attempts=attempts)

    # assert
    self.assertEqual(word, guessGame.original_word)
    self.assertEqual(word, guessGame.word)
    self.assertEqual(attempts, guessGame.attempts)

  def test_hide_letters(self):
    # arrange
    word = "plataforma"
    attempts = 3

    # act
    guessGame = GuessGame(word, attempts=attempts)
    guessGame.hide_letters()

    # assert
    self.assertNotEqual(word, guessGame.word)


  def test_count_hidden_letters(self):
    # arrange
    word = "plataforma"
    attempts = 3
    max_hidden = round(len(word) * 0.6)

    # act
    guessGame = GuessGame(word, attempts=attempts)
    guessGame.hide_letters()

    # assert
    self.assertLessEqual(guessGame.word.count(guessGame.char), max_hidden)


  def test_guess_length_exception(self):
    # arrange
    word = "plataforma"
    attempts = 3
    max_hidden = round(len(word) * 0.6)

    # act
    guessGame = GuessGame(word, attempts=attempts)
    guessGame.hide_letters()

    # assert
    self.assertRaises(Exception, guessGame.take_guess, "plataformas")


  def test_guess_word(self):
    # arrange
    word = "plataforma"
    attempts = 3

    # act
    guessGame = GuessGame(word, attempts=attempts)
    guessGame.hide_letters()
    guessGame.take_guess(word);

    # assert
    self.assertEqual(guessGame.status, GameStatus.WON)

  def test_guess_word_after_loss(self):
    # arrange
    word = "plataforma"
    attempts = 3

    # act
    guessGame = GuessGame(word, attempts=attempts)
    guessGame.hide_letters()

    try:
      guessGame.take_guess("z");
      guessGame.take_guess("z");
      guessGame.take_guess("z");
      guessGame.take_guess(word)
    except Exception as e:
      print(e)

    # assert
    self.assertEqual(guessGame.status, GameStatus.LOST)


  def test_guess_won(self):
    # arrange
    word = "plataforma"
    attempts = 3

    # act
    guessGame = GuessGame(word, attempts=attempts)
    guessGame.hide_letters()

    try:
      guessGame.take_guess("p");
      guessGame.take_guess("l");
      guessGame.take_guess("a");
      guessGame.take_guess("t");
      guessGame.take_guess("f");
      guessGame.take_guess("o");
      guessGame.take_guess("r");
      guessGame.take_guess("m");
    except Exception as e:
      print(e)

    # assert
    self.assertEqual(guessGame.status, GameStatus.WON)
    self.assertEqual(guessGame.word, guessGame.original_word)

# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # unittest.main() # uncomment for unit test
    manager()
