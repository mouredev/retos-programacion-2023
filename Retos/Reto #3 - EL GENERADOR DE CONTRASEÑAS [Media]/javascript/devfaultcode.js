/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const prompt = require('prompt-sync')();

const array = ['ABCDEFGHIJKLMNOPKRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '1234567890', '!#$%&*+-:<=>?@_|~']

array[Math.floor(Math.random() * array.length)];

const max = 16
const min = 8

/* Function to generate a random number between 8 and 16 both include */
function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
}

/* Function to generate combination of password */
function generateP() {
    let pass = '';

    let lenghtpass = getRndInteger(min, max)

    for (let i = 1; i <= lenghtpass; i++) {

        let arrsection = Math.floor(Math.random() * 4) + 1;

        let str = array[arrsection - 1]

        let randomchar = Math.floor(Math.random() * str.length)

        for (let j = 0; j < str.length; j++) {
            if (randomchar === j) {
                pass += str[j]
                break
            }
        }
    }

    return [pass, pass.length];
}

function menu() {

    while (1 === 1) {
        let answer = prompt ('Generate password of length between 8 and 16? (y or n): ')

        if (answer === 'y' || answer === 'Y') {

            let arrpass = generateP();
            console.log('\nYour password is: ' + arrpass[0] + '\nThe length of the password is: ' + arrpass[1] + '\n'); 

        } else if (answer === 'n' || answer === 'N'){

            break

        } else {
            console.log('\nPlease select a valid option (y or n)')
        }
    }
}

menu()
