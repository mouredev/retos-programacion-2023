/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import randomstring = require('randomstring');

function generatePassword(length: number = 12, useUppercase: boolean = true, useNumbers: boolean = true, useSymbols: boolean = true): string {
    let characters = '';
    // Validar la longitud de la contraseña
    if (length <= 8 || length => 16) {
        prompt("Error: la longitud de la contraseña debe estar entre 8 y 16");
        return;
    }
      
    // Crear una lista de caracteres permitidos
    if (useUppercase) {
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    }
    if (useNumbers) {
        characters += '0123456789';
    }
    if (useSymbols) {
        characters += '!@#$%^&*()_+-=[]{}\\|;:\'",.<>/?';
    }
    if (!useUppercase && !useNumbers && !useSymbols) {
        characters += 'abcdefghijklmnopqrstuvwxyz';
    }
      
    // Generar una contraseña aleatoria utilizando los caracteres permitidos   
    let password = randomstring.generate({
        length: length,
        charset: characters
    });
    return password;
}

// Ejemplo de uso
let password = generatePassword();
console.log(password);
