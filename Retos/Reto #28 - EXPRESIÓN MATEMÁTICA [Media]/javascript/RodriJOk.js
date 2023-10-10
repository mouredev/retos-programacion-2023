/* Crea una función que reciba una expresión matemática (String)
* y compruebe si es correcta. Retornará true o false.
* - Para que una expresión matemática sea correcta debe poseer
*   un número, una operación y otro número separados por espacios.
*   Tantos números y operaciones como queramos.
* - Números positivos, negativos, enteros o decimales.
* - Operaciones soportadas: + - * / % 
*
* Ejemplos:
* "5 + 6 / 7 - 4" -> true
* "5 a 6" -> false
*/

function expresionMatematica(expresion){
    const regex = /^(\d+\.?\d*|\.\d+)\s[+\-*/%]\s(\d+\.?\d*|\.\d+)(\s[+\-*/%]\s(\d+\.?\d*|\.\d+))*$/;
    return regex.test(expresion);
}

console.log(expresionMatematica("5 + 6 / 7 - 4")); // true
console.log(expresionMatematica("5 a 6")); // false
console.log(expresionMatematica("5 5 5")); // false
console.log(expresionMatematica("%")); // false
console.log(expresionMatematica("5 + ")); // false
console.log(expresionMatematica()); // false
console.log(expresionMatematica("55")); //false
console.log(expresionMatematica("5*5")); //false
console.log(expresionMatematica(1)); //false
console.log(expresionMatematica("10 * 10")); //true