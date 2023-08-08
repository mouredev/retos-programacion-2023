/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */


function column(name){
    let column = 0
    const letters = name.split('')
    for (let i = 0; i < letters.length; i++) {
        const value = letters[i].toUpperCase().charCodeAt(0) - 64
        column += value * Math.pow(26, letters.length - i - 1)
    }
    return column
}

console.log(column('AA')) // 27
console.log(column('CA')) // 79
console.log(column('AAA')) // 703
console.log(column('GHE')) // 4945