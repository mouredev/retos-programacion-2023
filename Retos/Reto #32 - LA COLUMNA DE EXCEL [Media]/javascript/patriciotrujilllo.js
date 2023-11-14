/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

function calculatorColumns (column) {
    const toArray = column.toUpperCase().split('')
    const abecedario = 'abcdefghijklmnopqrstuvwxyz'.toUpperCase().split('')

    numberString = []
    let acumulator = 0

    abecedario.forEach((char,index)=>{
        numberString[char] = index +1
    })

    let j = toArray.length-1

    for (item of toArray){
        const valor = numberString[item]
        const m = Math.pow(26,j)
        acumulator = acumulator + valor*m
        j--
    }
    return acumulator
}
console.log( calculatorColumns('z'))
console.log( calculatorColumns('ad'))
console.log(calculatorColumns('aa'))
console.log(calculatorColumns('ca'))

console.log(calculatorColumns('cac'))
