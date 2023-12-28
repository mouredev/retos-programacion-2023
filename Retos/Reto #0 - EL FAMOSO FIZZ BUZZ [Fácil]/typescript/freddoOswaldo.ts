/*
 * Reto 0
 * Imprimir los números del 1 al 100
 * Si el número es múltiplo de 3 imprimir "fizz"
 * Si el número es múltiplo de 5 imprimir "buzz"
 * Si el número es múltiplo de 3 y 5 imprimir "fizzbuzz"
 * Si no es múltiplo de 3 o 5 imprimir el número
 */
function printNumbers(limit = 100) {
  const FIZZ = "fizz";
  const BUZZ = "buzz";

  for (let count = 1; count <= limit; count++) {
    let result = "";
    result += !(count % 3) ? FIZZ : "";
    result += !(count % 5) ? BUZZ : "";
    console.log(`${result || count}\n`);
  }
}

printNumbers();
