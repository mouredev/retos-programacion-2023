/**
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 * @param {boolean} upperCase false default
 * @param {boolean} numbers false default
 * @param {boolean} symbols false default
 * @param {number} long 8 default
 * @returns
 */
const passwordGenerator = function (
  upperCase = false,
  numbers = false,
  symbols = false,
  long = 8
) {
  long = long >= 8 && long < 17 ? long : 8;

  const alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  const symbolsList = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "+",
    "{",
    "}",
    "]",
    "[",
    ":",
    "~",
  ];
  const numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
  let n = 0;
  let output = "";

  do {
    // If numbers are required add a random one
    if (randomNumber(4) == 1 && numbers == true) {
      output += numberList[randomNumber(numberList.length)];
    }
    // if symbols are needed
    else if (randomNumber(4) == 2 && symbols == true) {
      output += symbolsList[randomNumber(symbolsList.length)];
    }
    //   if UpperCase letters are needed
    else if (randomNumber(4) == 3 && upperCase == true) {
      output += alpha[randomNumber(alpha.length)].toUpperCase();
    } else {
      output += alpha[randomNumber(alpha.length)];
    }
    n++;
  } while (n < long);

  return output;
};

/**
 * Generate a random number given the max value
 * @param {number} max
 * @returns
 */
const randomNumber = function (max) {
  return Math.floor(Math.random() * max);
};

// const charNum = 12;
// const myOutPut = passwordGenerator(false, false, false, charNum);
// console.log(`Password: ${myOutPut} of ${myOutPut.length} Characters`);
