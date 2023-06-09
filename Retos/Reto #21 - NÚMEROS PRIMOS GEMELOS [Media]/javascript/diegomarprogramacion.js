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
let primos = [];
let primos_gemelos_array = [];
function primos_gemelos(rango) {
  for(let a=1; a<rango+1; a++){
    //console.log("A:"+a);
    let count_primos = 0;
    for(let b=1; b<a+1; b++){
      //console.log("B:"+b);
      if(Number.isInteger(a/b)){
        count_primos++;
      }
    }
    if(count_primos==2){
      //console.log(a)
      primos.push(a)
      if(primos[primos.length-2]==(primos[primos.length-1])-2){
        //console.log(primos[primos.length-2]+" es primo-gemelo de "+primos[primos.length-1])
        let primos_pequeño_array=[primos[primos.length-2],primos[primos.length-1]]
        primos_gemelos_array.push(primos_pequeño_array)
      }
    }
  }
  console.log(primos)
  console.log(primos_gemelos_array)
  return primos_gemelos_array
}

console.log(primos_gemelos(100))