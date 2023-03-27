var longitud = prompt("Dime la longitud de la contrasenya: ");
var mayusculas = prompt("Dime si quieres mayusculas: ");
var numeros = prompt("Dime si quieres numeros: ");
var simbolos = prompt("Dime si quieres simbolos: ");

function crearContrasenya(longitud, mayusculas, numeros, simbolos) {
    var contrasenya = ''
    var alphabet = 'abcdefghijklmnopqrstuvwxyz'
    const lowerCase = [...alphabet];
    const upperCase = [...alphabet.toUpperCase()];
    const numbers = [...'1234567890'];
    const symbols = [...'!@#$%^&*()-_=+\|[]{}:;"\',./<>?'];
    var characters = lowerCase


    if (mayusculas == 'y') {
        characters.push(...upperCase)
    }

    if (numeros == 'y') {
        characters.push(...numbers)
    }

    if (simbolos == 'y') {
        characters.push(...symbols)
    }

    var comprobador = 1
    while (longitud >= comprobador) {
        // get random index value
        const randomIndex = Math.floor(Math.random() * characters.length);

        // get random item
        const item = characters[randomIndex];
        contrasenya += item
        comprobador++
    }

    return contrasenya
}

// 16,y,y,y
console.log(crearContrasenya(longitud, mayusculas, numeros, simbolos)) // Z"6V[/(K,FqG;YuV
//14,y,n,n
console.log(crearContrasenya(longitud, mayusculas, numeros, simbolos)) // jPjgZCgdtJyJej
//10,n,y,y
console.log(crearContrasenya(longitud, mayusculas, numeros, simbolos)) // ldpw_;k95w
