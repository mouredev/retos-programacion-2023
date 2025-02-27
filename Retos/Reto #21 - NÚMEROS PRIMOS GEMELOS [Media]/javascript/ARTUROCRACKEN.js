/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

function isPrimoGemelo(range) {
  let numerosPrimos = [];
  for (let i = 2; i <= range; i++) {
    let esPrimo = true;
    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) {
        esPrimo = false;
        break;
      }
    }
    if (esPrimo) {
      numerosPrimos.push(i);
    }
  }

  let gemelos = [];
  for (let i = 0; i < numerosPrimos.length - 1; i++) {
    if (numerosPrimos[i + 1] - numerosPrimos[i] === 2) {
      gemelos.push([numerosPrimos[i], numerosPrimos[i + 1]]);
    }
  }

  console.log(gemelos);
}

isPrimoGemelo(7)
isPrimoGemelo(14)
isPrimoGemelo(100)
