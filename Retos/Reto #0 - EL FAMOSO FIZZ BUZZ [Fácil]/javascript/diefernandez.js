/*
    Reto 0
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
        - Múltiplos de 3 por la palabra "fizz".
        - Múltiplos de 5 por la palabra "buzz".
        - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

const isMultiple = (number, multiple) => number % multiple === 0

for (let number = 1; number <= 100; number++) {
  if (isMultiple(number, 3) && isMultiple(number, 5)) {
    console.log('buzzfizz')
  } else if (isMultiple(number, 3)){
    console.log('buzz')
  } else if (isMultiple(number, 5)) {
    console.log('fizz')
  } else {
  	console.log(number)
  }
}