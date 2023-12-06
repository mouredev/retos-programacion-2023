/*
 * Reto #8 - El generador pseudoaleatorio
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 23/02/2023
 */

var lastXDigits = 0;

function getRandomNumber() {
  // Get current date datetime
  const date = new Date().getTime();

  // Convert datetime to string
  const dateToString = date.toString();

  // Get last digit from datetime
  const lastDigit = parseInt(dateToString[dateToString.length - 1], 10);

  // Get X last numbers from datetime (1, 2 or 3)
  switch(lastDigit) {
    case 0:
    case 1:
    case 4:
    case 7:
      lastXDigits = 1;
      break;
    case 2:
    case 5:
    case 8:
      lastXDigits = 2;
      break;
    default:
      lastXDigits = 3;
  }

  // Get last X digits. If greater than 100 then return only 2 digits
  const result = parseInt(dateToString.slice(-lastXDigits));
  return result > 100 ? parseInt(dateToString.slice(-lastXDigits + 1)) : result;
}

console.log('Getting random number between 1 and 100: ', getRandomNumber());
