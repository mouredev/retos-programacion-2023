/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const esPrimo = num => {
  let primo = (num<2)? false: true;
  for(let i=2; i<num; i++){
    if(num%i===0) {
      primo = false;
      break;
    }
  }
  return primo;
}

const esFibonacci = num => {
  let a = 0;
  let b = 1;
  while (b<num) {
    let c = a + b;
    a = b;
    b = c;
  }
  return num === b;
}

const retoCuatro = (num) => {
  let result = '';
  if(esPrimo(num)){
    result += `${num} es primo, `;
  } else {
    result += `${num} no es primo, `;  
  }

  if(esFibonacci(num)){
    result += 'es fibonacci ';
  } else {
    result += 'no es fibonacci ';
  }

  if(num%2 === 0){
    result += 'y es par.';
  } else {
    result += 'y no es par.';
  }
  return result;
}