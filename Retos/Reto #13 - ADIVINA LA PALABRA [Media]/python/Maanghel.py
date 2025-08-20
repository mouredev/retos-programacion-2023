"""
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
- El juego comienza proponiendo una palabra aleatoria incompleta
    - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
    la palabra a adivinar)
    - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
        uno al número de intentos
    - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
        al número de intentos
    - Si el contador de intentos llega a 0, el jugador pierde
- La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
    ocultando más del 60%
- Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

import random

class Game:
    """
    A simple word guessing game where the player has to guess
    a randomly chosen word by suggesting letters or the full word.

    Attributes:
        words (list[str]): List of possible words for the game.
        replace_probabilities (float): Maximum percentage of letters that can be hidden.
        max_attempts (int): Maximum number of attempts allowed.
        random_word (str): The randomly chosen word for the game.
        current_lyrics (list[str]): The current state of the word with hidden/revealed letters.
        attempts_left (int): Number of attempts the player has left.
    """

    words = [
        "murcielago", "python", "programacion", "desarrollo", "reto", "palabra", "adivina", "juego",
        "computadora", "teclado", "raton", "pantalla", "internet", "variable", "funcion", "bucle",
        "condicional", "lista", "diccionario", "conjunto", "tupla"
    ]
    replace_probabilities = 0.6

    def __init__(self, max_attempts: int = 6) -> None:
        """
        Initialize the game with a random word and hidden letters.

        Args:
            max_attempts (int): Maximum number of attempts allowed. Default is 6.
        """
        self.max_attempts = max_attempts
        self.random_word = random.choice(self.words)
        self.current_lyrics = self._generate_incomplete_word()
        self.attempts_left = self.max_attempts

    def _generate_incomplete_word(self) -> list[str]:
        """
        Generate the word with randomly hidden letters, ensuring no more
        than 60% of the word is hidden.

        Returns:
            list[str]: The word represented as a list with some letters replaced by '_'.
        """
        max_hidden = int(len(self.random_word) * self.replace_probabilities)
        num_letters_to_hide = random.randint(1, max_hidden)
        hidden_positions = random.sample(range(len(self.random_word)), num_letters_to_hide)

        return [
            "_" if i in hidden_positions else char
            for i, char in enumerate(self.random_word)
        ]

    def main(self) -> None:
        """
        Run the main game loop until the player wins or runs out of attempts.
        """
        while self.attempts_left > 0:
            self._display_round()
            user_input = input("Ingresa una letra o la palabra completa: ").lower()

            if len(user_input) == 1 and user_input.isalpha():
                self._guess_letter(user_input)
            elif len(user_input) == len(self.random_word):
                self._guess_word(user_input)
            else:
                print("Entrada invalida. Intente de nuevo.")

            if "_" not in self.current_lyrics:
                print(f"Felicidades!! Completaste la palabra: {self.random_word}")
                return

        print(f"Te quedaste sin intentos! La palabra era: '{self.random_word}'.")

    def _guess_letter(self, letter: str) -> None:
        """
        Check if the guessed letter is in the word.

        Args:
            letter (str): The guessed letter.
        """
        if letter in self.random_word:
            for i, char in enumerate(self.random_word):
                if char == letter:
                    self.current_lyrics[i] = letter
            print(f"Correcto! La palabra ahora es: {''.join(self.current_lyrics)}")
        else:
            self.attempts_left -= 1
            print(f"Respuesta incorrecta. Intentos restantes: {self.attempts_left}")

    def _guess_word(self, word: str) -> None:
        """
        Check if the guessed word matches the random word.

        Args:
            word (str): The guessed word.
        """
        if word == self.random_word:
            print(f"Ganaste! La palabra es: '{self.random_word}'.")
            self.current_lyrics = list(self.random_word)
            return
        else:
            self.attempts_left -= 1
            print(f"Respuesta incorrecta. Intentos restantes: {self.attempts_left}")

    def _display_round(self) -> None:
        """
        Display the current round number, attempts left, and the incomplete word.
        """
        print(f"\nRonda: {(self.max_attempts - self.attempts_left) + 1} de {self.max_attempts}")
        print(f"Palabra incompleta: {''.join(self.current_lyrics)}")
        print("-" * 50)


if __name__ == "__main__":
    game = Game()
    game.main()
