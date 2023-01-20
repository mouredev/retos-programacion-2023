/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function passwordGenerator(n, hasUpper, hasNum, hasSymbols){
    if(n < 8 || n > 16) return "No puede tener esa longitud!";
    
    const lowerCase = "abcdefghijklmnopqrstuvwxyz";
    const upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numbers = "0123456789";
    const symbols = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/";

    let choices = lowerCase;
    
    if(hasUpper) choices += upperCase;
    if(hasNum) choices += numbers;
    if(hasSymbols) choices += symbols;
    
    let password = "";
    for(let i=0; i<n; i++){
        password += choices[Math.floor(Math.random()*choices.length)];
    }
    
    return password;
}

console.log(passwordGenerator(16, true, true, true));
console.log(passwordGenerator(8, false, false, false));
console.log(passwordGenerator(10, true, true, false));