/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
// shift must be 3 and must incñude ascii ñ character

function caesarCipher(plainText) {
    let cipherText = "";
    for (let i = 0; i < plainText.length; i++) {
        let ascii = plainText.charCodeAt(i);
        if (ascii >= 65 && ascii <= 90) {
            ascii = ascii + 3;
            if (ascii > 90) {
                ascii = ascii - 26;
            }
        } else if (ascii >= 97 && ascii <= 122) {
            ascii = ascii + 3;
            if (ascii > 122) {
                ascii = ascii - 26;
            }
        }
        cipherText += String.fromCharCode(ascii);
    }
    return cipherText;
}

function caesarUncipher(cipherText) {
    let plainText = "";
    for (let i = 0; i < cipherText.length; i++) {
        let ascii = cipherText.charCodeAt(i);
        if (ascii >= 65 && ascii <= 90) {
            ascii = ascii - 3;
            if (ascii < 65) {
                ascii = ascii + 26;
            }
        } else if (ascii >= 97 && ascii <= 122) {
            ascii = ascii - 3;
            if (ascii < 97) {
                ascii = ascii + 26;
            }
        }
        plainText += String.fromCharCode(ascii);
    }
    return plainText;
}

let text = "¡acbdxyz ABCDXYZ!";
console.log(text)
let cipherText = caesarCipher(text);
console.log(cipherText);
let plainText = caesarUncipher(cipherText);
console.log(plainText);