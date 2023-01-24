/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


/**
 * Genera una contraseña aleatoria con los parámetros indicados.
 * @param length Longitud de la contraseña. Por defecto 12.
 * @param flagUpperCase Indica si la contraseña debe contener letras mayúsculas. Por defecto true.
 * @param flagNumbers Indica si la contraseña debe contener números. Por defecto true.
 * @param flagSymbols Indica si la contraseña debe contener símbolos. Por defecto true.
 */
function generatePassword(length: number = 12, flagUpperCase:boolean=true, flagNumbers:boolean=true, flagSymbols:boolean=true): string {
    const regexgen = require("randexp");
    let password = ""

    if (length <= 8 || length >= 16) {
        return "La longitud de la contraseña debe estar entre 8 y 16"
    }

    // Crear una lista de caracteres permitidos
    let regCharacters:RegExp = new RegExp(/[a-z]/)

    if (flagUpperCase) {
        regCharacters = concatRegexp(regCharacters, /[A-Z]/);
    }

    if (flagNumbers) {
        regCharacters = concatRegexp(regCharacters, /[0-9]/);

    }
    if (flagSymbols) {
        regCharacters = concatRegexp(regCharacters,  /^[.:%\-ÁÉÍÓÚÜÑÇ\/*,<>=+_;()\nªº]/);
    }


    // Generar una contraseña aleatoria utilizando la expresion regular generada
    let randExp = new regexgen(regCharacters)


    for (let i = 0; i < length; i++) {
        password += randExp.gen()
    }

    return password;
}


/**
 * Concatena dos expresiones regulares
 * @param regExp1 Expresión regular 1
 * @param regExp2 Expresión regular 2
 */
function concatRegexp(regExp1:RegExp, regExp2:RegExp):RegExp {
    let flags = regExp1.flags + regExp2.flags;
    flags = Array.from(new Set(flags.split(''))).join();
    return new RegExp(regExp1.source +'|'+ regExp2.source, flags);
}


/**
 * Ejemplo de uso
 */

console.log(generatePassword(12,true,true,true))
console.log(generatePassword(10,true,false,true))
console.log(generatePassword(9,true,true,false))
console.log(generatePassword(12,false,false,true))
console.log(generatePassword(1,true,false,false))

