/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

// Array of ASCII values of the A-Z chars
const asciiValues = Array(26).fill().map((_, idx) => 65 + idx);

function checkErrors(column) {
    if (typeof column !== "string") throw TypeError("You have to enter a String.");
    
    column = column.toUpperCase();
    
    if (column.length < 1) throw SyntaxError("You have to give at least one letter as column name.");
    if (column.charCodeAt() < asciiValues[0] ||
        column.charCodeAt() > asciiValues[asciiValues.length - 1]) {
        throw RangeError("The given column name is out of range.");
    }
}

function getColumnNumber(column) {
    // Checking errors
    
    try {
        checkErrors(column);
    } catch (err) {
        return err;
    }

    // Get column number

    column = column.toUpperCase();
    const reversedColumnArr = column.split('').reverse();
    
    return reversedColumnArr.reduce((total, current, idx) => {
        const currentColPosition = asciiValues.indexOf(current.charCodeAt()) + 1;

        // asciiValues.length ** idx = number of turns to the A-Z values (starts at idx = 0)
        return total + ((asciiValues.length ** idx) * currentColPosition);
    }, 0);
}


console.log(getColumnNumber('A'));      // 1
console.log(getColumnNumber('Z'));      // 26
console.log(getColumnNumber('AA'));     // 27
console.log(getColumnNumber('CA'));     // 79

// Checking errors
console.log(getColumnNumber(''));       // SyntaxError: You have to give at least one letter as column name.
console.log(getColumnNumber(2));        // TypeError: You have to enter a String.
console.log(getColumnNumber('_'));      // RangeError: The given column name is out of range.