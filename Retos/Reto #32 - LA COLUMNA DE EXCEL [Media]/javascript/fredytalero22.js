/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

const getNumberColumn = (strColumn) => {
    const arrAlphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R',  'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z' ]
    const arrCharacter = strColumn.split('')
    const arrNumber = arrCharacter.map(value => arrAlphabet.indexOf(value.toUpperCase())+1)
    const base = arrAlphabet.length
    
    /**
     * Teorema fundamental de la numeración
     * Se dice que es la sumatoria del valor x la base elevado a la cantidad de digitos menos el anterior.
     */
    const output = arrNumber.reduce((total, currentValue, currentIndex)  => {
      return total + currentValue * base ** (arrCharacter.length - 1 - currentIndex)
    }, 0);

    return `${strColumn} = ${output}`
}

console.log(getNumberColumn('A'))
console.log(getNumberColumn('Z'))
console.log(getNumberColumn('AA'))
console.log(getNumberColumn('CA'))