// Reto #3: EL GENERADOR DE CONTRASEÑAS

// Function that returns a random number (integer) between min and max 
function randomNumber(min, max) {
    return Math.floor((Math.random() * (max - min + 1)) + min)
}

// Function that checks the parameters
function exceptions(lengthOfPassword, hasUppercase, hasNumbers, hasSymbols) {
    if (lengthOfPassword < 8 || lengthOfPassword > 16) {
        return [false, "ERROR! The lenght of password must be between 8 and 16"]
    } else if (typeof (hasUppercase) !== "boolean") {
        return [false, "ERROR! The parameter 'hasUpperCase' must be a boolean value [true / false]"]
    } else if (typeof (hasNumbers) !== "boolean") {
        return [false,"ERROR! The parameter 'hasNumbers' must be a boolean value [true/false]"]
    } else if (typeof (hasSymbols) !== "boolean") {
        return [false,"ERROR! The parameter 'hasSymbols' must be a boolean value [true/false]"]
    } 

    return [true]
}

// Main function -> Function that generates a password with some parameters
function passwordGenerator({ lengthOfPassword, hasUppercase, hasNumbers, hasSymbols }) {

    if (!exceptions(lengthOfPassword, hasUppercase, hasNumbers, hasSymbols)[0]) {
        return exceptions(lengthOfPassword, hasUppercase, hasNumbers, hasSymbols)[1]
    }

    let password = ''
    const lowercaseAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    const uppercaseAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const numbers = '1234567890'
    const symbols = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    let allCharacters = lowercaseAlphabet

    hasUppercase ? allCharacters += uppercaseAlphabet : allCharacters
    hasNumbers ? allCharacters += numbers : allCharacters
    hasSymbols ? allCharacters += symbols : allCharacters

    for (let i = 0; i < lengthOfPassword; i++) {
        password += allCharacters[randomNumber(0,allCharacters.length - 1)]
    }

    return password
}

// DEFAULT ARGUMENTS
let lengthOfPassword = 8
let hasUppercase = false
let hasNumbers = false
let hasSymbols = false

console.log("PASSWORD GENERATOR");
console.log("> " + passwordGenerator({lengthOfPassword, hasUppercase, hasNumbers, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword:9, hasUppercase, hasNumbers, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword:11, hasUppercase:true, hasNumbers, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword:13, hasUppercase:true, hasNumbers:true, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword:16, hasUppercase:true, hasNumbers:true, hasSymbols:true}))
console.log("> " + passwordGenerator({lengthOfPassword:7, hasUppercase, hasNumbers, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword:17, hasUppercase, hasNumbers, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword, hasUppercase:null, hasNumbers, hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword, hasUppercase, hasNumbers:"true", hasSymbols}))
console.log("> " + passwordGenerator({lengthOfPassword, hasUppercase, hasNumbers, hasSymbols:0}))

