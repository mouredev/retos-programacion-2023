/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

function caesarCipher(text, shift = 3, decrypt = false) {

    if (!decrypt) {
        return text.split('').map(e => {
            if (e.match(/[a-z]|[A-Z]/)) {
                if (97 <= e.charCodeAt() && e.charCodeAt() <= 122 && e.charCodeAt() + shift > 122) {
                    return String.fromCharCode(e.charCodeAt() + shift - 26)
                } else if (65 <= e.charCodeAt() && e.charCodeAt() <= 90 && e.charCodeAt() + shift > 90) {
                    return String.fromCharCode(e.charCodeAt() + shift - 26)
                }
                else {
                    return String.fromCharCode(e.charCodeAt() + shift)
                }
            } else {
                return e
            }

        }).join('')
    } else {
        return text.split('').map(e => {
            if (e.match(/[a-z]|[A-Z]/)) {
                if (97 <= e.charCodeAt() && e.charCodeAt() <= 122 && e.charCodeAt() - shift < 97) {
                    return String.fromCharCode(e.charCodeAt() - shift + 26)
                } else if (65 <= e.charCodeAt() && e.charCodeAt() <= 90 && e.charCodeAt() - shift < 65) {
                    return String.fromCharCode(e.charCodeAt() - shift + 26)
                } else {
                    return String.fromCharCode(e.charCodeAt() - shift)

                }
            } else {
                return e
            }
        }).join('')
    }
}

console.log(caesarCipher('Mi nombre es MoureDev.', 3, false))
console.log(caesarCipher('Pl qrpeuh hv PrxuhGhy.', 3, true)) 
