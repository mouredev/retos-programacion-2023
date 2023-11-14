/*
 * Crea una función que reciba una expresión matemática (String)
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

const tuplaOperaciones = ['+','-','*','/','%']

const expresionMatematica = (expresion) =>{
    const ToArray = expresion.split(' ')

    for(let i=0;i<=ToArray.length-3;i+=2){

        if(ToArray.length<3) return false

        if(isNaN(Number(ToArray[i]))){
            return false
        }
        if(!tuplaOperaciones.includes(ToArray[i+1])){
            return false
        }
        if(isNaN(Number(ToArray[i+2]))){
            return false
        }
        return true
    }
}

console.log(expresionMatematica("5 + 6 / 7 - 4"))//---->true
console.log(expresionMatematica("5 * 6 / 7 + 4"))//---->true
console.log(expresionMatematica("5 * 6 / -7 + 4 % 3"))//---->true
console.log(expresionMatematica("-5 * 6 / 7 + 4 % 3"))//---->true
console.log(expresionMatematica("5 a 6")) //---->false
console.log(expresionMatematica("a * 6")) //---->false
console.log(expresionMatematica("5 x 6")) //---->false
console.log(expresionMatematica("5 * b")) //---->false