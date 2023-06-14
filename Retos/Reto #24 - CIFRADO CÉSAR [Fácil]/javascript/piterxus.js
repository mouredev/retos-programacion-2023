function caesarCipher(textToEncrypt, displacement, decode) {
    let originalAlphabet = "abcdefghijklmnñopqrstuvwxyz".repeat(2);
    let cipherText = "";

    for (let i = 0; i < textToEncrypt.length; i++) {


        if ((originalAlphabet.indexOf(textToEncrypt[i]) >= 0)) {
            cipherText += originalAlphabet[originalAlphabet.indexOf(textToEncrypt[i]) + displacement]
        } else {
            cipherText += " "
        }



    }

    if (decode) {
        return `${cipherText}: ${textToEncrypt}`
    }
    return cipherText;

}


console.log(caesarCipher("mi mama me mima", 2, true))