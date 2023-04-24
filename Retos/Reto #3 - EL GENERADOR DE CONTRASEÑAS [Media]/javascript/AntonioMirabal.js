/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
const LETTERS = "ABCDEFGHIJKLMNÑOPKRSTUVWXYZ"
const DIGITS = "1234567890";
const SYMBOLS = "!#$%&*+-:<=>?@_|~";

const randomChar = (array) => array.charAt(Math.round(Math.random() * array.length));

function generatePassword(length, withUpperLetters, withNumbers, withSymbols){
    if(length < 8 || length > 16) return Error("Solo se puede generar contraseñas con minimo de 8 Caracteres y maximo 16 Caracteres.");
    else{
      let tempPassword = "";
      let characters = LETTERS.toLowerCase() + (withUpperLetters ? LETTERS : "") + (withNumbers ? DIGITS : "") + (withSymbols ? SYMBOLS : "");
        for(let i = 0; i < length; i++){
            tempPassword += randomChar(characters);
        }
        return tempPassword;
    }
}

// Casos de Prueba.
const randomBool = () => Math.random() > 0.5 ? true : false;
for(let i = 0; i < 10; i++){
    let len = Math.round(Math.random() * 8) + (16 - 8);
    console.log(generatePassword(len, randomBool(), randomBool(), randomBool()));
}

/*
 * Asi es como tenemos un generador de contraseñas co tan solo 33 Lineas de codigo(16 solo si contamos el codigo del generador)
 * Author: AntonioMirabal (CodeBlocks)
 * Github: https://github.com/AntonioMirabal
 */