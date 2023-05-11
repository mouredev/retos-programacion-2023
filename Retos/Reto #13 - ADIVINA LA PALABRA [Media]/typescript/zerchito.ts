/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
{
  const prompt = require('prompt-sync')();
  const words = ["mario", "zelda", "pokemon", "tetris", "sonic"];

  class GuesserMan {
    private healthPoints: number;
    private pickedLetters: Set<string>;
    private word: string;

    constructor(guessesLeft: number = 6) {
      this.healthPoints = guessesLeft;
      this.pickedLetters = new Set<string>();
    }

    #guess(letter: string): boolean {
      if (this.pickedLetters.has(letter)) {
        console.log(`You already guessed this letter: '${letter}'`);
        return false;
      }
      this.pickedLetters.add(letter);
      if (this.word.includes(letter)) {
        console.log(`Correct! '${letter}' is in the word.`);
        return true;
      } else {
        this.healthPoints--;
        console.log(`Sorry, letter '${letter}' is not in the word. You have ${this.healthPoints} guesses left.`);
        return false;
      }
    }

    #displayWord(): string {
      return this.word.split("").map((letter) => (this.pickedLetters.has(letter) ? letter : "_")).join("");
    }

    #isTheEnd(): boolean {
      return this.healthPoints <= 0 || this.#displayWord() === this.word;
    }

    
    #startGame() {
      this.word = words[Math.floor(Math.random() * words.length)];
      let letters = this.word.length / 3;
      while (letters > 0) {
        const index = Math.round(Math.random() * (this.word.length - 1));
        const letter = this.word.charAt(index);
        if (!this.pickedLetters.has(letter)) {
          this.pickedLetters.add(letter);
        }
        letters--;
      }
    }

    play(): void {
      this.#startGame();
      console.log("Welcome to GuesserMan! The word is:");
      console.log(this.#displayWord());

      while (!this.#isTheEnd()) {
        const letter = prompt("Guess a letter:")?.toLowerCase();
        if (!letter || letter.length !== 1) {
          console.log("Please enter a single letter.");
          continue;
        }
        this.#guess(letter);
        console.log(this.#displayWord());
      }

      if (this.#displayWord() === this.word) {
        console.log("Congratulations, you guessed the word!");
      } else {
        console.log(`Sorry, you ran out of guesses. The word was '${this.word}'.`);
      }
    }
  }

  const hangman = new GuesserMan();
  hangman.play();

}