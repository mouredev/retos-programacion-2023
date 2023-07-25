
// En este ejemplo utilizare la tabla ascii para convertir los numeros
// del teclado T9 a su salida de texto correspondiente

const example = '6-666-88-777-33-3-33-888' // esperado: mouredev
const example2 = '66-7-6-444-66-444-8-3-33-888' // esperado: npminitdev
const example3 = '2-22-222-3-33-333-4-44-444-5-55-555-6-66-666-7-77-777-7777-8-88-888-9-99-999-9999'

function normalizeT9Entry(t9entry){
  let result = '' // resultado final
  let t9letters = t9entry.split('-') // dividimos los numeros en un array separando por el caracter '-'
  for(let i = 0; i < t9letters.length; i++) { // recorremos cada numero/s
    let num = parseInt(t9letters[i][0]); // obtenemos numero individual, pasado a number
    let numCode = t9letters[i][0].charCodeAt(0); // codigo ascii del numero
    let Ascii = 
      numCode + 47 +  /* 1 */
      ((num - 2) * 2) +  /* 2 */
      (t9letters[i].length - 1);  /* 3 */
    /* 
    esta suma se resume asi:
    1 - Al codigo ASCII del numero le suma 47 (47 es la distancia entre el codigo del caracter 2 y el caracter 'a')
    2 - Le sumamos: el numero menos 2 y al resultado lo multiplicamos por 2
    esto es para obtener el codigo ASCII de la primer letra correspondiente al numero del teclado T9 
    (en el caso del numero 7 el codigo de la primera letra (p) es 112)
    3 - Le sumamos: la longitud de la cadena (por ejemplo 777) menos 1
    resultado: el codigo ascii de la letra esperada (para 777 obtenemos 114)
    */
    if(num >= 8) Ascii += 1 // como el numero 7 del teclado T9 tiene 4 letras tenemos que movernos +1 a partir de ahi
    result += String.fromCharCode(Ascii) // concatenamos la letra resultado, y asi con todas las iteraciones
  }
  return result
}

console.log(normalizeT9Entry(example)); // obtenido: mouredev
console.log(normalizeT9Entry(example2)); // obtenido: npminitdev
console.log(normalizeT9Entry(example3)); // obtenido: abcdefghijklmnopqrstuvwxyz

// Nota: esta solucion asume que las entradas siempre son validas, la serie 6666 imprimira 'p' que pertenece al numero 7 del teclado T9
// Mi idea era utilizar la minima cantidad de variables posibles pero para clarificar use mas de las esperadas