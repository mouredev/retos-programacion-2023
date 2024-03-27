/*# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

*/


const checkNum = (number) => {
  // Inicializamos la variable result con el número proporcionado como una cadena
  let result = `${number} `;

  // Comprobación de si es primo
  let esPrimo = true; // Inicializamos esPrimo como verdadero
  if (number > 1) { // Verificamos si el número es mayor que 1
    for (let i = 2; i < number; i++) { // Iniciamos un bucle desde 2 hasta el número 
      if (number % i === 0) { // Si el número es divisible por algún número entre 2 y el número, entonces no es primo
        esPrimo = false; // Cambiamos esPrimo a falso
      }
    }
  } else {
    esPrimo = false; // Si el número es 1 o menor, no es primo
  }
  // Agregamos al resultado si el número es primo o no
  result += esPrimo ? 'es primo, ' : 'no es primo, ';

  // Comprobación de si está en la secuencia de Fibonacci
  // Calculamos si (5 * n^2 + 4) o (5 * n^2 - 4) son cuadrados perfectos
  const esFibonacci = is_perfect_square(5 * number * number + 4) || is_perfect_square(5 * number * number - 4);
  // Agregamos al resultado si el número está en la secuencia de Fibonacci o no
  result += esFibonacci ? 'es Fibonacci, ' : 'no es Fibonacci, ';

  // Comprobación de si es par o impar
  // Verificamos si el número es divisible por 2 para determinar si es par o impar
  result += number % 2 === 0 ? 'es par' : 'es impar';

  // Imprimimos el resultado en la consola
  console.log(result);
}

// Función para verificar si un número es un cuadrado perfecto
const is_perfect_square = (number) => {
  // Calculamos la raíz cuadrada del número
  let sqrt = Math.sqrt(number);
  // Comprobamos si el cuadrado de la raíz cuadrada es igual al número
  return sqrt * sqrt === number;
}

// Ejemplos de uso
checkNum(2); // Salida: "2 es primo, es Fibonacci, es par"
checkNum(7); // Salida: "7 es primo, no es Fibonacci, es impar"
