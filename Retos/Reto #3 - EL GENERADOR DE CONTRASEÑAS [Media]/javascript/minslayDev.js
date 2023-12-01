/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function generatePassword(length, uppercase, numbers, symbols) {
    if (length < 8) {
        return "Password must be at least 8 characters long";
    } else if (length > 16) {
        return "Password must be at most 16 characters long";
    }
    
    var password = "";
    var characters = "abcdefghijklmnñopqrstuvwxyz";
    var charactersUpper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
    var charactersNumber = "0123456789";
    var characertsSymbols = "!@#$%^&*()_+";
    
    if (uppercase) {
        characters += charactersUpper;
    }
    if (numbers) {
        characters += charactersNumber;
    }
    if (symbols) {
        characters += characertsSymbols;
    }
    
    for (var i = 0; i < length; i++) {
        password += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    
    return password;
}


// Testing the function
console.log(generatePassword(7, true, true, true));
console.log(generatePassword(8, true, true, true));
console.log(generatePassword(8, false, true, true));
console.log(generatePassword(8, true, false, true));
console.log(generatePassword(8, true, true, false));
console.log(generatePassword(8, false, false, true));
console.log(generatePassword(8, false, true, false));
console.log(generatePassword(8, true, false, false));
console.log(generatePassword(8, false, false, false));
console.log(generatePassword(16, true, true, true));
console.log(generatePassword(16, false, true, true));
console.log(generatePassword(16, true, false, true));
console.log(generatePassword(16, true, true, false));
console.log(generatePassword(16, false, false, true));
console.log(generatePassword(16, false, true, false));
console.log(generatePassword(16, true, false, false));
console.log(generatePassword(16, false, false, false));
console.log(generatePassword(20, true, true, true));


