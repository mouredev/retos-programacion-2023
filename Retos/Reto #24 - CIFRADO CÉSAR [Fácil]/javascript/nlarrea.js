/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

const alphabet = 'abcdefghijklmnñopqrstuvwxyz';

const cesarCipher = (text, number = 3, cipher = true) => {
    const cipheredText = text.toLowerCase().split('').map(char => {
        const currentPosition = alphabet.split('').findIndex(letter => letter === char);

        if (currentPosition !== -1 && cipher) {
            let position = currentPosition + number;

            if (position >= alphabet.length) {
                position = Math.abs(alphabet.length - position);
            }

            return alphabet[position]
        } else if (currentPosition !== -1) {
            let position = currentPosition - number;

            if (position < 0) {
                position = alphabet.length + position;
            }

            return alphabet[position]
        } else {
            return char;
        }
    });

    return cipheredText.join('');
};


console.log(cesarCipher('Hola mundo!'));                        // krñd oxpgr!
console.log(cesarCipher('abcdefghijklmnñopqrstuvwxyz'));        // defghijklmnñopqrstuvwxyzabc
console.log(cesarCipher('abcdefghijklmnñopqrstuvwxyz', 5));     // fghijklmnñopqrstuvwxyzabcde

console.log(cesarCipher('krñd oxpgr!', 3, false));              // hola mundo!