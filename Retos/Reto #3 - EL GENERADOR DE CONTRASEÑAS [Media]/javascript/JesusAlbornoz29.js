// /*
//  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
//  * Podrás configurar generar contraseñas con los siguientes parámetros:
//  * - Longitud: Entre 8 y 16.
//  * - Con o sin letras mayúsculas.
//  * - Con o sin números.
//  * - Con o sin símbolos.
//  * (Pudiendo combinar todos estos parámetros entre ellos)
//  */

function generateRandomPassword(length, useLowerCase, useUpperCase , useNumbers, useSymbols) {
    const lowerCaseChars = "abcdefghijklmnopqrstuvwxyz";
    const upperCaseChars = lowerCaseChars.toUpperCase();
    const numberChars = "0123456789";
    const symbolChars = "!$%^&*_+";

    
    let passwordChars = "";
    let password = "";

    if (useUpperCase == true){
        passwordChars += upperCaseChars;
    }
    if (useNumbers == true){
        passwordChars += numberChars;
    }
    if (useSymbols == true){
        passwordChars += symbolChars;
    }
    if (useLowerCase == true){
        passwordChars += lowerCaseChars;
    }
        for (let i = 0; i < length; i++){
            const randomIndex = Math.floor(Math.random() * passwordChars.length);
            const randomChar = passwordChars[randomIndex];
            password += randomChar;
        }
        return password;
}

console.log(generateRandomPassword(8,true,true,true,true));