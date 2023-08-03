/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const symbols = '!"#$%&\'( )*+,-./:;<=>?@[\]^_`{|}~'
const letters = 'abcdefghijklmnopqrstuvwxyz'
const numbers = '1234567890'

function generateRandom(length, {lettersUpValid, lettersLowValid, numbersValid, symbolsValid}){
    let password = ''
    if(length<8 || length >16) password ='La longitud debe estar entre 8 y 16 caracteres'
    else{
        let validChars = ''
        if(lettersUpValid) validChars+=letters.toUpperCase()
        if(lettersLowValid) validChars+=letters
        if(numbersValid) validChars+=numbers
        if(symbolsValid) validChars+=symbols
        
        for(let i=0; i<length; i++){
            password += validChars.charAt(Math.floor(Math.random() * validChars.length))
        }
    }
    return password
}


const options1 = {
    lettersUpValid: false,
    lettersLowValid: true,
    numbersValid: true,
    symbolsValid: true
}
const options2 = {
    lettersUpValid: true,
    lettersLowValid: false,
    numbersValid: false,
    symbolsValid: true
}
const options3 = {
    lettersUpValid: true,
    lettersLowValid: true,
    numbersValid: true,
    symbolsValid: true
}

console.log(generateRandom(15, options1))
console.log(generateRandom(4, options1))
console.log(generateRandom(12, options2))
console.log(generateRandom(14, options3))