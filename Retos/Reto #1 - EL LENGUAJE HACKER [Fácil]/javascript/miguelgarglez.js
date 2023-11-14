/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const sustitucionesLeet = {
    ' ': ' ',
    'a': '4',
    'b': '|3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': '/\\/\\',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><',
    'y': 'j',
    'z': '2'
  };
  
function transformacion(texto) {
    let resultado = ''
    for (caracter of texto) {
        if(caracter in sustitucionesLeet){
            //console.log('La sustitución para el caracter ' + caracter + ' es: ' + sustitucionesLeet[caracter])
            resultado += sustitucionesLeet[caracter]
        } else {
            //console.log('No se ha encontrado el caracter ' + caracter + 'en el diccionario de traducción')
        }
    }
    return resultado
}

rl.question('Introduce el texto a transformar: ', (userInput) => {
    let textoLeet = transformacion(userInput)
    console.log('La transformación resultante es: \n' + textoLeet);
    rl.close();
});

