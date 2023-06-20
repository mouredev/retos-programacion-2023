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

import { createInterface } from 'readline/promises'
import { stdin, stdout }  from 'process'
import  chalk  from "chalk";
import fetch from "node-fetch";


/**
 * API para obtener palabras aleatorias
 */
const API_WORDS = "https://clientes.api.greenborn.com.ar/public-random-word?c=9&l=8"

/**
 * Funcion de extension para obtener todos los indices de una ocurrrencia de un string
 */
declare global {
    interface String {
        indexAllOf(search: string): number[]
    }
}

String.prototype.indexAllOf = function (search: string):number[] {
    let indexes = [], i = -1;
    while ((i = this.indexOf(search, i+1)) != -1){
        indexes.push(i);
    }
    return indexes;
}


/**
 * Interfaz para representar una letra y su posicion dentro de una palabra
 */
interface Letter {
    letter: string
    position: number
}


/**
 * Clase para manejar la logica de las palabras
 */

class GuessWord{


    private readonly _originalWord :string
    private _secretWord :string
    private _lettersUsed :string[] = []
    private _letters:Letter[] = []

    /**
     * Constructor de la clase
     * @param word Palabra original a adivinar
     * @param handicap Porcentaje de letras a ocultar
     */

    constructor(word:string, handicap:number){
        this._originalWord = word
        const numChars = Math.floor(this._originalWord.length * handicap)
            let offuscated = this._originalWord
            for (let i = 0; i < numChars; i++) {
                const position = Math.floor(Math.random() * this._originalWord.length)
                offuscated = offuscated.substring(0, position) + '_' + offuscated.substring(position + 1)

            }

       this._letters = offuscated.split('').reduce((acc: Letter[], current: string, index: number) =>
            (current === '_' ? acc : [...acc, { letter: current, position: index }]), []);
       this._secretWord = this.offuscate()


    }

    /**
     * Metodo estatico para obtener una palabra aleatoria de la API
     */
    public static getWord(): Promise<string> {
        return new Promise((resolve, reject) => {
            fetch(API_WORDS)
                .then((res:any) => res.json())
                .then((data:string[]) => {
                    resolve(data[0])
                })
                .catch((err: any) => reject(err))

        })


    }

    /**
     * Metodo para ocultar las letras de la palabra
     * @private
     */
    private offuscate(): string {
        return this._originalWord.split('').map((c,i)=> this._letters?.some((l)=> l.position===i)? c:'_').join('')

    }

    /**
     * Metodo para agregar una letra usada a la lista de letras que ya se han usado y no estan en la palabra
     * @param letter
     */
    public addUsedLetter(letter:string):void{
        if(!this._lettersUsed.some((l)=> l===letter)) {
            this._lettersUsed.push(letter)
        }
    }

    /**
     * Metodo para obtener las letras usadas que no estan en la palabra
     */
    public lettersUsed():string{
        return this._lettersUsed.map((l)=>l).join(',')
    }

    /**
     * Metodo para agregar una letra que si esta en la palabra
     * @param letter
     */
    public addLetter(letter:Letter):boolean{

        if(this._letters.some((l)=> l.position===letter.position && l.letter=="_")){
            return false
        }else{
            this._letters.push(letter)
            this._secretWord = this.offuscate()
            return true
        }
    }

    /**
     * Devuelve la palabra ofuscada
     */

    public get secretWord(){
        return this._secretWord
    }

}


/**
 * Clase para manejar la logica del juego
 */
class HangedGame {
    private _attempts: number
    private readonly _word: string
    private _guessWord: GuessWord
    private readonly _maxAttempts: number
    private _isFinish: boolean
    userInterface = new UserInterface()

    /**
     * Constructor de la clase
     * @param word Palabra a adivinar
     */
    constructor(word: string) {
        this._word = word
        this._attempts = 1
        this._isFinish = false
        this._maxAttempts = this.userInterface.HangedInput.length
        this._guessWord = new GuessWord(word, 0.6)
    }

    /**
     * Metodo que devuelve la palabra que se debe adivinar ofuscada
     */

    public get guessWord(): string {
        return this._guessWord?.secretWord
    }

