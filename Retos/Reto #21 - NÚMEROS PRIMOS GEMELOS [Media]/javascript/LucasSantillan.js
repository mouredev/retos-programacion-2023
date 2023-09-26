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

let rango = 14;
let primosGemelos = paresPirmosGemelos(rango);

console.log(`Rango ${rango}`);
console.log(primosGemelos);

function esPrimo(n){
  let x = 1;
  let r = 0;
  do {
    x++;
    if(n % x === 0) {
      return false;
    }
    r = n / x;
  } while(r >= x)
  return true
}

function paresPirmosGemelos(n) {
  if(n >= 5){
    let primos = [];
    let aux = 3;

    for(let i = 3; i <= n; i++) {
      let b = esPrimo(i);
      if(b === true){
        if(i - aux === 2){
          primos.push(`(${aux}, ${i})`);
        }
        aux = i
      }
    }
    return primos;
  }
  return 'No hay pares de números primos gemelos'
}