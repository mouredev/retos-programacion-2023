
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

/**
 * Funcion que dado un rango de valores buscara los multiplos de los valores de referencia pasados por parametro y colocara las palabras clabes fizz buzz fizzbuzz
 * - Guardara los resultados en una lista que puede contener strings y numbers 
 * - Imprimira la lista de valores con forme se obtengan los resultados, si asi se indica
 * @param {number} range Rango de valores
 * @param {number} reference_one Primer multipo a buscar
 * @param {number} reference_two Segundo multiplo a buscar
 * @param {boolean} printValues Define si se imprimiran los resultados con forme se obtengan
 * @returns {string|number[]} Lista con los resultados obtenidos
 */
const fizzBuzz = (range:number, reference_one:number, reference_two:number, printValues: boolean = true) : Array<string|number> => {
    const result:Array<string | number> = []
    let value: string | number = ''

    for (let i = 0; i <= range; i ++) {
        if (i%reference_one == 0 && i%reference_two == 0 ) value = "fizzbuzz"
        else if (i%reference_one == 0 ) value = "fizz"
        else if (i%reference_two == 0 ) value = "buzz"
        else value = i

        if (printValues) console.log(value)
        result.push(value)
    }

    return result
}

/** Funcion que ejecutara un test para los siguientes valores. 
 * - multiplos de 3  
 * - multiplos de 5 
 * - 100 valores totales*/
const testFizzBuzz = () => {
    const expectedFizz:number[] = [ 3, 6, 9, 12 , 18, 21, 24, 27, 33, 36, 39, 42, 48, 51]
    const expectedBuzz:number[] = [5, 10, 20, 25, 35, 40, 50, 55, 65]
    const expectedFizzBuzz:number[] = [0, 15, 30, 45, 60]

    const response = fizzBuzz(100, 3, 5, false)

   console.log(" ------------------------ ")

   expectedFizz.map((item, index) => {
    if (response[item] == "fizz") console.log(`✅ Fizz ${item} Check`)
    else console.log(`❌ Fizz ${item} Error`)
   })

   console.log(" ------------------------ ")

   expectedBuzz.map((item, index) => {
    if (response[item] == "buzz") console.log(`✅ Buzz ${item} Check`)
    else console.log(`❌ Buzz ${item} Error`)
   })

   console.log(" ------------------------ ")

   expectedFizzBuzz.map((item, index) => {
    if (response[item] == "fizzbuzz") console.log(`✅ FizzBuzz ${item} Check`)
    else console.log(`❌ FizzBuzz ${item} Error`)
   })

   console.log(" ------------------------ ")

}


// Correr la función
fizzBuzz(100, 3, 5, true)

// Correr el test
testFizzBuzz()