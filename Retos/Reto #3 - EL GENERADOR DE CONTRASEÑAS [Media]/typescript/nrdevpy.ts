/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

type options = {
    mayus: boolean,
    numbers: boolean,
    simbols: boolean,
}

function getPassword(length: number, object: options): string {
    try {
        if (length >= 8 && length <= 16) {
            let characters = 'abcdefghijklmnopqrstuvwxyz';
            let counter = 0;
            let result = '';
    
            if (object.mayus) {
                characters += characters.toUpperCase();
            }
            if (object.numbers) {
                characters += '1234567890';
            }
            if (object.simbols) {
                characters += '!@#$%^&*';
            }
            while (counter < length) {
                const randomIndex = Math.floor(Math.random() * characters.length);
                result += characters[randomIndex];
                ++counter;
            }
            return result;
        } else {
            return 'Please introduce a length between 8 and 16';
        }
    } catch (err) {
        console.log(err)
        throw err
    }
}

// Testing
const cases = [
    {
        mayus: true,
        numbers: true,
        simbols: true,
    },
    {
        mayus: true,
        numbers: true,
        simbols: false,
    },
    {
        mayus: true,
        numbers: false,
        simbols: false,
    },
    {
        mayus: false,
        numbers: false,
        simbols: false,
    },
    {
        mayus: false,
        numbers: true,
        simbols: true,
    },
    {
        mayus: false,
        numbers: true,
        simbols: false,
    },
    {
        mayus: false,
        numbers: false,
        simbols: true,
    },
]
for (let i = 0; i < cases.length; ++i) {
    console.log(getPassword(8, cases[i]))
    console.log(getPassword(12, cases[i]))
    console.log(getPassword(16, cases[i]))
}

// Error Test
console.log(getPassword(7, cases[0]));