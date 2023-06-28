/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

function cesarCipher (text, number){
    let cipher = ''
    for (let i = 0; i < text.length; i++){
        let char = text.charCodeAt(i)     
        if (char >= 65 && char <= 90){
            char = ((char - 65 + number+26) % 26) + 65
        }
        else if (char >= 97 && char <= 122){
           char = ((char - 97 + number+26) % 26) + 97
        }
        cipher += String.fromCharCode(char)
    }
    return cipher;
}

function cesarDecipher (text, number){
    return cesarCipher(text, - number)
}

console.log(cesarCipher('Hola mundo!', 3))
console.log(cesarDecipher('Krod pxqgr!', 3))

console.log(cesarCipher('Hola mundo!', 9))
console.log(cesarDecipher('Qxuj vdwmx!', 9))

