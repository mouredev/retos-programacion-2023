
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
*/


function columnNumberExcel (columnName){

    let columnNumber = 0;
    let letters = columnName.split('');
    for (let i = 0; i < letters.length; i++) {
        let value = letters[i].toUpperCase().charCodeAt(0) - 64;
        columnNumber += value * ( 26 ** (letters.length - i - 1));
    }
    return columnNumber;
}

console.log(columnNumberExcel('A'));
console.log(columnNumberExcel('Z'));
console.log(columnNumberExcel('AA')); 
console.log(columnNumberExcel('CA'));
console.log(columnNumberExcel('BAR')); 