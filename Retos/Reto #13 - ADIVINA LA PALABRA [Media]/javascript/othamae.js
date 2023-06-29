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

const readline = require('readline')


const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    
    })


const hideWord = (word) => {
    let hiddenWord = word.split('');
    let num = Math.floor(word.length * 0.6)
    while (num >0) {
        const randomIndex = Math.floor(Math.random() * word.length)
        let letter = hiddenWord[randomIndex]
        if (letter !== '_') {  
            for(let i = 0; i < word.length; i++){
            if(word[i] === letter){
                hiddenWord[i] = '_'
            }
        }
        }        
        num--
    }
    return hiddenWord.join('')
}

const wordFound = (wordToCheck, word) => {   
    let wordToCheckString = wordToCheck.join('')
    if (wordToCheckString === word) {
        console.log('You win!')
        rl.close()
        return true
    } 
    return false
}

const letterFound = (letter, word) => {
    return word.includes(letter)
}
const openLetter = (userGuess, word, hiddenWord) => {
    let newHiddenWord = hiddenWord.split('')
    const wordArray = word.split('')
    if (word.includes(userGuess[0])) {   
        for (let i = 0; i < word.length; i++) {
            if (wordArray[i] === userGuess[0]) {               
                newHiddenWord[i] = userGuess[0]
            }
        }       
    }     
    return newHiddenWord.join('')

}

const guessWord = (word, attempts) => {
    console.log('Try to guess the word, you have ' + attempts + ' attempts')
    let hiddenWord = hideWord(word)
    console.log('The word is: ' + hiddenWord)
         rl.on('line', (input) => {
            let userInput = input.trim()  
            let userGuess = userInput.split('')
            if((userGuess.length > 1 && userGuess.length != word.length) || userInput=== ''){
                console.log('You must write a word or a letter')
             } else if(userGuess.length === 1){
                letterFound(userGuess[0], word) ? hiddenWord = openLetter(userGuess, word, hiddenWord) : attempts--
               wordFound(hiddenWord.split(''), word)  ? `Word found!! ${word}` : console.log('Try again, you have ' + attempts + ' attempts')        
            } 
             if (userGuess.length === word.length ) {
                wordFound(userGuess, word)  ? `Word found!! ${word}` : attempts--                               
             }           
        
        if (attempts === 0) {
           console.log('No more attempts, you lose 😢')  
            rl.close()     
        } else {       
            console.log('The word is: ' + hiddenWord)
        }
        
       
        })
             
        
}
       

const playGame = (word, attempts) => { 
    guessWord(word, attempts)
}


playGame("holacaracola", 5)