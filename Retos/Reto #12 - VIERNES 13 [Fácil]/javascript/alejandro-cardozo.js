/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
/**
 * This function returns a boolean telling if the month passed as first argument
 * of the year passed as a second argument has a friday the 13th day
 * @param  {Number} month the month of the year to analyze
 * @param  {Number} year the year to analyze
 * @return {Boolean}    a boolean indicating whether there is a friday the 13th or not
 */
function hasHorrorFriday(month, year) {
  const date = new Date(year, month - 1, 13);
  return date.getDay() === 5;
}

// Tests
console.log(hasHorrorFriday(8, 2021)); // True
console.log(hasHorrorFriday(12, 2021)); // False
console.log(hasHorrorFriday(4, 2022)); // False
console.log(hasHorrorFriday(1, 2023)); // True
console.log(hasHorrorFriday(10, 2023)); // True
