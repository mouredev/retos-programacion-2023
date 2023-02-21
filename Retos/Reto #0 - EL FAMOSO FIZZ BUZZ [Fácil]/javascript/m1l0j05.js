/*

* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

*/

function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
      if (i % 3 === 0 && i % 5 === 0) {
        console.log(`The number is: FizzBuzz`);
      } else if (i % 5 === 0) {
        console.log(`The number is: Buzz`);
      } else if (i % 3 === 0) {
        console.log(`The number is: Fizz`);
      } else {
        console.log(`The number is: ${i}`);
      }
    }
  }
  
  fizzBuzz();
  
  /* 
  
  OpenAI
  
  Aquí te propongo algunas sugerencias para mejorar el código que has proporcionado:
  Considera utilizar una condición más simple en el bucle for. En lugar de usar i > 0 && i <= 100, puedes usar simplemente i <= 100. Esto hará que el código sea más legible y fácil de entender.
  
  Considera utilizar una tabla de verdad para determinar cuándo se deben imprimir "Fizz", "Buzz" o "FizzBuzz". Esto hará que el código sea más corto y fácil de entender. Por ejemplo:
  
  function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
      let output = "";
      if (i % 3 === 0) output += "Fizz";
      if (i % 5 === 0) output += "Buzz";
      console.log(output || i);
    }
  }
  
  fizzBuzz();
  
  Considera utilizar una función para determinar el resultado para cada número en lugar de hacerlo dentro del bucle for. Esto te permitiría reutilizar la lógica de determinación de "Fizz", "Buzz" o "FizzBuzz" en otros lugares del código. Por ejemplo:
  
  function getFizzBuzz(n) {
    let output = "";
    if (n % 3 === 0) output += "Fizz";
    if (n % 5 === 0) output += "Buzz";
    return output || n;
  }
  
  function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
      console.log(getFizzBuzz(i));
    }
  }
  
  fizzBuzz();
  
  */
  