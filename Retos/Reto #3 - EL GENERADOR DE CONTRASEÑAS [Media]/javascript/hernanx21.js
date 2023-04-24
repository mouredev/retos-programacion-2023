/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const passGenerator = (length, mayus, numbers, symbols) => {
    const mayusLetters = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ';
    const minLetters = 'abcdefghijklmnñopqrstuvwxyz';
    const numbersLetters = '0123456789';
    const symbolsLetters = '!#$%&/()=?¡*+';
    let pass = '';
    let letters = minLetters;
    
    if (mayus) letters += mayusLetters;
    if (numbers) letters += numbersLetters;
    if (symbols) letters += symbolsLetters;
    
    for (let i = 0; i < length; i++) {
        pass += letters.charAt(Math.floor(Math.random() * letters.length));
    }
    
    return pass;
}

console.log(passGenerator(16, true, false, true));