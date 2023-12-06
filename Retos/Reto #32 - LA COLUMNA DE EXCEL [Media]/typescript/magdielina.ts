/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79
 */

let c: string = 'CA';
console.log(`Column number: ${readColumnNumber(c)}`);

function readColumnNumber(column: string): string {
    if (column && column.match("[^A-Z]") == null) {
        return column.split('').reverse().reduce((acc, cur, idx) => (cur.charCodeAt(0) - 64) * 26**idx + acc, 0).toLocaleString();
    } else {
        return "Invalid column!";
    }
}