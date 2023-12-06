/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

const isFridayThirteen = (month, year) => {
    const date = new Date(year, month - 1, 13);
    return date.getDay() === 5;
}

console.log(isFridayThirteen(1, 2023));     // true
console.log(isFridayThirteen(3, 2022));     // false
console.log(isFridayThirteen(3, 2020));     // true