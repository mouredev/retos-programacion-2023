/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

let column = 'CA';
console.log(`Column number: ${getColumnNumber(column)}`);

function getColumnNumber(column) {
    if (column && column.match("[^A-Z]") == null) {
        return column.split('').reverse().reduce((acc, cur, idx) => (cur.charCodeAt(0) - 64) * 26**idx + acc, 0);
    } else {
        return "Invalid column!";
    }
}