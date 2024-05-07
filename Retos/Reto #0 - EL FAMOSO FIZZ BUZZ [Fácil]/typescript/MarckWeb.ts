/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const printfizzBuzz = () => {
   for (let i: number = 0; i < 101; i++) {
      let output: string = ''
      if (i % 3 == 0) output = 'fizz'
      if (i % 5 == 0) output = 'buzz'
      if (i % 3 == 0 && i % 5 == 0) output = 'fizzbuzz'

      console.log(`${i}= ${output}`)
   }
}

printfizzBuzz()