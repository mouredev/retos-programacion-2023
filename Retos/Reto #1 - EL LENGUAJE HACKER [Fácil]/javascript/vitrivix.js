/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const leet = `4I3[|)3ph6#1]|<1|\|/\/\0|>0_I257(_)\/\/\/><j2`
const caracteres = {a:'4', b:'I3', c:'[', d:'|)',e:'3', f:'ph', g:'6', h:'#', i:'1', j:']', k:'|<', l:'1', n:'|\\|', m:"/\\/\\", o:'0', p:'|>', q:'0_', r:'I2', s:'5', t:'7', u:'(_)', v:'\\/', w:'\\/\\/', x:'><', y:'j', z:'2'}

function alfaNumericos(arg) {
    const date = arg.toLowerCase().split(' '), result = [];
    for (let element of date){
        for (const jrElement of element) result.push(caracteres[jrElement]);
        result.push(' ');
    } return result.join('');
}
alfaNumericos('Hola Mundo');