    /**
     * Metodo que devuelve si el juego ha terminado o no
     */
    get isFinish(): boolean {
        return this._isFinish
    }

    /**
     * Numero de intentos que se han realizado
     */

    get attempts() {
        return this._attempts
    }

    /**
     * Metodo que devuelve la palabra original
     */
    get word() {
        return this._word
    }

    /**
     * Metodo para adivinar una letra de la palabra
     * Si es una sola letra se agrega a la lista de letras usadas
     * Si es mas de una letra se intenta adivinar la palabra
     * @param letter Letra a adivinar o palabra a adivinar
     */

    public guessLetter(letter: string): boolean {

        //Intento de palabra
        if (letter.length > 1) {
            if(letter === this._word) {
                console.log(chalk.bgGreenBright(`¡¡¡Has ganado!!! La palabra que buscamos es ${chalk.greenBright(this._word)}`))
                //this._winner = true
                this._isFinish = true
                return true
            }else{
                this._attempts++
                console.log(chalk.redBright("ERROR : La palabra no es correcta"))
                if (this._attempts > this._maxAttempts) {
                    console.log(chalk.bgCyanBright(`¡¡¡Has perdido!!! La palabra que buscamos es ${chalk.greenBright(this._word)}`))
                    this._isFinish = true
                }
                return false
            }
            //Intento de letra
        } else {
            if (this._word.includes(letter)) {
                this._word.indexAllOf(letter).forEach((i) => {
                    if (this._guessWord.addLetter({letter: letter, position: i})) {
                        if (this._guessWord.secretWord === this._word) {
                            console.log(chalk.bgGreenBright(`¡¡¡Has ganado!!! La palabra que buscamos es ${chalk.greenBright(this._word)}`))
                         //   this._winner = true
                            this._isFinish = true
                            return true
                        }
                    }
                })
            } else {
                this._attempts++
                this._guessWord.addUsedLetter(letter)
                console.log(chalk.redBright("ERROR : La letra no está en la palabra"))

                if (this._attempts > this._maxAttempts) {

                    console.log(chalk.bgCyanBright(`¡¡¡Has perdido!!! La palabra que buscamos es ${chalk.greenBright(this._word)}`))
                    this._isFinish = true
                }

                return false
            }
            return false
        }

    }


    /**
     * Metodo asincrono para iniciar el juego
     */
    async play() {

        console.log("Bienvenido al juego del ahorcado")
        console.log("================================\n")
        while (!this.isFinish) {

            console.log(chalk.greenBright(this.userInterface.HangedInput[this._attempts-1]))
            console.log(chalk.blue(`Palabra a adivinar: ${this.guessWord}`))
            console.log(`Intentos restantes : ${this._maxAttempts - this._attempts+1}`)
            console.log(`Letras usadas: ${this._guessWord.lettersUsed()}`)
            let input= await this.userInterface.prompt(chalk.whiteBright(`Ingresa una letra:`))
            this.guessLetter(input)
        }
    }

}


/**
 * Clase para manejar la interfaz de usuario
 *
 */

class UserInterface{

   public HangedInput:string[] = [`
                            +---+\n 
                            |   |\n 
                            O   |\n 
                            |   |\n
                                |\n
                                |\n
                        =========`,`
                            +---+\n 
                            |   |\n 
                            O   |\n 
                           /|\\  |\n
                                |\n
                                |\n
                        =========`,`
                            +---+\n 
                            |   |\n 
                            O   |\n 
                           /|\\  |\n
                                |\n
                                |\n
                        =========`,`
                            +---+\n 
                            |   |\n 
                            O   |\n 
                           /|\\  |\n
                           /    |\n
                                |\n
                        =========`,`
                            +---+\n 
                            |   |\n 
                            O   |\n 
                           /|\\  |\n
                           / \\  |\n
                                |\n
                        =========`,



    ]

    /**
     * Metodo para leer una entrada de texto
     * @param message Mensaje a mostrar al usuario
     */
    async prompt(message: string): Promise<string> {
        const readLineInterface = createInterface(stdin, stdout)
        let response = await readLineInterface.question(message)
        readLineInterface.close()
        return response
    }

}


/**
 * Inicio del juego
 */

const word = await GuessWord.getWord()
let game = new HangedGame(word)
game.play()






