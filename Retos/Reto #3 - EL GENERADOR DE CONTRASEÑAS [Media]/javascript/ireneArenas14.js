/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function generatePassword(long, hasUpper, hasNumbers, hasSymbols) {

    const min_long = 8;
    const max_long = 16;
    const upperCasse = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowerCase = 'abcdefghijklmnopqrstuvwxyz';
    const numbers = '0123456789';
    const symbols = '.-+=!¡¿?#$%&/()';
    let string = lowerCase;
    let password = '';

    if (long < min_long || long > max_long) {
        console.log('longitud no válida');
        return;
    }

    if (hasUpper) {
        string+= upperCasse;
    }
    if (hasNumbers) {
        string+= numbers;
    }
    if (hasSymbols) {
        string+= symbols;
    }

    for (let i = 0; i < long; i++) {
        let ind_random = Math.floor(Math.random() * string.length);
        password+=string.charAt(ind_random);
    }

    return password;
    
}

generatePassword(10,true,true,true);
