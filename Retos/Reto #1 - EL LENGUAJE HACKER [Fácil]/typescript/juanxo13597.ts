/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

export function hackerSpeak(text: string): string {
    const alphabet = {
        A: '4',
        B: 'I3',
        C: '[',
        D: ')',
        E: '3',
        F: '|=',
        G: '&',
        H: '#',
        I: '1',
        J: ',_|',
        K: '>|',
        L: '1',
        M: '/\\/\\',
        N: '^/',
        O: '0',
        P: '|*',
        Q: '(_,)',
        R: 'I2',
        S: '5',
        T: '7',
        U: '(_)',
        V: '\\/',
        W: '\\/\\/',
        X: '><',
        Y: 'j',
        Z: '2'
    };

    let hackerText = '';
    for (let i = 0; i < text.length; i++) {
        const letter = text[i].toUpperCase();
        hackerText += alphabet[letter] || letter;
    }

    return hackerText;
}
