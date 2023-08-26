/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 *
 *
 * EJERCICIO REALIZADO POR LAURA ORTEGA - 24/08/2023
 */

const letters = "abcdefghijklmnopqrstuvwxyz";
const numbers = "0123456789";
const symbols = "~`!@#$%^&*()_-+={[}]|:;\"'<,>./?";
const upperLetters = letters.toUpperCase();

const passwordGenerator = ( lengthOfPassword, hasUppercase, hasNumbers, hasSymbols ) => {
    
    if (lengthOfPassword<8 || lengthOfPassword>16) {
        return "ERROR! The lenght of password must be between 8 and 16";
    } 

    let characters = letters;
    hasUppercase ? characters += upperLetters : "";
    hasNumbers ? characters += numbers : "";
    hasSymbols ? characters += symbols : "";

    let password = "";

    for(let i = 0; i < lengthOfPassword; i++) {
        password += characters[Math.floor(Math.random() * characters.length)];
    }

    return `Generated password: ${password}`;
}


console.log(passwordGenerator(8, true, true, true));
console.log(passwordGenerator(8, true, true, true));
console.log(passwordGenerator(8, true, false, true));
console.log(passwordGenerator(7, true, true, false));
console.log(passwordGenerator(16, false, true, false));
console.log(passwordGenerator(16, false, false, false));
console.log(passwordGenerator(17, true, true, false));
