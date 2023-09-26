/* Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)  */

const alphabet = [...Array(26).keys()].map((i) => String.fromCharCode(i + 97).toUpperCase());
const numbers = [...Array(10).keys()];
const symbols = [...Array(14).keys()].map((i) => String.fromCharCode(i + 33));
let password = '';

const randomIndex = (n:number) => Math.floor(Math.random() * n);

const newKeyword = (withLower:boolean, withNumbers:boolean, withSymbols:boolean):string|number => {
  const index = randomIndex(3);
  if (index === 0 && withLower) return alphabet[randomIndex(alphabet.length - 1)].toLowerCase();
  else if (index === 1 && withNumbers) return numbers[randomIndex(numbers.length - 1)]
  else if (index === 2 && withSymbols) return symbols[randomIndex(symbols.length - 1)];
  
  return alphabet[randomIndex(alphabet.length - 1)]
  
};

const generatePassword = (lenght:number = 8, withLower:boolean = false , withNumbers:boolean = false , withSymbols:boolean = false):string => {
  if (lenght >= 8 && lenght <= 16) {
     let index = 0;
     while(index< lenght) {
      password += newKeyword(withLower, withNumbers, withSymbols).toString();
      index++
     }
     return password
  }
  return `length has to between 8 and 16`;
};

console.log(generatePassword(8, false, true, false));
// H00TK7MH
// DI55TP8J