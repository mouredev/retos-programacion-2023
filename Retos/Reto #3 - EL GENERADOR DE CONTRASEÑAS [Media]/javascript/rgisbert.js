/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min)
}

function getCharacters(options, strLength) {
    const optLength = options.length;

    return new Array(strLength)
        .fill()
        .map(() => options[randomIntFromInterval(0, optLength - 1)])
        .join("")
}

function createPassword({length = 10, upper = true, numbers = true, symbols = true}) {
    // Constants for password length
    const passRange = {
        MAX: 16,
        MIN: 8,
    };
    // Available characters
    const validChar = {
        lower: "abcdefghijklmnopqrstuvwxyz",
        number: "0123456789",
        symbol: "~!@#$%^&*()_-+={[}]|:;<,>.?/",
        upper() { return this.lower.toUpperCase() },
    };

    // Adapt length and create valid string
    const passLength = (passRange.MIN <= length && length <= passRange.MAX)
        ? length 
        : (length < passRange.MIN) ? passRange.MIN : passRange.MAX;
    
    const validOptions = validChar.lower +
        (numbers ? validChar.number : "")  +
        (symbols ? validChar.symbol : "") +
        (upper ? validChar.upper() : "");

    return getCharacters(validOptions, passLength);
}

const options = {length: 12, symbols: false};
console.log( createPassword( options ) );
