/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

const isFriday13th = (month, year) => {
    const date = new Date(year, month - 1, 13);
    return date.getDay() === 5;
}

console.log(isFriday13th(5, 2020));
console.log(isFriday13th(10, 2021));
console.log(isFriday13th(5, 2022));
console.log(isFriday13th(7, 2023));
console.log(isFriday13th(6, 2024));
