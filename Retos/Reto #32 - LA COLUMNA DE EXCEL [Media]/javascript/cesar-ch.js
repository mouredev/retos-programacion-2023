/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */


const columnNumber = (column) => {
    let result = 0;
    for (let i = 0; i < column.length; i++) {
        result = result * 26 + column.toUpperCase().charCodeAt(i) - 64;
    }
    return result;
}

console.log(columnNumber('A'))
console.log(columnNumber('Z'))
console.log(columnNumber('AA'))
console.log(columnNumber('CA'))