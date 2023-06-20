import { createInterface } from 'readline/promises'
import { stdin, stdout }  from 'process'
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

export class WordGenerator {
  generate() {
    const words = ['aligator','barbeque','constant','dinosaur','elementary']
    return words[Date.now() % words.length]
  }
}

export class WordOffuscator {
  public readonly offuscatedWord: string
  public readonly chars : {
    char: string,
    position: number
  }[]

  constructor(public readonly originalWord, numChars, chars?) {
    if (!chars) {
      this.chars = originalWord.split('').reduce((acc, current, index) => 
      ((index + 1) % Math.round(originalWord.length / numChars) === 0) ? 
      [...acc, { char: current, position: index}] :
      acc
      , [])
    } else {
      if (chars.length !== numChars || chars.some(c => c.char !== originalWord.charAt(c.position))) {
        throw new Error('The chars provided doesnt match with the word')
      }
      this.chars = chars
    }
    this.offuscatedWord = originalWord.split('').map((current, index) => this.chars.some(c => c.position === index) ? '_' : current).join('')
  }
}

export class Game {
  public get offuscatedWord() : string {
    return this._wordOffuscator?.offuscatedWord
  }
  
  private _remainingAttemps: number
  public get remainingAttemps() : number {
    return this._remainingAttemps
  }

  private _solved: boolean
  public get solved() : boolean {
    return this._solved
  }
  
  public get isOver() : boolean {
    return !this._solved && !this._remainingAttemps
  }
  
  constructor(private _wordOffuscator: WordOffuscator, attempts: number, private _ui?: UI) {
    this._remainingAttemps = attempts
    this._solved = false
  }

  guess(input: string): boolean {
    if (this._remainingAttemps === 0) {
      throw new Error('No remaining attempts')
    }
    const incorrectInputLength = input.length != 1 && input.length != this._wordOffuscator.offuscatedWord.length
    if (incorrectInputLength) {
      throw new Error('Input should be a single character or the complete word')
    }

    if (input === this._wordOffuscator.originalWord) {
      this._solved = true
      return true
    }
    const matchedChar = this._wordOffuscator.chars.find(c => c.char === input)
    if (matchedChar) {
      this._wordOffuscator = new WordOffuscator(
        this._wordOffuscator.originalWord,
        this._wordOffuscator.chars.length - 1,
        this._wordOffuscator.chars.filter(c => c.char !== input)
        )
      this._solved = !this._wordOffuscator.chars.length
      return true
    }
    this._remainingAttemps = this._remainingAttemps - 1
    return false
  }

  async play() {
    if(!this._ui) {
      throw new Error('Theres no UI available to start the game')
    }
    while(!this.isOver) {
      const input = await this._ui.ask(`Guess a character or the complete word for [${this.offuscatedWord}]:`)
      try {
        const correctGuess = this.guess(input)
        if(this._solved) {
          this._ui.show('Congrats, you have guessed the word!!!')
          return
        }
        if (correctGuess) {
          this._ui.show('Your guess was right!')
          continue
        } 
        if (!this.isOver) {
          this._ui.show(`You missed, but you still have ${this.remainingAttemps} remaining attempts`)
        }
      } catch (error) {
        this._ui.show(`Error: ${error.message}`)
      }
    }
    this._ui.show('You missed and it was your last attempt, sorry game over :-(')
  }
}

export class UI {
  async ask(message: string): Promise<string> {
    const readLineInterface = createInterface(stdin, stdout)
    const response = await readLineInterface.question(message)
    readLineInterface.close()
    return response
  }

  show(message: string) {
    console.log(message)
  }
}

const game = new Game(new WordOffuscator(new WordGenerator().generate(), 4), 3, new UI())
game.play()