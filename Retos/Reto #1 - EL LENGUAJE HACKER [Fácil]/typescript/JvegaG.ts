/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

// Solucion 01: Facil
const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
];

const leetArray = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|',
    '>|', '1', '/\\/\\', '^/', '0', '|*', '(_,)', 'I2', '5', '7', '(_)',
    '\\/', '\\/\\/', '><', 'j', '2'
];

const changeToLeet = (text: string): string => {
    let textToLeet = '';

    text.split('').forEach(item => {
        const character = item.toUpperCase();
        const letterPosition = letters.indexOf(character);

        textToLeet += (letterPosition !== -1) ? leetArray[letterPosition] : character;
    })

    return textToLeet;
}

const textForTest = "Que Dios me ayude con este codigo :)";
const newText = changeToLeet(textForTest);
console.log(newText)



// Solucion 02: compleja (usando Map)
const leetMap = new Map<string, string>()
letters.forEach((item, index) => leetMap.set(item, leetArray[index]));

const newChangeToLeet = (text: string): string => {
    let textToLeet = '';
    text.split('').forEach(item => textToLeet += leetMap.get(item.toUpperCase()) ?? item )

    return textToLeet
}

const secondNewText = newChangeToLeet(textForTest);
console.log(secondNewText)
