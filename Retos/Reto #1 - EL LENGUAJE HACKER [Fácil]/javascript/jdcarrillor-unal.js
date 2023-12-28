/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
const readline = require('readline');
console.log("Escibre un texto y yo lo traduzco a lenguaje hacker")
const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
input.question('Escriba un texto en lenguaje natural\n ', function(respuesta) {
    const datos = respuesta
    let resultado = '';
    for (let i = 0; i < datos.length; i++) {
        switch (datos[i].toLowerCase()) {
            case 'a':
                resultado += '4';
                break;
            case 'b':
                resultado += '8';
                break;
            case 'c':
                resultado += '[';
                break;
            case 'd':
                resultado += '|)';
                break;
            case 'e':
                resultado += '3';
                break;
            case 'f':
                resultado += '|=';
                break;
            case 'g':
                resultado += '&';
                break;
            case 'h':
                resultado += '#';
                break;
            case 'i':
                resultado += '1';
                break;
            case 'j':
                resultado += ']';
                break;
            case 'k':
                resultado += '>|';
                break;
            case 'l':
                resultado += '1';
                break;
            case 'm':
                resultado += '/\\/\\';
                break;
            case 'n':
                resultado += '|\\|';
                break;
            case 'o':
                resultado += '0';
                break;
            case 'p':
                resultado += '|*';
                break;
            case 'q':
                resultado += '9';
                break;
            case 'r':
                resultado += '|2';
                break;
            case 's':
                resultado += '5';
                break;
            case 't':
                resultado += '7';
                break;
            case 'u':
                resultado += '|_|';
                break;
            case 'v':
                resultado += '\\/';
                break;
            case 'w':
                resultado += '\\/\\/';
                break;
            case 'x':
                resultado += '><';
                break;
            case 'y':
                resultado += 'j';
                break;
            case 'z':
                resultado += '2';
                break;
            case '1':
                resultado += 'L';
                break;
            case '2':
                resultado += 'R';
                break;
            case '3':
                resultado += 'E';
                break;
            case '4':
                resultado += 'A';
                break;
            case '5':
                resultado += 'S';
                break;
            case '6':
                resultado += 'G';
                break;
            case '7':
                resultado += 'T';
                break;
            case '8':
                resultado += 'B';
                break;
            case '9':
                resultado += 'q';
                break;
            case '0':
                resultado += 'o';
                break;
            default:
                resultado += datos[i];
                break;
        }
    }

    console.log(resultado);
    input.close();
});