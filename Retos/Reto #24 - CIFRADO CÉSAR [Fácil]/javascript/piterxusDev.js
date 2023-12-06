/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

function caesarCipher(textToEncrypt, displacement, decode) {
    let originalAlphabet = "abcdefghijklmnñopqrstuvwxyz".repeat(2);
    let lowercaseEncryptedText = textToEncrypt.toLowerCase()
    let cipherText = "";

    for (let i = 0; i < lowercaseEncryptedText.length; i++) {


        if ((originalAlphabet.indexOf(lowercaseEncryptedText[i]) >= 0)) {
            cipherText += originalAlphabet[originalAlphabet.indexOf(lowercaseEncryptedText[i]) + displacement]
        } else {
            cipherText += " "
        }
    }

    if (decode) {
        return `${cipherText}: ${textToEncrypt}`
    }
    return cipherText;
}


