// Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
// Podrás configurar generar contraseñas con los siguientes parámetros:
// - Longitud: Entre 8 y 16.
// - Con o sin letras mayúsculas.
// - Con o sin números.
// - Con o sin símbolos.
// (Pudiendo combinar todos estos parámetros entre ellos)

// Configuraciones:
const passwordLength = 8;
const withUpperCase = true;
const withNumbers = true;
const withSymbols = true;

function generateTextDescriptions() {
    let textUpperCase;
    let textNumbers;
    let textSymbols;
    if (withUpperCase) {
        textUpperCase = 'has uppercase characters';
    } else {
        textUpperCase = 'has not uppercase characters';
    }
    if (withNumbers) {
        textNumbers = 'has numbers';
    } else {
        textNumbers = 'has not numbers';
    }
    if (withSymbols) {
        textSymbols = 'has symbol characters';
    } else {
        textSymbols = 'has not symbol characters';
    }
    return [textUpperCase, textNumbers, textSymbols];
}

function addRandomCharacter() {
    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()-_=+';

    let chars = lowercaseChars;
    if (withUpperCase) {
        chars += uppercaseChars;
    }
    if (withNumbers) {
        chars += numberChars;
    }
    if (withSymbols) {
        chars += symbolChars;
    }
    const randomCharachter = chars[Math.floor(Math.random() * chars.length)];

    return randomCharachter;
}

function generatePassword() {
    const texts = generateTextDescriptions();
    const [textUpperCase, textNumbers, textSymbols] = texts;
    let password = '';
    console.log('Welcome to the password generator');
    console.log(
        `Your password has ${passwordLength} elements ${textUpperCase}, ${textNumbers} and ${textSymbols}`,
    );
    for (let i = 0; i < passwordLength; i++) {
        password += addRandomCharacter();
    }
    console.log(`*********************************
    Your password is: ${password}
*********************************`);
}

generatePassword();
